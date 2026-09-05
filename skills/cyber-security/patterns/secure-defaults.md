# Secure defaults library

Copy-paste starting points so reviews can diff against "hardened by default" instead of inventing baselines. Every entry = something to check for or adopt. Not exhaustive — the right default beats a long list.

## HTTP headers (all responses)

```
Content-Security-Policy: default-src 'self'; frame-ancestors 'none'; base-uri 'none'
Strict-Transport-Security: max-age=63072000; includeSubDomains
X-Content-Type-Options: nosniff
Referrer-Policy: no-referrer or strict-origin-when-cross-origin
X-Frame-Options: DENY (legacy; CSP frame-ancestors preferred)
Cache-Control: no-store          # on authenticated API responses
```

## Cookies (session/auth)

```
Set-Cookie: session=...; HttpOnly; Secure; SameSite=Lax|Strict; Path=/; Max-Age=...
```
- New session ID on login and on privilege change; server-side revoke on logout.

## Node / Express

- `app.disable('x-powered-by')`; helmet for headers.
- Parameterized queries always (`db.query('... WHERE id = $1', [id])`).
- Body limits: `express.json({ limit: '100kb' })`.
- Bind allowlists: pick fields explicitly, never `req.body` spread into models (F035).
- Session store: Redis/memory-store with TTL; rotate secret per env.

## Python / FastAPI / Django

- Pydantic `model_config = ConfigDict(extra='forbid')` (blocks mass assignment).
- ORM always (SQLAlchemy/Django ORM); never f-string SQL.
- `allow_origins` explicit list; never `*` with credentials.
- Django: `SECURE_SSL_REDIRECT`, `SESSION_COOKIE_SECURE`, `CSRF_COOKIE_SECURE`, check `DEBUG=False` in prod.
- FastAPI: dependency-based auth per route; `OAuth2PasswordBearer` + short-lived JWT.

## Java / Spring

- Disable Actuator endpoints or bind to management port + internal interface.
- `HttpSecurity`: CSRF on for session apps; stateless JWT → CSRF off but tokens short-lived.
- Jackson: `@JsonIgnoreProperties(ignoreUnknown=true)` on inbound DTOs with explicit fields.
- Prepared statements / JPA; no string-concatenated JPQL.

## Go

- `http.Server{ ReadHeaderTimeout, ReadTimeout, WriteTimeout, IdleTimeout }` always set (slowloris).
- `database/sql` + parameterized queries; `html/template` (auto-escapes) over `text/template`.

## Postgres

- App role: no `SUPERUSER`, no `CREATE`, grants limited to needed tables (separate migration role).
- `ssl=on` + client cert or scram; `log_connections`/`log_disconnections`.
- Row-level security for multi-tenant tables (`CREATE POLICY tenant_isolation USING (tenant_id = current_setting('app.tenant')::uuid)`).

## Redis

- `requirepass` or ACL users; `bind` internal interface; `protected-mode yes`.
- No `FLUSHALL`/`CONFIG` for app user; TLS if crossing networks; TTL on session keys.

## Nginx / reverse proxy

```
server_tokens off;
ssl_protocols TLSv1.2 TLSv1.3;
add_header X-Content-Type-Options nosniff always;
client_max_body_size 10m;      # align with app limit
limit_req_zone ...             # basic rate limit zone for auth routes
```

## Docker

```dockerfile
USER nonroot
COPY --chown=nonroot:nonroot ...
```
- Specific tags (`node:20.11-slim`), never `latest`; read-only rootfs; `--cap-drop=ALL --security-opt=no-new-privileges`; no secrets in ENV/layers (build args leak into history).

## JWT (when used)

- alg allowlist server-side (`HS256`/`RS256` only, never trust header).
- `exp` short (5–15 min access), `aud`/`iss` validated, refresh tokens rotated with reuse detection.
- Claims computed server-side; never accept role/permissions from client-provided payload.

## OAuth / OIDC

- `state` + PKCE for all clients (public ones mandatory).
- `redirect_uri` exact match allowlist; narrowest scopes; validate `nonce` for ID tokens.

## Cloud IAM (generic)

- One role per workload; no wildcard actions/resources; humans via SSO groups not direct binds.
- Storage: private by default; public only via signed URLs / explicit opt-in bucket policy.

## CI/CD

- `permissions: contents: read` default per workflow; secrets never passed to fork PRs; third-party actions pinned by full SHA.

## TLS baseline

- TLS 1.2+ only, modern ciphers, HSTS, automated renewal monitored; mTLS for service-to-service where feasible.
