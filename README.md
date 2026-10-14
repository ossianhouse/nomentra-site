# nomentra.app

Static website for Nomentra: plain HTML and one stylesheet. No build step, no scripts, no analytics, no third-party files.

| Path | Page |
|---|---|
| `index.html` | Homepage — https://nomentra.app/ |
| `privacy/index.html` | Privacy Policy — https://nomentra.app/privacy |
| `support/index.html` | Support — https://nomentra.app/support |
| `404.html` | Not-found page (served by GitHub Pages) |
| `style.css` | Shared style. Colours are the app's Phase B tokens from `Nomentra/DesignSystem/DesignSystemColorTokens.swift`; type is system serif (New York) for titles and system sans (SF Pro) for text. The homepage's top band is the app's brand ribbon: `homeHero` colours and `RibbonArtwork.swift` geometry at rest (single style) |
| `assets/` | App icon sizes, the sharing image (`og.png`, drawn from `tools/og.html`), five app images (`app-home-ribbon.webp`, `app-tracker-detail.webp`, `app-calendar-month.webp`, `app-country-page.webp`, `app-trip-page.webp`) and the App Store badge placeholder (`app-store-badge.svg`, to be replaced by Apple's badge and the store link at launch) |
| `tools/update-captures.py` | Turns `captures/<slot>.png` into the five app images (786 × 1704 WebP), with a placeholder for any slot that has no capture; `--og` also redraws `og.png`. Needs Pillow; `--og` needs Google Chrome |
| `captures/` | Local only (ignored by Git, so never published): the PNG captures the tool reads |
| `favicon.ico`, `favicon-32.png`, `apple-touch-icon.png` | Icons, made from the app's `AppIcon-Light-1024.png` |
| `CNAME`, `.nojekyll`, `robots.txt` | GitHub Pages custom domain, no Jekyll processing, allow indexing |

## Sources

- **App images**: captured on 14 October 2026 from app `main` at `7a054ed7` by the mounted capture suite `NomentraTests/Features/Verification/SiteStoreCaptureTests.swift` (`website()`), a 393 × 852 pt window rendered at 3×, light appearance. The data is benchmark persona P04 (Cyprus-based mobile resident, `NomentraTests/Fixtures/FirstScanRealityBenchmark/expected/personas/P04.json`) loaded through the app's DEBUG testing-profile loader and the shipping first-scan path, its 2025 dates moved forward by exactly one year and cut at the capture clock (14 October 2026, 18:00 in Cyprus). Its located photos show the app's own bundled catalogue pictures, added to the simulator's Photos library. Synthetic data only. Slots under `captures/`: `home-ribbon.png`, `tracker-detail.png`, `calendar-month.png`, `country-page.png`, `trip-page.png`; run `python3 tools/update-captures.py`, then describe each image in its alt text in `index.html`, with the figures it shows.
- **Regenerating the images** (after a merge to app `main`; the suite lives on app branch `tools/site-captures-20261014` until merged): from the app checkout, with an iPhone 17 Pro Max simulator booted, one command builds, prepares the simulator's synthetic Photos library, runs the suite and copies the PNGs:

  ```
  zsh Scripts/site-captures/capture.sh <simulator udid> "/Users/ossianhouse/APP Dev/nomentra-site/captures" "$HOME/Desktop/nomentra-store-screenshots"
  ```

  The suite alone, once the simulator is prepared: `TEST_RUNNER_NOMENTRA_SITE_CAPTURES=1 xcodebuild test-without-building -project Nomentra.xcodeproj -scheme Nomentra -destination 'platform=iOS Simulator,id=<udid>' -parallel-testing-enabled NO -collect-test-diagnostics never -only-testing:NomentraTests/SiteStoreCaptureTests` (store screenshots also need `Scripts/site-captures/host-screenshots.sh` running). Then here: `python3 tools/update-captures.py --og`, and check every alt text's figures against the new images.
- **Homepage copy**: the owner’s final App Store description of 14 October 2026 (tagline, lead, Collect the world, Relive every trip, Know where you stand, Private, on your phone, its not-advice paragraph and Plans). The homepage footer carries that not-advice paragraph; the other pages' footers carry the app's sentence (`AppCopy` `notAdvice`). Coming soon to the App Store, with a placeholder badge linking to `#`, and Requires iOS 26 or later. The band's six short lines are the store screenshot captions.
- **Privacy Policy**: written from the app source on `main` at `f0210f43` (1 October 2026), approved wording in `docs/PRD_wording.md`, Feature PRD 13 and WEB-01/02 in `docs/plan/settings-release-simplification.md`. Re-check it whenever the app's data practices change, and change the “Last updated” date. Last revised for launch on 14 October 2026.
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
