# PR security gate (defensive)

Use before merge (Fast: skim · Max: full).

- [ ] No secrets in diff  
- [ ] AuthZ on new routes (deny by default)  
- [ ] User-controlled IDs checked against session  
- [ ] Inputs validated at boundary  
- [ ] Dangerous sinks reviewed (SQL, exec, HTML, path, deserialize, SSRF fetch)  
- [ ] New dependencies justified + locked  
- [ ] Errors don’t leak stacks/PII to clients  
- [ ] Logging includes security events, not secrets  
- [ ] Rate limits on auth and expensive endpoints  
- [ ] Tests: happy + forbidden access + one abuse case  
- [ ] Migrations safe / reversible  
- [ ] Feature flags for risky rollouts  
