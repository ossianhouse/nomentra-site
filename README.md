# nomentra.app

Static site for Nomentra, served by GitHub Pages at https://nomentra.app.

| Path | Page | Source of the text |
|---|---|---|
| `index.html` | Landing page: name, one line, links to Privacy and Support | owner ruling add. 182 (C) |
| `privacy/index.html` | https://nomentra.app/privacy | Nomentra repo, `docs/02-pre-building/12-app-store-readiness-specification/0004-privacy-policy-draft-2026-09-06.md` on `main` at `7b9480a0`, verbatim |
| `support/index.html` | https://nomentra.app/support | same folder, `0005-support-page-draft-2026-09-06.md` at `7b9480a0`, verbatim |
| `style.css` | shared style: the fixed Phase B palette and the Decision 0176 type ladder (New York titles, SF Pro text), values from `Nomentra/DesignSystem/DesignSystemColorTokens.swift` and `docs/02-pre-building/15-design-playbook/country-cover-final.html` on main | |
| `CNAME` | custom domain for GitHub Pages | |

## Go-live (do all of this within the same hour; .app is HTTPS-only)

1. On github.com create a **public** repository `ossianhouse/nomentra-site` and upload the contents of this folder (keep the `privacy/` and `support/` folders).
2. Repository **Settings → Pages**: source = branch `main`, folder `/ (root)`. Custom domain = `nomentra.app`. Tick **Enforce HTTPS** as soon as it becomes available (up to 24 hours after DNS).
3. Squarespace **Domains → nomentra.app → DNS**: delete the four Squarespace `A` records on `@` and add GitHub's four; change `www` from `ext-sq.squarespace.com` to `ossianhouse.github.io`. Leave `MX 1 smtp.google.com` and the Google `TXT` record untouched (they carry support@nomentra.app).

```
A      @     185.199.108.153
A      @     185.199.109.153
A      @     185.199.110.153
A      @     185.199.111.153
CNAME  www   ossianhouse.github.io
```

4. In `ossianhouse/ossianhouse-site` upload the three changed files (`index.html`, `privacy.html`, `support.html`) so the old pages forward to nomentra.app.
5. Check https://nomentra.app/privacy and https://nomentra.app/support in a private window; then tick row 97 of the TestFlight checklist.

## Updating

- The "Last updated" date on the privacy page is the day it is published. Change it whenever the policy text changes.
- Held sentences (iCloud, file backup, optional downloads, opt-in diagnostics) live as hold notes in record 0004; publish them here on the day those controls ship.
