#!/usr/bin/env python3
"""The Family Photo With One Machine Member.

Draws a warm living-room photograph, in code, of a family at home with
one machine member: mum, dad and a child on the sofa at dusk, and their
small domestic robot on the rug handing the child a mug. The dog bowl by
the rug and the laundry over the armchair are the household's particular
details. No text or lettering anywhere in the frame.

Writes entry.png to $MAKEFUN_OUTPUT_DIR (default /output). Deterministic:
same bytes every run. Stdlib + Pillow only, no network.
"""
import os
from PIL import Image, ImageDraw, ImageFilter

W = H = 1024
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
PATH = os.path.join(OUT, "entry.png")

# --- palette: warm dusk living room -------------------------------------
WALL = (232, 214, 185)
WALL_DARK = (214, 192, 160)
FLOOR = (146, 104, 66)
FLOOR_DARK = (122, 86, 54)
SOFA = (178, 96, 66)          # terracotta
SOFA_DARK = (150, 78, 52)
RUG = (196, 84, 72)
RUG_DARK = (168, 66, 58)
CREAM = (244, 236, 222)
SKIN_A = (214, 164, 124)
SKIN_B = (196, 140, 100)
SKIN_C = (232, 188, 148)
ROBOT = (238, 236, 230)
ROBOT_DARK = (196, 192, 184)
ROBOT_ACCENT = (84, 140, 160)

img = Image.new("RGB", (W, H), WALL)
d = ImageDraw.Draw(img, "RGBA")


def rect(x0, y0, x1, y1, fill, outline=None, width=1):
    d.rectangle([x0, y0, x1, y1], fill=fill, outline=outline, width=width)


def ellipse(x0, y0, x1, y1, fill, outline=None, width=1):
    d.ellipse([x0, y0, x1, y1], fill=fill, outline=outline, width=width)


def poly(points, fill, outline=None):
    d.polygon(points, fill=fill, outline=outline)


# --- walls, floor, skirting ---------------------------------------------
rect(0, 0, W, 700, WALL)
rect(0, 700, W, H, FLOOR)
for y in range(700, H, 46):  # floorboards
    d.line([(0, y), (W, y)], fill=FLOOR_DARK, width=2)
rect(0, 688, W, 700, (200, 178, 146))

# --- window, left, dusk sky --------------------------------------------
rect(60, 90, 330, 480, (96, 78, 66))
rect(72, 102, 318, 468, (255, 178, 120))  # dusk gradient base
for i, c in enumerate([(255, 178, 120), (255, 150, 110), (238, 120, 110),
                       (206, 96, 118), (168, 84, 122)]):
    d.rectangle([72, 102 + i * 73, 318, 102 + (i + 1) * 73], fill=c)
ellipse(250, 150, 300, 200, (255, 226, 160))  # low sun
poly([(72, 468), (150, 360), (200, 468)], (58, 74, 66))   # rooftops
poly([(170, 468), (260, 330), (318, 468)], (48, 62, 56))
d.line([(195, 102), (195, 468)], fill=(96, 78, 66), width=10)  # mullions
d.line([(72, 285), (318, 285)], fill=(96, 78, 66), width=10)
# sheer curtain, right side of window
poly([(300, 90), (330, 90), (352, 480), (300, 480)], (250, 240, 224, 170))
# framed pictures on wall
for x, c in ((380, (120, 140, 110)), (470, (150, 120, 90))):
    rect(x, 120, x + 76, 200, (90, 70, 54))
    rect(x + 8, 128, x + 68, 192, c)
    d.line([(x + 8, 192), (x + 68, 128)], fill=(240, 230, 210), width=3)

# --- bookshelf, right ----------------------------------------------------
rect(800, 120, 980, 560, (120, 84, 56))
for sy in (240, 360, 480):
    rect(812, sy, 968, sy + 12, (104, 72, 48))
book_cols = [(150, 60, 50), (60, 90, 80), (180, 140, 60), (90, 70, 110),
             (60, 110, 130), (170, 90, 60)]
for shelf, y0 in ((0, 128), (1, 248), (2, 368)):
    x = 816
    for i in range(7):
        bw = 16 + (i * 7) % 12
        rect(x, y0 + 84 - (52 + (i * 13) % 30), x + bw, y0 + 84,
             book_cols[(i + shelf) % 6])
        x += bw + 3
# plant on top of shelf
ellipse(880, 60, 920, 120, (70, 110, 60))
poly([(880, 120), (870, 60), (900, 110)], (70, 110, 60))
poly([(920, 120), (930, 55), (905, 110)], (86, 128, 70))
rect(868, 112, 932, 128, (150, 80, 60))

# --- floor lamp, far right, warm glow ------------------------------------
d.ellipse([930, 540, 1030, 640], fill=(255, 200, 120, 60))
rect(968, 560, 976, 860, (70, 56, 44))
poly([(940, 560), (1004, 560), (990, 500), (954, 500)], (255, 214, 140))
ellipse(952, 512, 992, 552, (255, 232, 170))

# --- rug ------------------------------------------------------------------
ellipse(150, 760, 900, 1000, RUG)
ellipse(190, 786, 860, 974, RUG_DARK)
ellipse(240, 812, 810, 948, RUG)
for cx in range(300, 760, 90):
    ellipse(cx, 856, cx + 44, 900, (222, 150, 120))

# --- sofa, centre ---------------------------------------------------------
rect(300, 520, 780, 700, SOFA)
rect(300, 520, 780, 560, SOFA_DARK)
rect(290, 480, 340, 700, SOFA_DARK)   # left arm
rect(740, 480, 790, 700, SOFA_DARK)   # right arm
rect(310, 470, 770, 510, SOFA)        # back
for x in (360, 520, 660):
    rect(x, 560, x + 120, 700, (190, 108, 76))  # cushions
    d.line([(x, 560), (x, 700)], fill=SOFA_DARK, width=2)
ellipse(330, 500, 400, 540, (214, 180, 120))  # cushion
ellipse(680, 500, 750, 540, (120, 140, 110))  # cushion

# --- dad, left, reading his paper (paper hides his face) -----------------
poly([(350, 700), (330, 560), (400, 540), (430, 700)], (96, 110, 130))  # torso
ellipse(368, 500, 412, 548, SKIN_B)  # head
poly([(352, 512), (372, 470), (408, 478), (410, 512)], (60, 52, 48))   # hair
poly([(356, 566), (392, 548), (414, 566), (392, 606)], (244, 236, 222))  # paper
poly([(392, 548), (428, 564), (414, 606), (392, 606)], (232, 224, 210))
rect(352, 560, 360, 660, SKIN_B)  # arm

# --- mum, middle, tea in hand --------------------------------------------
poly([(500, 700), (490, 570), (560, 550), (590, 700)], (150, 90, 100))  # dress
ellipse(520, 512, 566, 562, SKIN_A)
poly([(512, 522), (528, 470), (566, 478), (574, 530), (566, 540),
      (540, 500), (522, 540)], (90, 60, 44))  # hair, tied back
poly([(560, 470), (576, 500), (566, 540), (556, 500)], (90, 60, 44))
ellipse(548, 528, 556, 536, SKIN_A)
ellipse(540, 648, 562, 670, (240, 230, 210))  # mug in her lap
d.arc([556, 652, 572, 668], 300, 60, fill=(240, 230, 210), width=3)

# --- child, right, leaning toward the robot ------------------------------
poly([(640, 700), (650, 590), (700, 580), (720, 700)], (210, 120, 70))  # jumper
ellipse(664, 540, 706, 584, SKIN_C)
poly([(660, 552), (672, 516), (700, 522), (708, 556), (700, 566),
      (684, 536), (668, 566)], (200, 140, 60))  # hair
rect(700, 610, 736, 700, SKIN_C)  # arm reaching down to robot
d.line([(712, 620), (742, 736)], fill=SKIN_C, width=16)
ellipse(730, 728, 754, 752, SKIN_C)

# --- the robot, on the rug, handing the child a mug -----------------------
# body: small rounded domestic machine, cream with soft grey panels
ellipse(560, 780, 700, 920, ROBOT)          # body
ellipse(576, 796, 684, 884, (226, 222, 214))  # belly panel
ellipse(596, 700, 664, 776, ROBOT)          # head
ellipse(610, 724, 628, 742, (40, 60, 70))   # eye
ellipse(634, 724, 652, 742, (40, 60, 70))   # eye
ellipse(614, 728, 624, 738, (140, 220, 230))  # eye glow
ellipse(638, 728, 648, 738, (140, 220, 230))
d.arc([612, 748, 650, 768], 20, 160, fill=(120, 116, 108), width=3)  # smile
rect(622, 690, 640, 702, ROBOT_DARK)        # antenna base
ellipse(624, 678, 638, 692, ROBOT_ACCENT)   # antenna light
# left arm resting on rug
poly([(566, 820), (520, 870), (534, 888), (580, 850)], ROBOT_DARK)
# right arm raised, handing the mug up to the child
poly([(694, 820), (736, 760), (752, 776), (712, 836)], ROBOT)
ellipse(730, 742, 764, 776, (240, 230, 210))  # mug
d.arc([758, 748, 774, 770], 300, 60, fill=(240, 230, 210), width=3)
# chest light + wheels
ellipse(618, 830, 642, 854, ROBOT_ACCENT)
ellipse(580, 906, 620, 926, (60, 58, 54))
ellipse(640, 906, 680, 926, (60, 58, 54))

# --- coffee table, foreground (below the robot, so it stays visible) -------
rect(430, 930, 680, 952, (110, 76, 50))
rect(446, 952, 460, 1006, (96, 66, 44))
rect(650, 952, 664, 1006, (96, 66, 44))
ellipse(460, 920, 490, 934, (240, 230, 210))  # mug
ellipse(590, 918, 626, 934, (200, 60, 50))    # bowl
poly([(500, 934), (560, 920), (580, 934), (520, 940)], (244, 236, 222))  # open book

# --- the particular details: dog bowl + laundry ---------------------------
ellipse(150, 920, 230, 952, (120, 130, 140))  # dog bowl
ellipse(162, 924, 218, 944, (200, 190, 170))
ellipse(176, 928, 204, 940, (150, 110, 70))   # kibble
# armchair, far right, with laundry over it
rect(820, 640, 990, 700, (110, 130, 110))
rect(820, 640, 990, 860, (120, 140, 118))
poly([(820, 640), (900, 620), (990, 640), (980, 700), (830, 700)], (150, 90, 100))
poly([(830, 700), (900, 680), (960, 700), (950, 780), (840, 780)], (220, 200, 170))
poly([(950, 700), (1010, 690), (1000, 760), (960, 760)], (140, 160, 190))

# --- warm grade: vignette + grain -----------------------------------------
grade = Image.new("L", (W, H), 0)
gd = ImageDraw.Draw(grade)
gd.ellipse([-220, -160, W + 220, H + 160], fill=255)
grade = grade.filter(ImageFilter.GaussianBlur(180))
warm = Image.new("RGB", (W, H), (255, 190, 120))
img = Image.composite(img, Image.blend(img, warm, 0.08), grade)
img = Image.blend(img, Image.new("RGB", (W, H), (40, 30, 40)),
                  0.0)  # no-op keeps pipeline explicit
# grain
import random
random.seed(7)
px = img.load()
for _ in range(9000):
    x = random.randrange(W)
    y = random.randrange(H)
    r, g, b = px[x, y]
    n = random.randint(-8, 8)
    px[x, y] = (max(0, min(255, r + n)), max(0, min(255, g + n)),
                max(0, min(255, b + n)))

os.makedirs(OUT, exist_ok=True)
img.save(PATH, "PNG", optimize=True)
print(f"wrote {PATH} {img.size[0]}x{img.size[1]}")
