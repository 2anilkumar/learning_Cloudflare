# py-pg-app

Python Worker + PostgreSQL (via Hyperdrive), auto-deployed from GitHub to Cloudflare Workers.

## One-time setup

1. Run `schema.sql` in your Postgres database (e.g. Neon free tier).
2. Create the Hyperdrive config and copy the printed ID into `wrangler.toml`:
   ```bash
   npx wrangler login
   npx wrangler hyperdrive create my-pg-hyperdrive \
     --connection-string="postgres://user:password@host:5432/dbname"
   ```
3. Create a Cloudflare API token (dashboard > My Profile > API Tokens > "Edit Cloudflare Workers" template).
4. In GitHub: Settings > Secrets and variables > Actions, add:
   - `CLOUDFLARE_API_TOKEN`
   - `CLOUDFLARE_ACCOUNT_ID` (shown on the Workers & Pages overview page)
5. Push to `main`. The workflow in `.github/workflows/deploy.yml` deploys automatically.

## Local dev

```bash
export WRANGLER_HYPERDRIVE_LOCAL_CONNECTION_STRING_HYPERDRIVE="postgres://user:password@host:5432/dbname"
uv run pywrangler dev
```
