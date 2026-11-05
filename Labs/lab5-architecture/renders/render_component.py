# Renders the Lab 5 component diagram with a controlled layout.
# Auto-layout (PlantUML/Graphviz) produced unreadable ball/socket routing at 10
# interfaces, so the layout here is explicit: every coordinate is chosen so
# provided-interface balls and required-interface sockets land on the correct
# edges and connecting lines stay short.
#
# Run: python renders/render_component.py   -> writes component.png next to it.

from PIL import Image, ImageDraw, ImageFont

S = 2  # supersampling for antialiasing
W, H = 1600, 1300

FONT = "C:/Windows/Fonts/arial.ttf"
FONT_B = "C:/Windows/Fonts/arialbd.ttf"
FONT_I = "C:/Windows/Fonts/ariali.ttf"

img = Image.new("RGB", (W * S, H * S), "white")
d = ImageDraw.Draw(img)


def f(size, bold=False, italic=False):
    path = FONT_B if bold else FONT_I if italic else FONT
    return ImageFont.truetype(path, size * S)


def text(cx, cy, s, bold=False, italic=False, size=14, anchor="mm"):
    d.text((cx * S, cy * S), s, fill="black", font=f(size, bold, italic), anchor=anchor)


def line(pts, width=2):
    d.line([(x * S, y * S) for x, y in pts], fill="black", width=width * S)


def rect(x1, y1, x2, y2, width=2):
    d.rectangle([x1 * S, y1 * S, x2 * S, y2 * S], outline="black", width=width * S)


def circle(cx, cy, r, width=2):
    d.ellipse([(cx - r) * S, (cy - r) * S, (cx + r) * S, (cy + r) * S],
              outline="black", width=width * S, fill="white")


def socket(cx, cy, side, r=10):
    """Required-interface socket: half-circle arc opening toward `side`."""
    box = [(cx - r) * S, (cy - r) * S, (cx + r) * S, (cy + r) * S]
    a0 = {"right": -90, "down": 0, "left": 90, "up": 180}[side]
    d.arc(box, start=a0, end=a0 + 180, fill="black", width=2 * S)


def component(x1, y1, x2, y2, name, sub=None):
    rect(x1, y1, x2, y2)
    # component icon, top-right corner
    ix, iy = x2 - 22, y1 + 7
    rect(ix, iy, ix + 12, iy + 12, width=1)
    rect(ix - 4, iy + 2, ix + 2, iy + 6, width=1)
    rect(ix - 4, iy + 8, ix + 2, iy + 12, width=1)
    cx = (x1 + x2) / 2
    if sub:
        text(cx, y1 + 13, "«component»", italic=True, size=11)
        text(cx, (y1 + y2) / 2 + 5, name, bold=True, size=14)
        text(cx, y2 - 14, sub, size=12)
    else:
        text(cx, y1 + 13, "«component»", italic=True, size=11)
        text(cx, (y1 + y2) / 2 + 5, name, bold=True, size=14)


def actor(cx, cy):
    circle(cx, cy - 22, 10)
    line([(cx, cy - 12), (cx, cy + 12)])
    line([(cx - 14, cy - 4), (cx + 14, cy - 4)])
    line([(cx, cy + 12), (cx - 12, cy + 32)])
    line([(cx, cy + 12), (cx + 12, cy + 32)])
    text(cx, cy + 46, "User", size=14)


def cylinder(x1, y1, x2, y2, name):
    ry = 9
    d.ellipse([x1 * S, y1 * S, x2 * S, (y1 + 2 * ry) * S], outline="black",
              width=2 * S, fill="white")
    line([(x1, y1 + ry), (x1, y2 - ry)])
    line([(x2, y1 + ry), (x2, y2 - ry)])
    d.arc([x1 * S, (y2 - 2 * ry) * S, x2 * S, y2 * S], 0, 180, fill="black",
          width=2 * S)
    text((x1 + x2) / 2, (y1 + y2) / 2 + 5, name, bold=True, size=13)


def ball(cx, cy, label=None, label_pos=None, r=10):
    circle(cx, cy, r)
    if label and label_pos:
        text(*label_pos, label, size=13)


def conn(pts, label=None, label_pos=None):
    """Assembly connector: solid line between socket and ball."""
    line(pts)
    if label and label_pos:
        text(*label_pos, label, size=13)


# ---------------- title / containers ----------------
text(W / 2, 28, "VideoHub Architecture - Component Diagram", bold=True, size=19)

rect(140, 160, 1340, 940)
text(740, 178, "VideoHub System", bold=True, size=16)

rect(140, 1060, 920, 1250)
text(530, 1078, "External Systems", bold=True, size=16)

# ---------------- actor ----------------
actor(290, 95)
line([(290, 137), (290, 192)])
d.polygon([(290 * S, 195 * S), (285 * S, 185 * S), (295 * S, 185 * S)],
          fill="black")

# ---------------- components (uniform grid) ----------------
# row 1: entry layer          (h=80)
component(200, 195, 380, 275, "Frontend", "(Next.js)")
component(540, 195, 780, 275, "API Gateway", "(Express)")
# row 2: domain services      (h=80, uniform 160 wide, 80 gaps)
component(160, 480, 320, 560, "Auth Service")
component(400, 480, 560, 560, "Video Service")
component(640, 480, 800, 560, "Notification Service")
component(880, 480, 1040, 560, "Search Service")
component(1120, 480, 1280, 560, "Comment Service")
# row 3: data layer           (h=70)
component(480, 760, 680, 830, "Data Access Layer", "(Prisma)")
cylinder(740, 770, 880, 830, "PostgreSQL")
# external row                (h=70, same 160-200 box widths)
component(160, 1135, 340, 1205, "Google OAuth")
component(620, 1135, 820, 1205, "Email/SMS Gateway")

# ---------------- interfaces ----------------

# IRestApi: FE requires (socket right) -> GW provides (ball left)
socket(380, 235, "right")
conn([(390, 235), (520, 235)])
ball(530, 235, "IRestApi", (455, 212))

# GW requires four service contracts (sockets on bottom edge, y=275)
for sx, name, bx in [
    (580, "IAuth", 240),
    (620, "IVideoOps", 480),
    (660, "ISearch", 960),
    (700, "ICommentOps", 1200),
]:
    socket(sx, 275, "down")
    conn([(sx, 285), (bx, 460)])
    ball(bx, 470, name, (bx + 17, 452))

# INotify: VS requires -> NS provides (adjacent pair)
socket(560, 510, "right")
conn([(570, 510), (620, 510)])
ball(630, 510, "INotify", (600, 488))

# ISearchIndex: VS requires -> SS provides (orthogonal route over the row)
socket(520, 480, "up")
conn([(520, 470), (520, 440), (900, 440), (900, 460)],
     "ISearchIndex", (710, 423))
ball(900, 470)

# IDataAccess: AUTH/VS/SS/CS require -> single provided ball on DAL
for sx, ex in [(240, 565), (450, 572), (960, 590), (1200, 602)]:
    socket(sx, 560, "down")
    conn([(sx, 570), (ex, 737)])
ball(580, 748, "IDataAccess", (630, 745))

# DAL -> PostgreSQL
line([(680, 800), (736, 800)])
d.polygon([(742 * S, 800 * S), (732 * S, 795 * S), (732 * S, 805 * S)],
          fill="black")

# IGoogleOAuth: AUTH requires -> Google provides (crosses boundary)
socket(200, 560, "down")
conn([(200, 570), (200, 1115)])
ball(200, 1125, "IGoogleOAuth", (215, 850))

# IEmailGateway: NS requires -> Email provides (crosses boundary)
socket(700, 560, "down")
conn([(700, 570), (700, 1115)])
ball(700, 1125, "IEmailGateway", (715, 850))

# ---------------- legend ----------------
rect(1150, 40, 1580, 105, width=1)
socket(1168, 62, "right", r=8)
text(1186, 62, "required interface", size=11, anchor="lm")
ball(1168, 92, r=8)
text(1186, 92, "provided interface", size=11, anchor="lm")

img = img.resize((W, H), Image.LANCZOS)
img.save(__file__.rsplit("\\", 1)[0] + "/component.png")
print("component.png written")
