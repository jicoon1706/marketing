"""
IGEN VERITAS brand constants for social visual generation.
Import this in any visual generation script.
"""
from PIL import ImageFont
import os

# ── Canvas ──────────────────────────────────────────────────────────────────
CANVAS_SIZE = (1080, 1080)
OUTPUT_DIR  = os.path.join(
    os.path.dirname(__file__), "..", "..", "..", "..", "social-media"
)

# ── Brand Colors (RGBA tuples) ───────────────────────────────────────────────
VIOLET       = (123, 103, 209, 255)   # #7B67D1
PURPLE       = (138,  93, 204, 255)   # #8A5DCC
BLUE_MID     = ( 72, 143, 227, 255)   # #488FE3
BLUE_BRIGHT  = ( 65, 150, 230, 255)   # #4196E6
DARK_NAVY    = ( 11,  11,  20, 255)   # #0B0B14
WHITE        = (255, 255, 255, 255)
BODY_GRAY    = (107, 114, 128, 255)   # #6B7280
GLASS_FILL   = (255, 255, 255,  13)   # ~5% white
GLASS_BORDER = (255, 255, 255,  26)   # ~10% white

# Gradient definitions (start_color, end_color)
HERO_GRADIENT = (VIOLET, BLUE_BRIGHT)
DARK_GRADIENT = (DARK_NAVY, (30, 15, 50, 255))

# ── Typography ───────────────────────────────────────────────────────────────
_WIN_FONTS = {
    "bold":       "C:/Windows/Fonts/segoeuib.ttf",
    "semibold":   "C:/Windows/Fonts/segoeuiz.ttf",
    "regular":    "C:/Windows/Fonts/segoeui.ttf",
    "light":      "C:/Windows/Fonts/segoeuil.ttf",
    "italic":     "C:/Windows/Fonts/segoeuii.ttf",
}

_SKILL_DIR = os.path.dirname(os.path.dirname(__file__))
_ASSET_FONTS = os.path.join(_SKILL_DIR, "assets", "fonts")

_CUSTOM_FONTS = {
    "bold":    os.path.join(_ASSET_FONTS, "Inter-Bold.ttf"),
    "regular": os.path.join(_ASSET_FONTS, "Inter-Regular.ttf"),
}


def get_font(size: int, weight: str = "regular") -> ImageFont.FreeTypeFont:
    """Return an ImageFont, preferring cached Inter, then Segoe UI, then default."""
    custom = _CUSTOM_FONTS.get(weight)
    if custom and os.path.exists(custom):
        return ImageFont.truetype(custom, size)
    win = _WIN_FONTS.get(weight, _WIN_FONTS["regular"])
    if os.path.exists(win):
        return ImageFont.truetype(win, size)
    return ImageFont.load_default()


# ── Gradient helper ───────────────────────────────────────────────────────────
def draw_gradient(draw, width: int, height: int,
                  start: tuple, end: tuple, direction: str = "vertical"):
    """Fill canvas with a linear gradient. direction: 'vertical' or 'diagonal'."""
    for i in range(height if direction == "vertical" else width + height):
        t = i / (height - 1 if direction == "vertical" else width + height - 1)
        t = max(0.0, min(1.0, t))
        r = int(start[0] + (end[0] - start[0]) * t)
        g = int(start[1] + (end[1] - start[1]) * t)
        b = int(start[2] + (end[2] - start[2]) * t)
        a = int(start[3] + (end[3] - start[3]) * t)
        if direction == "vertical":
            draw.line([(0, i), (width, i)], fill=(r, g, b, a))
        else:
            draw.line([(0, i), (i, 0)], fill=(r, g, b, a))


# ── Glass card helper ─────────────────────────────────────────────────────────
def draw_glass_card(draw, box: tuple, radius: int = 24,
                    fill=GLASS_FILL, outline=GLASS_BORDER, outline_width: int = 1):
    """Draw a glassmorphism-style rounded rectangle."""
    draw.rounded_rectangle(box, radius=radius, fill=fill,
                            outline=outline, width=outline_width)


# ── Centered text helper ──────────────────────────────────────────────────────
def draw_centered_text(draw, cx: int, y: int, text: str, font,
                       fill=WHITE, anchor: str = "mt"):
    """Draw text centered at (cx, y)."""
    draw.text((cx, y), text, font=font, fill=fill, anchor=anchor)
