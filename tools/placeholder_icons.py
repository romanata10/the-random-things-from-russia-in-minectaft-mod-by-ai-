"""Generates simple, clean flat-style placeholder icons (32x32) for items that don't yet
have an AI-generated texture. These can be swapped for nicer art later without touching
any other part of the mod - just overwrite the PNG at the same path.
"""
import os
from PIL import Image, ImageDraw

OUT = os.path.join(os.path.dirname(__file__), "..",
                    "src/main/resources/assets/rushops/textures/item")
os.makedirs(OUT, exist_ok=True)

S = 32
OUTLINE = (30, 24, 20, 255)


def canvas():
    return Image.new("RGBA", (S, S), (0, 0, 0, 0))


def rrect(d, box, radius, fill, outline=OUTLINE, width=1):
    d.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def save(name, im):
    im.save(os.path.join(OUT, name + ".png"))
    print("wrote", name)


def bottle(name, body, cap=(70, 70, 70, 255), label=None):
    im = canvas()
    d = ImageDraw.Draw(im)
    rrect(d, (13, 3, 19, 8), 2, cap)
    rrect(d, (9, 8, 23, 29), 4, body)
    if label:
        d.rectangle((10, 16, 22, 23), fill=label, outline=OUTLINE)
    save(name, im)


def can(name, body, lid=(210, 210, 210, 255), label=None):
    im = canvas()
    d = ImageDraw.Draw(im)
    rrect(d, (8, 5, 24, 27), 3, body)
    d.rectangle((8, 5, 24, 8), fill=lid, outline=OUTLINE)
    if label:
        d.rectangle((9, 14, 23, 22), fill=label, outline=OUTLINE)
    save(name, im)


def box(name, body, tape=(220, 220, 200, 255)):
    im = canvas()
    d = ImageDraw.Draw(im)
    rrect(d, (5, 9, 27, 27), 2, body)
    d.rectangle((14, 9, 18, 27), fill=tape, outline=OUTLINE)
    d.rectangle((5, 16, 27, 20), fill=tape, outline=OUTLINE)
    save(name, im)


def tube(name, body, cap=(230, 230, 230, 255)):
    im = canvas()
    d = ImageDraw.Draw(im)
    d.polygon([(12, 4), (20, 4), (23, 10), (9, 10)], fill=cap, outline=OUTLINE)
    rrect(d, (9, 10, 23, 28), 3, body)
    save(name, im)


def bag(name, body=(235, 235, 240, 255)):
    im = canvas()
    d = ImageDraw.Draw(im)
    d.arc((9, 2, 15, 10), 180, 360, fill=OUTLINE, width=1)
    d.arc((17, 2, 23, 10), 180, 360, fill=OUTLINE, width=1)
    d.polygon([(7, 9), (25, 9), (23, 29), (9, 29)], fill=body, outline=OUTLINE)
    save(name, im)


def device_phone(name):
    im = canvas()
    d = ImageDraw.Draw(im)
    rrect(d, (10, 3, 22, 29), 3, (25, 25, 28, 255))
    d.rectangle((12, 6, 20, 24), fill=(120, 200, 230, 255))
    save(name, im)


def device_laptop(name):
    im = canvas()
    d = ImageDraw.Draw(im)
    d.polygon([(6, 10), (26, 10), (24, 22), (8, 22)], fill=(60, 60, 65, 255), outline=OUTLINE)
    d.rectangle((9, 12, 23, 20), fill=(120, 200, 230, 255))
    d.polygon([(3, 22), (29, 22), (27, 26), (5, 26)], fill=(150, 150, 155, 255), outline=OUTLINE)
    save(name, im)


def headphones(name):
    im = canvas()
    d = ImageDraw.Draw(im)
    d.arc((7, 4, 25, 26), 180, 360, fill=OUTLINE, width=3)
    d.ellipse((5, 16, 13, 27), fill=(35, 35, 38, 255), outline=OUTLINE)
    d.ellipse((19, 16, 27, 27), fill=(35, 35, 38, 255), outline=OUTLINE)
    save(name, im)


def power_bank(name):
    im = canvas()
    d = ImageDraw.Draw(im)
    rrect(d, (8, 6, 24, 27), 3, (35, 35, 38, 255))
    d.polygon([(17, 10), (13, 18), (16, 18), (14, 23), (20, 15), (17, 15)], fill=(240, 220, 60, 255))
    save(name, im)


def toy_car(name):
    im = canvas()
    d = ImageDraw.Draw(im)
    rrect(d, (5, 14, 27, 22), 3, (205, 40, 40, 255))
    d.polygon([(10, 14), (14, 8), (22, 8), (24, 14)], fill=(205, 40, 40, 255), outline=OUTLINE)
    d.rectangle((13, 10, 21, 14), fill=(170, 220, 235, 255))
    d.ellipse((6, 20, 13, 27), fill=(25, 25, 25, 255))
    d.ellipse((19, 20, 26, 27), fill=(25, 25, 25, 255))
    save(name, im)


def teddy_bear(name):
    im = canvas()
    d = ImageDraw.Draw(im)
    brown = (150, 105, 65, 255)
    d.ellipse((9, 3, 15, 9), fill=brown, outline=OUTLINE)
    d.ellipse((17, 3, 23, 9), fill=brown, outline=OUTLINE)
    d.ellipse((8, 7, 24, 21), fill=brown, outline=OUTLINE)
    d.ellipse((7, 19, 15, 29), fill=brown, outline=OUTLINE)
    d.ellipse((17, 19, 25, 29), fill=brown, outline=OUTLINE)
    d.ellipse((13, 12, 19, 18), fill=(200, 170, 130, 255), outline=OUTLINE)
    save(name, im)


def rubiks(name):
    im = canvas()
    d = ImageDraw.Draw(im)
    colors = [(230, 60, 50, 255), (250, 210, 40, 255), (60, 160, 70, 255),
              (40, 90, 200, 255), (240, 240, 240, 255), (240, 130, 30, 255)]
    rrect(d, (5, 5, 27, 27), 3, (20, 20, 20, 255))
    i = 0
    for r in range(3):
        for c in range(3):
            x0, y0 = 6 + c * 7, 6 + r * 7
            d.rectangle((x0, y0, x0 + 6, y0 + 6), fill=colors[i % len(colors)], outline=OUTLINE)
            i += 1
    save(name, im)


def blocks_set(name):
    im = canvas()
    d = ImageDraw.Draw(im)
    rrect(d, (5, 11, 27, 27), 2, (235, 170, 40, 255))
    colors = [(210, 50, 50, 255), (50, 140, 210, 255), (60, 170, 70, 255), (240, 220, 50, 255)]
    pos = [(7, 4), (14, 2), (20, 5)]
    for (px, py), col in zip(pos, colors):
        d.rectangle((px, py, px + 6, py + 7), fill=col, outline=OUTLINE)
    save(name, im)


def blob(name, body):
    im = canvas()
    d = ImageDraw.Draw(im)
    d.ellipse((6, 10, 26, 25), fill=body, outline=OUTLINE)
    d.ellipse((10, 6, 20, 14), fill=body, outline=OUTLINE)
    save(name, im)


def carton(name, body=(235, 235, 235, 255), mark=None):
    im = canvas()
    d = ImageDraw.Draw(im)
    d.polygon([(10, 3), (22, 3), (24, 8), (8, 8)], fill=body, outline=OUTLINE)
    d.rectangle((8, 8, 24, 28), fill=body, outline=OUTLINE)
    if mark:
        d.line((11, 15, 21, 22), fill=mark, width=2)
        d.line((21, 15, 11, 22), fill=mark, width=2)
    save(name, im)


def coin_token(name):
    im = canvas()
    d = ImageDraw.Draw(im)
    d.ellipse((4, 4, 28, 28), fill=(205, 170, 60, 255), outline=OUTLINE, width=2)
    d.rectangle((12, 13, 20, 19), outline=(90, 70, 20, 255), width=2)
    d.ellipse((10, 19, 14, 23), outline=(90, 70, 20, 255), width=1)
    d.ellipse((18, 19, 22, 23), outline=(90, 70, 20, 255), width=1)
    save(name, im)


def price_gun(name):
    im = canvas()
    d = ImageDraw.Draw(im)
    d.rectangle((6, 13, 20, 18), fill=(90, 90, 95, 255), outline=OUTLINE)
    d.polygon([(14, 18), (20, 18), (18, 27), (12, 27)], fill=(60, 60, 65, 255), outline=OUTLINE)
    d.rectangle((20, 14, 26, 17), fill=(220, 190, 40, 255), outline=OUTLINE)
    save(name, im)


def bag_food(name, body, label=None):
    im = canvas()
    d = ImageDraw.Draw(im)
    d.polygon([(8, 3), (24, 3), (27, 29), (5, 29)], fill=body, outline=OUTLINE)
    if label:
        d.rectangle((9, 12, 23, 20), fill=label, outline=OUTLINE)
    save(name, im)


def jar(name, body, lid=(200, 200, 200, 255)):
    im = canvas()
    d = ImageDraw.Draw(im)
    d.rectangle((12, 2, 20, 7), fill=lid, outline=OUTLINE)
    d.rounded_rectangle((7, 7, 25, 29), radius=4, fill=body, outline=OUTLINE)
    save(name, im)


def box_food(name, body, accent=None):
    im = canvas()
    d = ImageDraw.Draw(im)
    d.rectangle((5, 8, 27, 27), fill=body, outline=OUTLINE)
    if accent:
        d.rectangle((5, 8, 27, 13), fill=accent, outline=OUTLINE)
    save(name, im)


def meat_piece(name, body):
    im = canvas()
    d = ImageDraw.Draw(im)
    d.ellipse((5, 9, 27, 24), fill=body, outline=OUTLINE)
    d.line((9, 13, 23, 20), fill=(240, 240, 240, 255), width=2)
    save(name, im)


bottle("kvass_bottle", (90, 60, 30, 255), cap=(60, 60, 60, 255), label=(200, 170, 110, 255))
bag_food("kefir_carton", (235, 235, 240, 255), label=(80, 140, 210, 255))
can("tushonka_can", (190, 160, 80, 255), label=(230, 220, 190, 255))
can("sgushenka_can", (60, 110, 200, 255), label=(235, 235, 235, 255))
box_food("glazed_cheese_curd", (235, 220, 190, 255), accent=(120, 70, 40, 255))
box_food("yarche_cookies", (230, 200, 60, 255), accent=(255, 255, 255, 255))
bag_food("yarche_crackers", (200, 150, 70, 255), label=(255, 255, 255, 255))
can("fix_price_soda", (210, 40, 40, 255), label=(255, 255, 255, 255))
bag_food("pyaterochka_bread", (210, 150, 70, 255), label=(230, 120, 30, 255))
box_food("instant_noodles", (235, 200, 60, 255), accent=(210, 40, 40, 255))
bag_food("pelmeni_pack", (225, 225, 230, 255), label=(200, 60, 60, 255))
jar("mayonnaise_jar", (245, 245, 235, 255))
bag_food("sunflower_seeds_pack", (210, 160, 60, 255), label=(60, 60, 60, 255))
bag_food("sushki_pack", (220, 190, 140, 255), label=(180, 60, 60, 255))
box_food("pryaniki_pack", (200, 140, 90, 255), accent=(220, 60, 60, 255))
meat_piece("salo_piece", (250, 235, 215, 255))

bottle("shampoo_bottle", (230, 170, 40, 255), cap=(255, 255, 255, 255), label=(255, 220, 150, 255))
bottle("perfume_bottle", (190, 150, 210, 255), cap=(220, 190, 70, 255), label=(230, 210, 240, 255))
bottle("bleach_bottle", (230, 230, 140, 255), cap=(255, 255, 255, 255), label=(80, 140, 220, 255))
bottle("dish_soap", (60, 170, 120, 255), cap=(255, 255, 255, 255), label=(200, 240, 220, 255))
bottle("toilet_cleaner", (60, 110, 200, 255), cap=(255, 255, 255, 255), label=(200, 220, 250, 255))

can("yarche_cookies_unused", (0, 0, 0, 0))  # placeholder not used, keep function referenced

box("washing_powder", (70, 120, 200, 255))
box("cardboard_box", (165, 120, 75, 255))

tube("toothpaste_tube", (235, 240, 245, 255))

bag("plastic_bag")

device_phone("smartphone")
device_laptop("laptop")
headphones("wireless_headphones")
power_bank("power_bank")

toy_car("toy_car")
teddy_bear("teddy_bear")
rubiks("rubiks_cube")
blocks_set("building_blocks_set")

blob("rotten_sausage", (120, 140, 60, 255))
blob("spoiled_meat", (150, 80, 70, 255))
carton("expired_milk", body=(225, 225, 215, 255), mark=(200, 30, 30, 255))

# moldy bread: tan loaf with green spots
im = canvas()
d = ImageDraw.Draw(im)
d.rounded_rectangle((5, 13, 27, 25), radius=6, fill=(195, 150, 90, 255), outline=OUTLINE)
d.arc((5, 5, 27, 21), 180, 360, fill=OUTLINE, width=1)
for (mx, my) in [(10, 17), (16, 15), (21, 19), (13, 21)]:
    d.ellipse((mx - 2, my - 2, mx + 2, my + 2), fill=(90, 150, 70, 255))
save("moldy_bread", im)

# soap bar
im = canvas()
d = ImageDraw.Draw(im)
d.rounded_rectangle((6, 11, 26, 23), radius=5, fill=(245, 240, 225, 255), outline=OUTLINE)
save("soap_bar", im)

coin_token("shopping_cart_token")
price_gun("price_gun")

os.remove(os.path.join(OUT, "yarche_cookies_unused.png"))

print("done")
