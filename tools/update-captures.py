#!/usr/bin/env python3
"""Homepage app images (and the sharing image) for nomentra.app.

    python3 tools/update-captures.py          # app images from captures/, placeholders where missing
    python3 tools/update-captures.py --og     # also redraw assets/og.png from tools/og.html

Slots: take each from the next build as a portrait iPhone PNG, light appearance,
and save it under captures/ with exactly this name:

    captures/home-ribbon.png     -> assets/app-home-ribbon.webp     Home with the ribbon hero and trackers
    captures/tracker-detail.png  -> assets/app-tracker-detail.webp  a tracker's detail page
    captures/calendar-month.png  -> assets/app-calendar-month.webp  the calendar month with flags
    captures/country-page.png    -> assets/app-country-page.webp    a country page with photos

Each capture is fitted to 786 x 1704 px (the page's phone size; any portrait
iPhone size works, the few extra rows are trimmed evenly) and saved as WebP.
A slot without a capture gets a placeholder, the Warm stone canvas (#E3DFD8,
phaseBCanvas) with the nomentra wordmark (SF Pro regular, #0B172A phaseBInk),
so the page never shows a broken image. After adding a real capture, change
that image's alt text in index.html from "Nomentra" to a description of what
the capture shows.

Needs Pillow with WebP support (python3 -m pip install --user Pillow).
--og also needs Google Chrome (or NOMENTRA_CHROME pointing at a Chrome binary).
"""
import argparse
import os
import shutil
import signal
import subprocess
import sys
import tempfile
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SLOTS = ['home-ribbon', 'tracker-detail', 'calendar-month', 'country-page']
SIZE = (786, 1704)
CANVAS, INK = '#E3DFD8', '#0B172A'
WORDMARK_FONT = '/System/Library/Fonts/SFNS.ttf'
CHROME = os.environ.get('NOMENTRA_CHROME', '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome')


def pillow():
    try:
        from PIL import Image, ImageDraw, ImageFont, features
    except ImportError:
        sys.exit('Pillow is missing: python3 -m pip install --user Pillow')
    if not features.check('webp'):
        sys.exit('This Pillow has no WebP support')
    return Image, ImageDraw, ImageFont


def fitted(Image, path):
    image = Image.open(path).convert('RGB')
    width, height = image.size
    if width >= height:
        sys.exit(f'{path.name} is not a portrait capture ({width} x {height})')
    scale = max(SIZE[0] / width, SIZE[1] / height)
    resized = image.resize((round(width * scale), round(height * scale)), Image.LANCZOS)
    left = (resized.width - SIZE[0]) // 2
    top = (resized.height - SIZE[1]) // 2
    return resized.crop((left, top, left + SIZE[0], top + SIZE[1]))


def placeholder(Image, ImageDraw, ImageFont):
    image = Image.new('RGB', SIZE, CANVAS)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(WORDMARK_FONT, 88)
    try:
        font.set_variation_by_name('Regular')
    except (OSError, ValueError):
        pass
    left, top, right, bottom = draw.textbbox((0, 0), 'nomentra', font=font)
    draw.text(((SIZE[0] - (right - left)) / 2 - left, (SIZE[1] - (bottom - top)) / 2 - top),
              'nomentra', font=font, fill=INK)
    return image


def render_og():
    """Draw tools/og.html at 1200 x 630 with headless Chrome. Chrome can stay
    alive after writing the file, so the run ends once the file is reported."""
    if not Path(CHROME).exists():
        sys.exit(f'Google Chrome not found at {CHROME}; set NOMENTRA_CHROME')
    work = Path(tempfile.mkdtemp(prefix='nomentra-og-'))
    shot, log = work / 'og.png', work / 'chrome.log'
    command = [CHROME, '--headless=new', '--disable-gpu', '--hide-scrollbars', '--force-color-profile=srgb',
               '--force-device-scale-factor=1', '--window-size=1200,630', f'--user-data-dir={work / "profile"}',
               '--no-first-run', '--no-default-browser-check', '--use-mock-keychain', '--password-store=basic',
               '--disable-extensions', '--disable-sync', '--disable-background-networking',
               '--disable-component-update', '--allow-file-access-from-files', '--virtual-time-budget=3000',
               f'--screenshot={shot}', (ROOT / 'tools' / 'og.html').as_uri()]
    try:
        with open(log, 'wb') as stream:
            process = subprocess.Popen(command, stdout=stream, stderr=subprocess.STDOUT, start_new_session=True)
            deadline = time.time() + 90
            while time.time() < deadline:
                if process.poll() is not None or b'bytes written to file' in log.read_bytes():
                    break
                time.sleep(0.2)
            if process.poll() is None:
                os.killpg(process.pid, signal.SIGTERM)
                process.wait(timeout=10)
        if not shot.exists():
            sys.exit('Chrome did not draw og.png:\n' + log.read_text(errors='replace')[-2000:])
        shutil.move(str(shot), ROOT / 'assets' / 'og.png')
        print('wrote assets/og.png')
    finally:
        shutil.rmtree(work, ignore_errors=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--og', action='store_true', help='also redraw assets/og.png from tools/og.html')
    args = parser.parse_args()
    Image, ImageDraw, ImageFont = pillow()
    for slot in SLOTS:
        source = ROOT / 'captures' / f'{slot}.png'
        target = ROOT / 'assets' / f'app-{slot}.webp'
        if source.exists():
            fitted(Image, source).save(target, 'WEBP', quality=85, method=6)
            print(f'wrote {target.relative_to(ROOT)} from {source.relative_to(ROOT)}; update its alt text in index.html')
        else:
            placeholder(Image, ImageDraw, ImageFont).save(target, 'WEBP', quality=85, method=6)
            print(f'wrote {target.relative_to(ROOT)} as a placeholder (no {source.relative_to(ROOT)})')
    if args.og:
        render_og()


if __name__ == '__main__':
    main()
