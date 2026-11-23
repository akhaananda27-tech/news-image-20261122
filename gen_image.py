#!/usr/bin/env python3
"""news-image-20261122 — one-page front page summing up Sunday 22 November 2026.
Draws entry.png (1024x1024) with PIL only. No network, no clock, no randomness."""
import math
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
F = "/usr/share/fonts/truetype/dejavu/"

CREAM = (245, 239, 223)
PAPER = (250, 246, 233)
INK = (26, 26, 26)
RED = (178, 34, 34)
DARKRED = (140, 20, 20)
GREY = (90, 88, 80)
LIGHT = (232, 226, 210)
SEA = (186, 214, 224)
LAND = (238, 226, 196)
TAN = (222, 205, 165)

REGIONS = {
    "Middle East": ((178, 34, 34), 7),
    "Europe": ((43, 94, 167), 13),
    "East Asia": ((15, 118, 110), 3),
    "South Asia": ((123, 79, 166), 2),
    "South-East Asia": ((146, 110, 30), 3),
    "Africa": ((217, 123, 41), 4),
    "Americas": ((46, 125, 50), 3),
}
REGION_ORDER = ["Middle East", "Europe", "East Asia", "South Asia",
                "South-East Asia", "Africa", "Americas"]

def font(name, size):
    return ImageFont.truetype(os.path.join(F, name), size)

SERIF_B = lambda s: font("DejaVuSerif-Bold.ttf", s)
SERIF = lambda s: font("DejaVuSerif.ttf", s)
SERIF_I = lambda s: font("DejaVuSerif-Italic.ttf", s) if os.path.exists(os.path.join(F, "DejaVuSerif-Italic.ttf")) else font("DejaVuSerif.ttf", s)
SANS = lambda s: font("DejaVuSans.ttf", s)
SANS_B = lambda s: font("DejaVuSans-Bold.ttf", s)

def tw(draw, text, f):
    b = draw.textbbox((0, 0), text, font=f)
    return b[2] - b[0]

def wrap(draw, text, f, maxw):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if tw(draw, t, f) <= maxw:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def center(draw, x, y, w, text, f, fill=INK):
    draw.text((x + (w - tw(draw, text, f)) / 2, y), text, font=f, fill=fill)

def badge(draw, x, y, text, fill=(34, 120, 60)):
    f = SANS_B(9)
    w = tw(draw, text, f) + 12
    draw.rounded_rectangle([x, y, x + w, y + 13], radius=3, fill=fill)
    draw.text((x + 6, y + 2), text, font=f, fill=(255, 255, 255))
    return w

def hline(draw, x, y, w, fill=INK, width=1):
    draw.line([(x, y), (x + w, y)], fill=fill, width=width)

W = H = 1024
img = Image.new("RGB", (W, H), CREAM)
d = ImageDraw.Draw(img)
M = 12
CW = W - 2 * M

# ---- top strip ----
f_top = SANS_B(9)
d.text((M, 4), "THE WORLD IN ONE DAY", font=f_top, fill=INK)
center(d, M, 4, CW, "DAY 326 OF 2026", f_top, RED)
rt = "ALL TIMES UTC \u00b7 RANKED BY CONSEQUENCE"
d.text((W - M - tw(d, rt, f_top), 4), rt, font=f_top, fill=INK)
hline(d, M, 17, CW, INK, 2)

# ---- masthead ----
y = 20
f_mast = SERIF_B(60)
center(d, M, y, CW, "Sunday 22 November 2026", f_mast, INK)
y += 64
hline(d, M, y, CW, INK, 2)
y += 4
f_sub = SANS_B(11)
center(d, M, y, CW, "35 STORIES, 7 REGIONS, EVERY ONE DATED SUNDAY 22 NOVEMBER 2026", f_sub, RED)
y += 16
hline(d, M, y, CW, INK, 1)
y += 4
f_tick = SERIF_I(13)
tick = "COP31 collapses with no deal  \u25c6  Iran strikes US bases in Bahrain  \u25c6  El Chapo Isidro captured in Sinaloa"
center(d, M, y, CW, tick, f_tick, INK)
y += 17
hline(d, M, y, CW, INK, 2)

# ---- THE DAY IN UTC strip ----
y += 5
strip_y = y
utc_items = [
    ("Morning", "COP31 talks collapse\nin Antalya"),
    ("Morning", "Iran strikes US bases\nin Bahrain"),
    ("Midday", "El Chapo Isidro\ncaptured, Sinaloa"),
    ("Afternoon", "S&P 500 falls into\ncorrection, New York"),
    ("Evening", "World Court: Myanmar\ncommitted genocide"),
    ("Evening", "M\u00e1rquez takes an\n8th MotoGP title"),
]
lab_w = 92
cell_w = (CW - lab_w) / 6
d.rectangle([M, strip_y, M + lab_w, strip_y + 32], fill=INK)
d.text((M + 6, strip_y + 3), "THE DAY", font=SANS_B(10), fill=(255, 255, 255))
d.text((M + 6, strip_y + 15), "IN UTC", font=SANS_B(10), fill=(255, 255, 255))
f_ut = SANS_B(10)
f_ut2 = SANS(8)
for i, (t, txt) in enumerate(utc_items):
    cx = M + lab_w + i * cell_w
    d.rectangle([cx, strip_y, cx + cell_w - 1, strip_y + 32], outline=GREY, width=1)
    d.text((cx + 5, strip_y + 2), t, font=f_ut, fill=RED)
    ly = strip_y + 14
    for ln in txt.split("\n"):
        d.text((cx + 5, ly), ln, font=f_ut2, fill=INK)
        ly += 9
y = strip_y + 34

# ---- THE DAY IN NUMBERS ----
num_y = y
d.rectangle([M, num_y, M + lab_w, num_y + 44], fill=RED)
d.text((M + 6, num_y + 4), "THE DAY", font=SANS_B(10), fill=(255, 255, 255))
d.text((M + 6, num_y + 16), "IN NUMBERS", font=SANS_B(10), fill=(255, 255, 255))
d.text((M + 6, num_y + 28), "AS REPORTED", font=SANS(7), fill=(255, 220, 220))
nums = [
    ("-3.7%", "S&P 500 on Friday;\nNasdaq -5.3%"),
    ("11", "killed in Sinaloa raid,\n4 of them soldiers"),
    ("24", "dead as a boat capsizes\nin Nigeria"),
    ("36", "missing after a factory\nfire in Cikande"),
    ("98.5%", "of goods tariff-free\nin EU\u2013Indonesia deal"),
    ("2", "injured as Iran hits\nUS bases in Bahrain"),
]
cell_w = (CW - lab_w) / 6
f_num = SANS_B(21)
f_num2 = SANS(8)
for i, (n, txt) in enumerate(nums):
    cx = M + lab_w + i * cell_w
    d.rectangle([cx, num_y, cx + cell_w - 1, num_y + 44], outline=GREY, width=1)
    d.text((cx + 5, num_y + 2), n, font=f_num, fill=RED)
    ly = num_y + 24
    for ln in txt.split("\n"):
        d.text((cx + 5, ly), ln, font=f_num2, fill=INK)
        ly += 9
y = num_y + 46

# ---- region bar ----
bar_y = y
x = M
f_reg = SANS_B(8)
for name in REGION_ORDER:
    col, n = REGIONS[name]
    wseg = CW * n / 35.0
    d.rectangle([x, bar_y, x + wseg - 1, bar_y + 14], fill=col)
    lab = f"{name} {n}"
    if tw(d, lab, f_reg) <= wseg - 4:
        d.text((x + 3, bar_y + 3), lab, font=f_reg, fill=(255, 255, 255))
    else:
        num = str(n)
        d.text((x + (wseg - tw(d, num, f_reg)) / 2, bar_y + 3), num, font=f_reg, fill=(255, 255, 255))
    x += wseg
y = bar_y + 16

# ================= FEATURES =================
feat_y = y
feat_w = (CW - 2 * 10) / 3
feat_h = 206

def feature_panel_cop31(x, yy, w, h):
    d.rectangle([x, yy, x + w, yy + h], fill=(232, 240, 232), outline=INK, width=1)
    d.text((x + 8, yy + 5), "COP31", font=SANS_B(24), fill=(16, 90, 60))
    d.text((x + 8, yy + 32), "ANTALYA \u00b7 UN CLIMATE SUMMIT", font=SANS_B(8), fill=GREY)
    cx = x + 8
    cy = yy + 44
    for day in range(10, 23):
        cw = 21
        fill = RED if day == 22 else (255, 255, 255)
        d.rectangle([cx, cy, cx + cw - 2, cy + 18], fill=fill, outline=GREY)
        d.text((cx + 6, cy + 3), str(day), font=SANS_B(9), fill=(255, 255, 255) if day == 22 else INK)
        cx += cw
    d.text((x + 8, cy + 21), "DAY 13 OF A 12-DAY SUMMIT \u00b7 TALKS END WITH NO DEAL", font=SANS_B(8), fill=DARKRED)
    d.rectangle([x + 8, yy + h - 15, x + w - 8, yy + h - 2], fill=(255, 255, 255), outline=GREY)
    d.text((x + 12, yy + h - 13), "DRAFT: \u201cfossil fuels\u201d", font=SERIF_I(9), fill=GREY)
    d.line([(x + 12, yy + h - 5), (x + 118, yy + h - 5)], fill=RED, width=2)
    d.text((x + 130, yy + h - 13), "NO MENTION", font=SANS_B(9), fill=RED)

def feature_panel_bahrain(x, yy, w, h):
    d.rectangle([x, yy, x + w, yy + h], fill=SEA, outline=INK, width=1)
    # Iran land across the top
    d.polygon([(x + 10, yy + 8), (x + w - 10, yy + 8), (x + w - 10, yy + 26), (x + 10, yy + 26)], fill=LAND)
    d.text((x + 14, yy + 11), "IRAN", font=SANS_B(10), fill=INK)
    # Saudi land at the bottom left, Qatar peninsula right
    d.polygon([(x + 10, yy + h - 8), (x + w * 0.55, yy + h - 8), (x + w * 0.5, yy + h - 30), (x + 10, yy + h - 30)], fill=LAND)
    d.polygon([(x + w * 0.68, yy + h - 8), (x + w - 10, yy + h - 8), (x + w - 10, yy + h - 34), (x + w * 0.66, yy + h - 34)], fill=LAND)
    d.text((x + 14, yy + h - 24), "SAUDI ARABIA", font=SANS_B(8), fill=INK)
    d.text((x + w - 58, yy + h - 24), "QATAR", font=SANS_B(8), fill=INK)
    # Bahrain island in the gulf
    bx, by = x + int(w * 0.44), yy + 52
    d.ellipse([bx - 7, by - 5, bx + 7, by + 5], fill=RED, outline=(255, 255, 255), width=2)
    d.text((bx + 10, by - 7), "BAHRAIN", font=SANS_B(10), fill=INK)
    # missile arcs from Iran down to Bahrain
    for sx0 in [x + 60, x + 110, x + 170]:
        for k in range(7):
            fx0 = sx0 + (bx - sx0) * k / 7
            fy0 = (yy + 26) + (by - (yy + 26)) * k / 7 - 8 * math.sin(math.pi * k / 7)
            fx1 = sx0 + (bx - sx0) * (k + 0.6) / 7
            fy1 = (yy + 26) + (by - (yy + 26)) * (k + 0.6) / 7 - 8 * math.sin(math.pi * (k + 0.6) / 7)
            d.line([(fx0, fy0), (fx1, fy1)], fill=RED, width=2)
    d.text((x + 8, yy + 62), "US BASES HIT BY MISSILES AND DRONES", font=SANS_B(7), fill=DARKRED)
    d.rectangle([x + w - 92, yy + 6, x + w - 6, yy + 26], fill=RED)
    d.text((x + w - 86, yy + 10), "2 INJURED", font=SANS_B(12), fill=(255, 255, 255))

def feature_panel_markets(x, yy, w, h):
    d.rectangle([x, yy, x + w, yy + h], fill=(245, 238, 220), outline=INK, width=1)
    d.text((x + 8, yy + 5), "MARKETS", font=SANS_B(24), fill=DARKRED)
    d.text((x + 8, yy + 32), "NEW YORK \u00b7 STOCKS FALL INTO CORRECTION", font=SANS_B(8), fill=GREY)
    # falling chart
    cx0, cy0, cw, ch = x + 14, yy + 48, w - 28, 34
    d.rectangle([cx0, cy0, cx0 + cw, cy0 + ch], fill=(255, 255, 255), outline=GREY)
    pts = [(cx0 + 4 + i * (cw - 8) / 9, cy0 + 4 + (ch - 8) * (i / 9) ** 1.4 + (2 if i % 3 else -2)) for i in range(10)]
    d.line(pts, fill=RED, width=3)
    d.ellipse([pts[-1][0] - 3, pts[-1][1] - 3, pts[-1][0] + 3, pts[-1][1] + 3], fill=RED)
    d.text((cx0 + 4, cy0 + ch - 12), "FRI", font=SANS_B(7), fill=GREY)
    d.text((cx0 + cw - 22, cy0 + 2), "LOW", font=SANS_B(7), fill=RED)
    d.text((x + 8, cy0 + ch + 4), "S&P 500 \u22123.7% \u00b7 NASDAQ \u22125.3% \u00b7 AI SELL-OFF HITS ASIA", font=SANS_B(8), fill=INK)
    d.rectangle([x + w - 100, yy + 6, x + w - 6, yy + 26], fill=RED)
    d.text((x + w - 94, yy + 10), "CORRECTION", font=SANS_B(12), fill=(255, 255, 255))

FEATURES = [
    ("EUROPE \u00b7 COP31, ANTALYA \u00b7 CLIMATE", "COP31 collapses as talks fail on fossil fuels",
     "Final draft drops every fossil-fuel mention; EU objects; Guterres \u2018deeply disappointed\u2019; no deal at all.",
     "AFP \u00b7 REUTERS", "CONFIRMED", feature_panel_cop31),
    ("MIDDLE EAST \u00b7 BAHRAIN \u00b7 CONFLICT", "Iran strikes US bases in Bahrain",
     "Missiles and drones hit US bases; two people injured. Tehran claims two Patriot radars destroyed.",
     "REUTERS \u00b7 AFP", "CONFIRMED", feature_panel_bahrain),
    ("AMERICAS \u00b7 MARKETS \u00b7 ECONOMY", "US stocks fall into correction as AI sell-off spreads",
     "S&P 500 drops 3.7% on Friday, Nasdaq 5.3%; the rout reaches Japan and Korea.",
     "AP", "CONFIRMED", feature_panel_markets),
]

f_kick = SANS_B(9)
f_head = SERIF_B(19)
f_deck = SERIF(10)
f_src = SANS(8)
for i, (kick, head, deck, src, conf, panel) in enumerate(FEATURES):
    fx = M + i * (feat_w + 10)
    panel(fx, feat_y, feat_w, 92)
    ty = feat_y + 98
    col, _ = REGIONS["Europe" if i == 0 else ("Middle East" if i == 1 else "Americas")]
    d.rectangle([fx, ty, fx + 14, ty + 13], fill=col)
    d.text((fx + 18, ty + 2), str(i + 1), font=SANS_B(10), fill=INK)
    d.text((fx + 32, ty + 2), kick, font=f_kick, fill=INK)
    bw = badge(d, fx + feat_w - 78, ty, conf)
    ty += 16
    for ln in wrap(d, head, f_head, feat_w):
        d.text((fx, ty), ln, font=f_head, fill=INK)
        ty += 21
    ty += 2
    for ln in wrap(d, deck, f_deck, feat_w):
        d.text((fx, ty), ln, font=f_deck, fill=INK)
        ty += 12
    d.text((fx, ty + 2), src, font=f_src, fill=GREY)
y = feat_y + feat_h + 6

# ================= GRID (12 stories, 4-15) =================
grid_y = y
cols = 4
rows = 3
gw = (CW - 3 * 8) / cols
gh = 100

def mini_panel(x, yy, w, h, kind):
    d.rectangle([x, yy, x + w, yy + h], fill=LIGHT, outline=INK, width=1)
    if kind == "raid":
        d.rectangle([x, yy, x + w, yy + h], fill=(30, 40, 55))
        d.rectangle([x + 12, yy + 8, x + 60, yy + 34], fill=(120, 120, 120))
        d.rectangle([x + 66, yy + 8, x + 90, yy + 34], fill=(120, 120, 120))
        d.text((x + 100, yy + 6), "11", font=SANS_B(20), fill=(255, 140, 0))
        d.text((x + 100, yy + 28), "KILLED", font=SANS_B(8), fill=(255, 255, 255))
    elif kind == "missile":
        d.rectangle([x, yy, x + w, yy + h], fill=(225, 228, 235))
        d.rectangle([x + 12, yy + 10, x + 52, yy + 40], fill=(160, 160, 170), outline=INK)
        d.line([(x + 12, yy + 25), (x + 52, yy + 18)], fill=RED, width=2)
        d.text((x + 60, yy + 6), "7", font=SANS_B(20), fill=RED)
        d.text((x + 60, yy + 28), "YEARS OLD", font=SANS_B(8), fill=INK)
    elif kind == "scales":
        d.rectangle([x, yy, x + w, yy + h], fill=(232, 236, 244))
        d.line([(x + 60, yy + 6), (x + 60, yy + 30)], fill=INK, width=2)
        d.line([(x + 20, yy + 12), (x + 100, yy + 12)], fill=INK, width=2)
        d.arc([x + 14, yy + 12, x + 34, yy + 30], 0, 180, fill=INK, width=2)
        d.arc([x + 86, yy + 12, x + 106, yy + 30], 0, 180, fill=INK, width=2)
        d.text((x + 120, yy + 8), "ICJ", font=SANS_B(14), fill=INK)
        d.text((x + 120, yy + 26), "GENOCIDE", font=SANS_B(8), fill=RED)
    elif kind == "handshake":
        d.rectangle([x, yy, x + w, yy + h], fill=(220, 240, 210))
        d.rectangle([x + 10, yy + 8, x + 60, yy + 16], fill=(0, 51, 153))
        d.rectangle([x + 10, yy + 16, x + 60, yy + 24], fill=(255, 255, 255))
        d.rectangle([x + 10, yy + 24, x + 60, yy + 32], fill=(255, 0, 0))
        d.rectangle([x + 70, yy + 8, x + 120, yy + 16], fill=(255, 0, 0))
        d.rectangle([x + 70, yy + 16, x + 120, yy + 24], fill=(255, 255, 255))
        d.text((x + 130, yy + 8), "98.5%", font=SANS_B(14), fill=(20, 90, 40))
        d.text((x + 130, yy + 26), "TARIFF-FREE", font=SANS_B(8), fill=INK)
    elif kind == "factory":
        d.rectangle([x, yy, x + w, yy + h], fill=(240, 228, 210))
        d.rectangle([x + 10, yy + 16, x + 70, yy + 40], fill=(150, 120, 90), outline=INK)
        d.polygon([(x + 10, yy + 16), (x + 25, yy + 4), (x + 40, yy + 16), (x + 55, yy + 4), (x + 70, yy + 16)], fill=(150, 120, 90))
        d.ellipse([x + 78, yy + 8, x + 100, yy + 30], fill=(255, 140, 0))
        d.text((x + 110, yy + 6), "36", font=SANS_B(20), fill=RED)
        d.text((x + 110, yy + 28), "MISSING", font=SANS_B(8), fill=INK)
    elif kind == "boat":
        d.rectangle([x, yy, x + w, yy + h], fill=SEA)
        d.polygon([(x + 60, yy + 18), (x + 140, yy + 18), (x + 120, yy + 32), (x + 80, yy + 32)], fill=(120, 90, 60))
        d.arc([x + 50, yy + 26, x + 90, yy + 42], 0, 180, fill=(255, 255, 255), width=2)
        d.arc([x + 110, yy + 30, x + 150, yy + 46], 0, 180, fill=(255, 255, 255), width=2)
        d.text((x + 160, yy + 8), "24 DEAD", font=SANS_B(11), fill=DARKRED)
    elif kind == "capitol":
        d.rectangle([x, yy, x + w, yy + h], fill=(235, 230, 245))
        d.polygon([(x + 60, yy + 8), (x + 110, yy + 8), (x + 120, yy + 20), (x + 50, yy + 20)], fill=(200, 200, 210))
        d.rectangle([x + 78, yy + 20, x + 92, yy + 38], fill=(200, 200, 210))
        d.text((x + 130, yy + 8), "HOUSE", font=SANS_B(12), fill=INK)
        d.text((x + 130, yy + 24), "FLIPS BIG", font=SANS_B(9), fill=RED)
    elif kind == "moto":
        d.rectangle([x, yy, x + w, yy + h], fill=(220, 240, 210))
        d.text((x + 6, yy + 4), "8th", font=SANS_B(20), fill=(20, 90, 40))
        d.text((x + 6, yy + 27), "TITLE \u00b7 PORTUGAL", font=SANS_B(7), fill=INK)
        d.text((x + 120, yy + 10), "M\u00c1RQUEZ", font=SANS_B(11), fill=INK)
        d.text((x + 120, yy + 26), "PASSES ROSSI", font=SANS_B(8), fill=GREY)
    elif kind == "ship":
        d.rectangle([x, yy, x + w, yy + h], fill=(30, 40, 55))
        d.rectangle([x + 20, yy + 24, x + 150, yy + 34], fill=(120, 120, 120))
        d.rectangle([x + 100, yy + 12, x + 116, yy + 24], fill=(120, 120, 120))
        d.ellipse([x + 60, yy + 2, x + 84, yy + 26], fill=(255, 140, 0))
        d.ellipse([x + 68, yy - 2, x + 80, yy + 10], fill=(255, 60, 0))
        d.text((x + 160, yy + 12), "STILL", font=SANS_B(10), fill=(255, 255, 255))
        d.text((x + 160, yy + 24), "BURNING", font=SANS_B(10), fill=(255, 140, 0))
    elif kind == "poland":
        d.rectangle([x, yy, x + w, yy + h], fill=(225, 228, 235))
        d.rectangle([x + 10, yy + 8, x + 60, yy + 16], fill=(255, 255, 255), outline=INK)
        d.rectangle([x + 10, yy + 16, x + 60, yy + 24], fill=(220, 20, 60), outline=INK)
        d.rectangle([x + 10, yy + 24, x + 60, yy + 32], fill=(255, 255, 255), outline=INK)
        d.text((x + 70, yy + 8), "NATO:", font=SANS_B(12), fill=INK)
        d.text((x + 70, yy + 24), "VIOLATION", font=SANS_B(9), fill=RED)
    elif kind == "taiwan":
        d.rectangle([x, yy, x + w, yy + h], fill=(235, 240, 235))
        d.rectangle([x + 10, yy + 8, x + 60, yy + 16], fill=(255, 0, 0))
        d.rectangle([x + 10, yy + 16, x + 60, yy + 24], fill=(255, 255, 255))
        d.rectangle([x + 10, yy + 24, x + 60, yy + 32], fill=(255, 0, 0))
        d.text((x + 70, yy + 8), "TAIWAN", font=SANS_B(12), fill=INK)
        d.text((x + 70, yy + 24), "TENSIONS", font=SANS_B(9), fill=INK)
    elif kind == "patriot":
        d.rectangle([x, yy, x + w, yy + h], fill=(232, 236, 244))
        d.polygon([(x + 20, yy + 30), (x + 40, yy + 8), (x + 60, yy + 30)], fill=(43, 94, 167))
        d.rectangle([x + 38, yy + 30, x + 42, yy + 38], fill=(43, 94, 167))
        d.text((x + 70, yy + 8), "PATRIOT", font=SANS_B(12), fill=INK)
        d.text((x + 70, yy + 24), "WHERE ARE THEY?", font=SANS_B(9), fill=RED)

GRID = [
    (4, "AMERICAS", "CONFIRMED", (46, 125, 50), "Cartel boss \u2018El Chapo Isidro\u2019 captured in Sinaloa raid",
     "Special forces raid kills 11, including four soldiers.", "AP \u00b7 AL JAZEERA", "raid"),
    (5, "EUROPE", "CONFIRMED", (178, 34, 34), "Russian missile hits Zelenskyy\u2019s hometown Kryvyi Rih",
     "A boy, 7, and a woman, 20, are killed; 60 wounded.", "AP \u00b7 CNN", "missile"),
    (6, "SOUTH-EAST ASIA", "OFFICIAL", (20, 120, 60), "World Court: Myanmar committed genocide against the Rohingya",
     "First time the court finds a state responsible for genocide.", "AP \u00b7 REUTERS", "scales"),
    (7, "SOUTH-EAST ASIA", "OFFICIAL", (146, 110, 30), "EU and Indonesia sign landmark trade deal",
     "After almost 10 years of talks; tariffs scrapped on up to 98.5% of goods.", "EU \u00b7 AP", "handshake"),
    (8, "SOUTH-EAST ASIA", "CONFIRMED", (20, 120, 60), "Fire at Indonesian candy factory kills 3; 36 missing",
     "Rescuers search the ruins in Cikande, near Jakarta.", "AP \u00b7 REUTERS", "factory"),
    (9, "AFRICA", "OFFICIAL", (20, 120, 60), "Boat capsizes in Nigeria, at least 24 dead",
     "The boat was carrying people to a funeral.", "AP", "boat"),
    (10, "AMERICAS", "REPORTED", (178, 34, 34), "US Democrats secure biggest House majority in decades",
     "Midterms deliver a historic Democratic majority.", "EURONEWS", "capitol"),
    (11, "EUROPE", "OFFICIAL", (20, 90, 40), "M\u00e1rquez wins an eighth MotoGP title in Portugal",
     "Surpasses Rossi\u2019s record with the win.", "EURONEWS", "moto"),
    (12, "EUROPE", "REPORTED", (178, 34, 34), "Russian cargo ship still on fire after Baltic attack",
     "Finland confirms Russia is towing the drone-hit ship.", "EURONEWS \u00b7 YLE", "ship"),
    (13, "EUROPE", "OFFICIAL", (43, 94, 167), "Russian missiles land in Poland during NATO drills",
     "NATO calls the landing a violation.", "AP", "poland"),
    (14, "EAST ASIA", "REPORTED", (178, 34, 34), "China\u2013Japan relations sour over Taiwan and minerals",
     "Beijing and Tokyo trade warnings as ties deteriorate.", "REUTERS", "taiwan"),
    (15, "EUROPE", "OFFICIAL", (43, 94, 167), "Zelenskyy presses US to release paid-for Patriot missiles",
     "Kyiv says deliveries are delayed as Russian strikes continue.", "REUTERS", "patriot"),
]

f_gtag = SANS_B(8)
f_ghead = SERIF_B(11)
f_gsum = SANS(8)
f_gsrc = SANS(7)
for idx, (num, region, conf, confcol, head, summ, src, kind) in enumerate(GRID):
    r, c = divmod(idx, cols)
    gx = M + c * (gw + 8)
    gy = grid_y + r * (gh + 6)
    mini_panel(gx, gy, gw, 40, kind)
    ty = gy + 44
    d.text((gx, ty), str(num), font=SANS_B(10), fill=RED)
    d.text((gx + 18, ty + 1), region, font=f_gtag, fill=INK)
    bw = badge(d, gx + gw - 66, ty, conf, confcol)
    ty += 13
    lines = wrap(d, head, f_ghead, gw)
    for ln in lines[:2]:
        d.text((gx, ty), ln, font=f_ghead, fill=INK)
        ty += 13
    lines2 = wrap(d, summ, f_gsum, gw)
    for ln in lines2[:1]:
        d.text((gx, ty), ln, font=f_gsum, fill=GREY)
        ty += 10
    d.text((gx, ty), src, font=f_gsrc, fill=GREY)
y = grid_y + rows * (gh + 6) + 2

# ================= BOTTOM: map + also-on =================
bot_y = y
map_w = 340
map_h = 178
also_x = M + map_w + 10
also_w = CW - map_w - 10

d.rectangle([M, bot_y, M + map_w, bot_y + map_h], fill=PAPER, outline=INK, width=1)
d.text((M + 6, bot_y + 3), "WHERE IT HAPPENED", font=SANS_B(10), fill=INK)
d.text((M + 6, bot_y + 15), "pin numbers match the stories; pin colour = the region", font=SANS(7), fill=GREY)
mx0, my0, mw, mh = M + 4, bot_y + 26, map_w - 8, map_h - 44
d.rectangle([mx0, my0, mx0 + mw, my0 + mh], fill=SEA)
CONTINENTS = {
    "NA": [(-168,66),(-140,70),(-125,72),(-110,73),(-95,80),(-85,70),(-75,62),(-60,55),(-55,47),(-70,42),(-75,35),(-80,26),(-90,21),(-97,16),(-105,20),(-115,28),(-125,40),(-125,48),(-140,60),(-165,60)],
    "GL": [(-58,64),(-45,60),(-30,68),(-20,70),(-35,76),(-55,76),(-60,70)],
    "SA": [(-80,10),(-75,5),(-60,0),(-50,-5),(-35,-8),(-40,-20),(-48,-28),(-58,-35),(-65,-45),(-70,-52),(-73,-40),(-75,-25),(-80,-15),(-80,-5)],
    "AF": [(-17,15),(-10,30),(0,35),(10,37),(20,32),(32,31),(35,28),(40,15),(48,11),(51,10),(44,0),(40,-10),(35,-20),(30,-30),(20,-35),(15,-30),(12,-18),(9,-5),(9,4),(-8,5),(-15,10)],
    "EU": [(-10,36),(-9,43),(-2,48),(-5,50),(0,51),(5,53),(8,57),(10,59),(18,56),(21,55),(24,59),(28,60),(30,62),(25,65),(20,70),(15,70),(10,62),(5,58),(0,55),(-2,50),(-5,48),(-8,43),(-10,38)],
    "AS": [(30,62),(40,68),(55,68),(70,72),(90,75),(110,76),(130,72),(150,70),(170,66),(178,65),(170,60),(160,55),(150,45),(142,40),(140,35),(130,33),(127,30),(122,25),(120,22),(110,20),(108,10),(105,5),(100,8),(98,15),(95,20),(92,22),(88,22),(85,20),(80,15),(76,10),(73,20),(70,25),(66,25),(60,25),(56,26),(52,28),(50,30),(48,30),(44,29),(40,32),(36,36),(30,36),(28,42),(30,45),(30,50),(30,55),(30,60)],
    "AU": [(113,-22),(114,-30),(115,-35),(120,-34),(129,-32),(132,-32),(136,-35),(140,-38),(145,-38),(150,-37),(153,-32),(150,-25),(146,-19),(142,-11),(140,-15),(136,-12),(132,-11),(126,-14),(122,-17),(118,-20)],
}
def ll(lon, lat):
    return (mx0 + (lon + 180) / 360 * mw, my0 + (90 - lat) / 180 * mh)
for poly in CONTINENTS.values():
    d.polygon([ll(lon, lat) for lon, lat in poly], fill=LAND, outline=GREY)
PINS = {
    1: (30.7, 36.9, "Europe"), 2: (50.5, 26.2, "Middle East"), 3: (-74.0, 40.7, "Americas"),
    4: (-107.0, 24.8, "Americas"), 5: (33.4, 47.9, "Europe"), 6: (96.1, 21.9, "South-East Asia"),
    7: (106.8, -6.2, "South-East Asia"), 8: (106.1, -6.3, "South-East Asia"), 9: (6.5, 9.5, "Africa"),
    10: (-77.0, 38.9, "Americas"), 11: (-8.5, 37.1, "Europe"), 12: (25.0, 59.8, "Europe"),
    13: (23.0, 52.0, "Europe"), 14: (139.7, 35.7, "East Asia"), 15: (30.5, 50.4, "Europe"),
}
f_pin = SANS_B(7)
for num, (lon, lat, reg) in PINS.items():
    px, py = ll(lon, lat)
    col, _ = REGIONS[reg]
    d.ellipse([px - 6, py - 6, px + 6, py + 6], fill=col, outline=(255, 255, 255), width=1)
    d.text((px - 3, py - 5), str(num), font=f_pin, fill=(255, 255, 255))
d.text((M + 6, bot_y + map_h - 14), "Pins carry each story's number; colour = region.", font=SANS(7), fill=GREY)

ALSO = [
    (16, "Iran hits three tankers near the Strait of Hormuz; two catch fire."),
    (17, "Settler attacks torch West Bank villages; Israel's opposition calls it 'terrorism'."),
    (18, "Saudi Arabia and Yemen's Houthis exchange fire across the border."),
    (19, "Lebanon's army seizes 264 kg of explosives from alleged traffickers."),
    (20, "Iran unveils an underground 'missile city' and starts rationing power."),
    (21, "Lewis Pugh swims the Strait of Hormuz as tankers burn nearby."),
    (22, "Denmark expels a Russian official over an alleged assassination plot."),
    (23, "Poland says Russia twice tried to kill a Ukrainian-American rapper."),
    (24, "Phumzile Mlambo-Ngcuka, ex-South Africa deputy president, dies at 71."),
    (25, "Paolo Bulgari, who built the family brand into a global name, dies at 89."),
    (26, "Germany tests kamikaze drones and AI targeting in Lithuania."),
    (27, "French interior ministry rocked by a probe into prefect leaks."),
    (28, "Turkey prosecutors seek asset freezes on 108 high-profit traders."),
    (29, "Drone strikes hit homes and a UN building in Khartoum."),
    (30, "Pakistan minister's Delhi visit ends without formal India-Pakistan talks."),
    (31, "India Youth Congress protests at Meta offices over removed accounts."),
    (32, "Taiwan voices concern over Canada's deepening China trade ties."),
    (33, "Japan: mascot mania takes over Saitama with 200 colourful characters."),
    (34, "Morocco: a surreal sculpture park turns the world upside down."),
    (35, "Polls put Spain's PP ahead of PSOE a week before the 29 November vote."),
]
d.text((also_x, bot_y + 1), "ALSO ON SUNDAY 22 NOVEMBER 2026 \u2014 20 MORE STORIES", font=SANS_B(10), fill=INK)
d.text((also_x, bot_y + 14), "in order of consequence", font=SANS(8), fill=GREY)
f_also = SANS(8)
f_also_b = SANS_B(9)
col_w = also_w / 2
for col_i in range(2):
    ax = also_x + col_i * col_w
    ly = bot_y + 22
    for j in range(10):
        num, txt = ALSO[col_i * 10 + j]
        lines = wrap(d, txt, f_also, col_w - 26)
        d.text((ax, ly), str(num), font=f_also_b, fill=RED)
        ly2 = ly
        for ln in lines[:2]:
            d.text((ax + 20, ly2), ln, font=f_also, fill=INK)
            ly2 += 11
        ly = ly2
y = max(bot_y + map_h, ly) + 4

# ---- DATE CHECK ----
dc_y = y
dc_lines = wrap(d, "Left out (other days): the Shenzhen trilateral summit (19\u201320 Nov). Not yet: Spain votes 29 Nov \u00b7 US Senate vote 1 Dec \u00b7 Ganga treaty expiry 12 Dec.", SANS(8), CW - 110)
dc_h = 6 + 10 * len(dc_lines) + 4
d.rectangle([M, dc_y, W - M, dc_y + dc_h], outline=RED, width=2)
d.text((M + 6, dc_y + 4), "DATE CHECK", font=SANS_B(10), fill=RED)
for i, ln in enumerate(dc_lines):
    d.text((M + 92, dc_y + 4 + i * 10), ln, font=SANS(8), fill=INK)
y = dc_y + dc_h + 3

# ---- HOW SURE legend ----
hs_y = y
d.rectangle([M, hs_y, M + 60, hs_y + 13], fill=INK)
d.text((M + 4, hs_y + 2), "HOW SURE", font=SANS_B(8), fill=(255, 255, 255))
leg = [("CONFIRMED", (20, 120, 60), "2+ major outlets"), ("OFFICIAL", (43, 94, 167), "on the record: agency, ministry, federation"), ("REPORTED", (178, 34, 34), "one major outlet")]
lx = M + 66
f_leg2 = SANS(8)
for name, col, desc in leg:
    w = badge(d, lx, hs_y, name, col)
    lx += w + 4
    d.text((lx, hs_y + 2), desc, font=f_leg2, fill=INK)
    lx += tw(d, desc, f_leg2) + 14
y = hs_y + 15

# ---- footer ----
hline(d, M, y, CW, INK, 1)
y += 3
f_foot = SERIF(9)
center(d, M, y, CW, "Every story here happened or was first reported on Sunday 22 November 2026 (UTC), told as the named outlets reported it. All maps and drawings are original vector work.", f_foot, INK)

img.save(os.path.join(HERE, "entry.png"), optimize=True)
print("saved entry.png", img.size, "final y =", y)
