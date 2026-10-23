import json
from urllib.parse import urlparse

import asyncpg
from workers import Response, WorkerEntrypoint


class Default(WorkerEntrypoint):
    async def fetch(self, request):
        path = urlparse(request.url).path
        hd = self.env.HYPERDRIVE

        conn = await asyncpg.connect(
            host=hd.host,
            port=int(hd.port),
            user=hd.user,
            password=hd.password,
            database=hd.database,
            ssl=False,  # Hyperdrive handles TLS to your database
        )
        try:
            rows = await conn.fetch("SELECT id, name, price FROM products ORDER BY id")
        finally:
            await conn.close()

        products = [{"id": r["id"], "name": r["name"], "price": float(r["price"])} for r in rows]

        if path == "/api/products":
            return Response(json.dumps(products), headers={"Content-Type": "application/json"})

        items = "".join(f"<li>{p['name']} - ${p['price']:.2f}</li>" for p in products)
        html = f"""<!doctype html>
<html><head><meta charset="utf-8"><title>Hello World</title></head>
<body>
  <h1>Hello World from Python on Cloudflare!</h1>
  <h2>Products from PostgreSQL</h2>
  <ul>{items}</ul>
  <p>JSON version: <a href="/api/products">/api/products</a></p>
</body></html>"""
        return Response(html, headers={"Content-Type": "text/html; charset=utf-8"})
