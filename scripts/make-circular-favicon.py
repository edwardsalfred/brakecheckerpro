"""Create a circular-masked favicon from the square logo PNG.

The source logo has a white square background outside its circular badge.
Browsers don't apply CSS border-radius to favicons, so we have to bake the
circular shape into the alpha channel.

Outputs:
  site/assets/favicon.png       (256x256, used for og:image and apple-touch)
  site/assets/favicon-32.png    (32x32, primary favicon)

Run from the project root:
    python scripts/make-circular-favicon.py
"""
from PIL import Image, ImageDraw
import os

SRC = "site/assets/brakecheckerprofinalv4.png"
OUT_LARGE = "site/assets/favicon.png"
OUT_SMALL = "site/assets/favicon-32.png"


def circular_crop(img: Image.Image) -> Image.Image:
    img = img.convert("RGBA")
    w, h = img.size
    mask = Image.new("L", (w, h), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, w - 1, h - 1), fill=255)
    out = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    out.paste(img, (0, 0), mask)
    return out


def main():
    if not os.path.exists(SRC):
        raise SystemExit(f"Source not found: {SRC}")
    src = Image.open(SRC)
    masked = circular_crop(src)
    masked.resize((256, 256), Image.LANCZOS).save(OUT_LARGE, "PNG", optimize=True)
    masked.resize((32, 32), Image.LANCZOS).save(OUT_SMALL, "PNG", optimize=True)
    print(f"Wrote {OUT_LARGE} ({os.path.getsize(OUT_LARGE)} bytes)")
    print(f"Wrote {OUT_SMALL} ({os.path.getsize(OUT_SMALL)} bytes)")


if __name__ == "__main__":
    main()
