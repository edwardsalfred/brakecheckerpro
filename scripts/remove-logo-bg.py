"""Flood-fill the white background of the logo PNG from each corner,
preserving the interior white of the circular badge.

Run from the project root:
    python scripts/remove-logo-bg.py
"""
from PIL import Image, ImageDraw
from collections import deque
import os

SRC = "site/assets/logo-nav.png"
DST = "site/assets/logo-nav.png"  # overwrite in place

# Pixels within this distance of pure white get flood-filled when reached
# from the image edge. Higher catches anti-aliased halos but risks eating
# into light areas of the design. 50 is the sweet spot for this badge:
# pure white (255,255,255) down to near-mid gray (205,205,205) is removed,
# but the badge's interior whites are protected because they are enclosed
# by the black ring and unreachable from the outside.
WHITE_TOLERANCE = 50

def is_whiteish(px):
    r, g, b = px[0], px[1], px[2]
    a = px[3] if len(px) > 3 else 255
    if a == 0:
        return False  # already transparent
    return (
        r >= 255 - WHITE_TOLERANCE
        and g >= 255 - WHITE_TOLERANCE
        and b >= 255 - WHITE_TOLERANCE
    )


def flood_fill_corners(img):
    img = img.convert("RGBA")
    w, h = img.size
    px = img.load()

    visited = [[False] * h for _ in range(w)]
    queue = deque()

    # Seed from every whiteish pixel along the four edges, not just the corners.
    # This catches anti-aliased halos that break corner-to-corner connectivity.
    for x in range(w):
        for y in (0, h - 1):
            if is_whiteish(px[x, y]) and not visited[x][y]:
                queue.append((x, y))
                visited[x][y] = True
    for y in range(h):
        for x in (0, w - 1):
            if is_whiteish(px[x, y]) and not visited[x][y]:
                queue.append((x, y))
                visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        # Mark transparent
        px[x, y] = (0, 0, 0, 0)
        # 4-connected neighbors
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < w and 0 <= ny < h and not visited[nx][ny]:
                if is_whiteish(px[nx, ny]):
                    visited[nx][ny] = True
                    queue.append((nx, ny))

    return img


def main():
    if not os.path.exists(SRC):
        raise SystemExit(f"Source not found: {SRC}")
    img = Image.open(SRC)
    out = flood_fill_corners(img)
    out.save(DST, "PNG", optimize=True)
    print(f"Wrote {DST} ({os.path.getsize(DST)} bytes)")


if __name__ == "__main__":
    main()
