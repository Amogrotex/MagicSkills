# Secure defaults (remediation patterns)

Guidance for **owners** — not attack recipes.

## Cookies / sessions
- `Secure` + `HttpOnly` + explicit `SameSite`  
- Rotate session on login; invalidate on logout/password change  
- Short idle timeout for sensitive apps  

## Passwords
- Store with modern KDF (argon2id/bcrypt/scrypt) — never plain/reversible  
- Separate “reset token” random, single-use, short TTL  

## Tokens
- Prefer opaque server-side sessions for browsers when possible  
- JWT: short TTL, audience/issuer checks, no secrets in frontend code  
- Bind refresh tokens; revoke list/rotation  

## HTTP headers (baseline)
- HSTS (HTTPS sites)  
- CSP appropriate to app  
- `X-Content-Type-Options: nosniff`  
- Frame protections as needed  

## CORS
- Explicit allowlist; no `*` with credentials  

## CORS/CSRF
- State-changing requests need anti-CSRF or same-site + custom header patterns  

## API AuthZ
- Authorize every object access server-side  
- Never trust client `userId` / `isAdmin` fields  

## SSRF
- Allowlist schemes/hosts; block link-local/metadata IPs; no raw user URLs to fetchers  

## Uploads
- Randomize stored names; separate domain; size/type caps; scan async; no exec path  

## Rate limits
- Per-IP + per-account on login, OTP, reset, expensive search  

## Secrets
- Env/vault only; never commit; rotate on leak; redact logs  
