# nomentra.app

Static website for Nomentra: plain HTML and one stylesheet. No build step, no scripts, no analytics, no third-party files.

| Path | Page |
|---|---|
| `index.html` | Homepage — https://nomentra.app/ |
| `privacy/index.html` | Privacy Policy — https://nomentra.app/privacy |
| `support/index.html` | Support — https://nomentra.app/support |
| `404.html` | Not-found page (served by GitHub Pages) |
| `style.css` | Shared style. Colours are the app's Phase B tokens from `Nomentra/DesignSystem/DesignSystemColorTokens.swift`; type is system serif (New York) for titles and system sans (SF Pro) for text |
| `assets/` | App icon sizes, the sharing image (`og.png`) and three app captures |
| `favicon.ico`, `favicon-32.png`, `apple-touch-icon.png` | Icons, made from the app's `AppIcon-Light-1024.png` |
| `CNAME`, `.nojekyll`, `robots.txt` | GitHub Pages custom domain, no Jekyll processing, allow indexing |

## Sources

- **App captures** (`assets/app-home.webp`, `app-status.webp`, `app-travel.webp`): real renders of the app at commit `0c760521`, mounted by a throwaway capture test with synthetic data only (a UK traveller, eight trips in 2026, a Schengen tracker, two personal trackers and a passport deadline). No personal data. Full-size originals and `notes.md` are in `/Users/ossianhouse/APP Dev/nomentra-site-captures/`.
- **Privacy Policy**: written from the app source on `main` at `f0210f43` (1 October 2026), approved wording in `docs/PRD_wording.md`, Feature PRD 13 and WEB-01/02 in `docs/plan/settings-release-simplification.md`. Re-check it whenever the app's data practices change, and change the “Last updated” date.
- **Review**: reconciled against app main `1ca17eda` on 1 October 2026 (`Nomentra-clean/docs/audits/website-source-review-2026-10-01.md`). Send feedback and the privacy link are implemented on main; distribution and website publication are separate.

## Preview locally

```
python3 -m http.server 8765 --bind 127.0.0.1
```

Then open http://127.0.0.1:8765/.

## Publication

Live since 2 October 2026 at https://nomentra.app, served by GitHub Pages from `main` of `ossianhouse/nomentra-site` (custom domain `nomentra.app`, HTTPS enforced).

DNS is managed in Squarespace (**Domains → nomentra.app → DNS Settings**):

```
A      @     185.199.108.153
A      @     185.199.109.153
A      @     185.199.110.153
A      @     185.199.111.153
CNAME  www   ossianhouse.github.io
MX     @     smtp.google.com  (priority 1)   — mail, do not change
TXT    @     google-site-verification=…      — do not change
```

To update the site: commit on `main`, then `git push origin main`. This repository uses its own deploy key (`core.sshCommand` in the local git config). Pages redeploys within a minute or two.

This site and the company site (ossianhouse.com) are kept independent: no links from here to the company site.
