# nomentra.app

Static website for Nomentra: plain HTML and one stylesheet. No build step, no scripts, no analytics, no third-party files.

| Path | Page |
|---|---|
| `index.html` | Homepage — https://nomentra.app/ |
| `privacy/index.html` | Privacy Policy — https://nomentra.app/privacy |
| `support/index.html` | Support — https://nomentra.app/support |
| `404.html` | Not-found page (served by GitHub Pages) |
| `style.css` | Shared style. Colours are the app's Phase B tokens from `Nomentra/DesignSystem/DesignSystemColorTokens.swift`; type is system serif (New York) for titles and system sans (SF Pro) for text. The homepage's top band is the app's brand ribbon: `homeHero` colours and `RibbonArtwork.swift` geometry at rest (single style) |
| `assets/` | App icon sizes, the sharing image (`og.png`, drawn from `tools/og.html`) and four app images (`app-home-ribbon.webp`, `app-tracker-detail.webp`, `app-calendar-month.webp`, `app-country-page.webp`) |
| `tools/update-captures.py` | Turns `captures/<slot>.png` into the four app images (786 × 1704 WebP), with a placeholder for any slot that has no capture; `--og` also redraws `og.png`. Needs Pillow; `--og` needs Google Chrome |
| `captures/` | Local only (ignored by Git, so never published): the PNG captures the tool reads |
| `favicon.ico`, `favicon-32.png`, `apple-touch-icon.png` | Icons, made from the app's `AppIcon-Light-1024.png` |
| `CNAME`, `.nojekyll`, `robots.txt` | GitHub Pages custom domain, no Jekyll processing, allow indexing |

## Sources

- **App images**: placeholders (Warm stone canvas with the wordmark) until the next build's captures exist. Save each as a portrait iPhone PNG, light appearance, under `captures/` as `home-ribbon.png` (Home with the ribbon hero and trackers), `tracker-detail.png` (a tracker's detail page), `calendar-month.png` (the calendar month with flags) and `country-page.png` (a country page with photos); run `python3 tools/update-captures.py`; then replace each image's alt text in `index.html` ("Nomentra") with a description of what it shows. The six earlier captures (app commit `0c760521`, synthetic data) showed the retired photo hero and were removed; their originals stay in `/Users/ossianhouse/APP Dev/nomentra-site-captures/`.
- **Homepage copy**: the owner's final App Store description of 13 October 2026 (tagline, lead, Collect the world, Relive every trip, Know where you stand, Private, on your phone, Plans) and the app's not-advice sentence (`AppCopy` `notAdvice`), which every page's footer carries. The band's six short lines are the store screenshot captions.
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
