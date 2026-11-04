import json
import os
import random
import sys

sys.path.insert(0, os.path.dirname(__file__))
from mod_data import STRUCTURES

from nbtlib import File, Compound, List, Int, String, Byte

ROOT = os.path.join(os.path.dirname(__file__), "..")
DATA_DIR = os.path.join(ROOT, "src/main/resources/data/rushops")
STRUCT_NBT_DIR = os.path.join(DATA_DIR, "structures")
WG_STRUCT_DIR = os.path.join(DATA_DIR, "worldgen/structure")
WG_SET_DIR = os.path.join(DATA_DIR, "worldgen/structure_set")
WG_POOL_DIR = os.path.join(DATA_DIR, "worldgen/template_pool")
LOOT_DIR = os.path.join(DATA_DIR, "loot_tables/chests")

for d in (STRUCT_NBT_DIR, WG_STRUCT_DIR, WG_SET_DIR, WG_POOL_DIR, LOOT_DIR):
    os.makedirs(d, exist_ok=True)

BIOMES_DEFAULT = [
    "minecraft:plains", "minecraft:sunflower_plains", "minecraft:meadow",
    "minecraft:forest", "minecraft:birch_forest", "minecraft:savanna",
    "minecraft:taiga", "minecraft:snowy_plains",
]
BIOMES_SVETOFOR = [
    "minecraft:plains", "minecraft:desert", "minecraft:savanna",
    "minecraft:badlands", "minecraft:snowy_plains", "minecraft:windswept_gravelly_hills",
]
BIOMES_HYPERMARKET = [
    "minecraft:plains", "minecraft:sunflower_plains", "minecraft:meadow", "minecraft:savanna",
]

BIOME_OVERRIDES = {
    "svetofor_store": BIOMES_SVETOFOR,
    "lenta_metro_store": BIOMES_HYPERMARKET,
    "auchan_store": BIOMES_HYPERMARKET,
}


class Builder:
    def __init__(self, w, h, d):
        self.w, self.h, self.d = w, h, d
        self.blocks = {}  # (x,y,z) -> (block_id, properties_dict or None, nbt_dict or None)

    def set(self, x, y, z, block_id, properties=None, nbt=None):
        if 0 <= x < self.w and 0 <= y < self.h and 0 <= z < self.d:
            self.blocks[(x, y, z)] = (block_id, properties, nbt)

    def get(self, x, y, z):
        return self.blocks.get((x, y, z))


def is_perimeter(x, z, w, d):
    return x == 0 or x == w - 1 or z == 0 or z == d - 1


def build_local(shop):
    """Builds the core building (walls/roof/door/sign/chest/shelving) in LOCAL
    coordinates where z=0 is always the front (entrance) wall."""
    w, core_h, d = shop["size"]
    pitched = shop.get("pitched_roof", False)
    rundown = shop.get("rundown", False)
    rnd = random.Random(shop["id"])

    wall = "minecraft:" + shop["wall"]
    floor = "minecraft:" + shop["floor"]
    roof = "minecraft:" + shop["roof"]
    accent = "minecraft:" + shop["accent"]
    glass = "minecraft:" + shop["glass"]
    door_wood = shop.get("door", "oak")
    door_block = f"minecraft:{door_wood}_door"

    if pitched:
        max_edge = (w - 1) // 2
        ridge_level = core_h + max_edge
        total_h = ridge_level + 2
    else:
        total_h = core_h + 2

    b = Builder(w, total_h, d)

    # floor
    for x in range(w):
        for z in range(d):
            b.set(x, 0, z, floor)

    # walls
    for y in range(1, core_h):
        for x in range(w):
            for z in range(d):
                if is_perimeter(x, z, w, d):
                    block = wall
                    if rundown and rnd.random() < 0.18:
                        block = "minecraft:mossy_cobblestone"
                    b.set(x, y, z, block)

    # window band just below the eaves
    window_y = max(1, core_h - 2)
    for x in range(w):
        for z in (0, d - 1):
            if 1 < x < w - 2 and x % 2 == 0:
                b.set(x, window_y, z, glass)
    for z in range(d):
        for x in (0, w - 1):
            if 1 < z < d - 2 and z % 2 == 0:
                b.set(x, window_y, z, glass)

    # entrance door(s) on the front wall (z = 0)
    cx = w // 2
    door_xs = [cx - 1, cx] if w >= 6 else [cx]
    for x in door_xs:
        b.set(x, 1, 0, door_block, {
            "facing": "south", "half": "lower", "hinge": "left", "open": "false", "powered": "false",
        })
        b.set(x, 2, 0, door_block, {
            "facing": "south", "half": "upper", "hinge": "left", "open": "false", "powered": "false",
        })
        if core_h >= 5:
            b.set(x, 3, 0, glass)

    # roof
    if pitched:
        for x in range(w):
            edge_dist = min(x, w - 1 - x)
            level = core_h + edge_dist
            if edge_dist == max_edge:
                # ridge cap, full width run down the whole building
                for z in range(d):
                    b.set(x, level, z, roof)
            else:
                facing = "east" if x < cx else "west"
                for z in range(d):
                    b.set(x, level, z, roof_stairs_id(shop["roof"]), {
                        "facing": facing, "half": "bottom", "shape": "straight", "waterlogged": "false",
                    })
                # close the triangular gable ends at the front/back walls
                for z in (0, d - 1):
                    for y in range(core_h, level):
                        block = wall
                        if rundown and rnd.random() < 0.18:
                            block = "minecraft:mossy_cobblestone"
                        b.set(x, y, z, block)
        sign_x, sign_y = cx, ridge_level + 1
    else:
        holes = set()
        if rundown:
            candidates = [(x, z) for x in range(1, w - 1) for z in range(1, d - 1)]
            rnd.shuffle(candidates)
            holes = set(candidates[: max(1, len(candidates) // 12)])
        for x in range(w):
            for z in range(d):
                if (x, z) in holes:
                    continue
                if is_perimeter(x, z, w, d):
                    b.set(x, core_h, z, accent)
                else:
                    b.set(x, core_h, z, roof)
        sign_x, sign_y = cx, core_h + 1

    # interior shelving
    interior_ok = w >= 7 and d >= 6
    if interior_ok:
        shelf_xs = [2, w - 3] if w >= 9 else [w // 2]
        for sx in shelf_xs:
            for z in range(2, d - 2):
                if not is_perimeter(sx, z, w, d):
                    b.set(sx, 1, z, "minecraft:bookshelf")
                    if core_h > 4:
                        b.set(sx, 2, z, "minecraft:bookshelf")

    # cobwebs for run-down shops
    if rundown:
        for _ in range(6):
            x = rnd.randint(1, w - 2)
            z = rnd.randint(1, d - 2)
            y = rnd.randint(1, core_h - 1)
            if b.get(x, y, z) is None:
                b.set(x, y, z, "minecraft:cobweb")

    # chest(s) with the shop loot table
    loot_table = f"rushops:chests/{shop['id']}"
    chest_positions = [(w // 2, 1, d - 2)]
    if w * d > 140:
        chest_positions = [(w // 3, 1, d - 2), ((2 * w) // 3, 1, d - 2)]
    for (cxp, cyp, czp) in chest_positions:
        b.set(cxp, cyp, czp, "minecraft:chest", {"facing": "south"},
              {"id": "minecraft:chest", "LootTable": loot_table, "LootTableSeed": 0})

    # sign on the roof peak / parapet above the entrance
    sign_text = shop["ru"][:15]
    b.set(sign_x, sign_y, 0, "minecraft:oak_sign", {"rotation": "8", "waterlogged": "false"},
          {
              "id": "minecraft:sign",
              "front_text": {
                  "has_glowing_text": 0,
                  "color": "black",
                  "messages": [json.dumps(sign_text, ensure_ascii=False), '""', '""', '""'],
              },
              "back_text": {
                  "has_glowing_text": 0,
                  "color": "black",
                  "messages": ['""', '""', '""', '""'],
              },
              "is_waxed": 0,
          })

    # Explicitly carve out air for every empty interior/attic cell so the
    # building reads as hollow even when it overlaps hills, trees or caves -
    # without this, unset cells are simply left untouched by the structure
    # template and whatever terrain was already there would stay in place.
    for y in range(1, core_h):
        for x in range(w):
            for z in range(d):
                if b.get(x, y, z) is None:
                    b.set(x, y, z, "minecraft:air")
    if pitched:
        for x in range(w):
            edge_dist = min(x, w - 1 - x)
            level = core_h + edge_dist
            for y in range(core_h, level):
                for z in range(1, d - 1):
                    if b.get(x, y, z) is None:
                        b.set(x, y, z, "minecraft:air")

    return b, (w, total_h, d)


def roof_stairs_id(roof_block_name):
    # Concrete/terracotta don't have stair variants, so pick the closest-looking
    # stair block that actually exists in vanilla for the roof silhouette.
    mapping = {
        "red_concrete": "minecraft:brick_stairs",
        "green_concrete": "minecraft:dark_oak_stairs",
        "blue_concrete": "minecraft:dark_prismarine_stairs",
        "black_concrete": "minecraft:blackstone_stairs",
        "white_concrete": "minecraft:quartz_stairs",
        "yellow_concrete": "minecraft:dark_oak_stairs",
        "orange_concrete": "minecraft:dark_oak_stairs",
        "purple_concrete": "minecraft:purpur_stairs",
        "red_terracotta": "minecraft:cobblestone_stairs",
        "gray_concrete": "minecraft:andesite_stairs",
    }
    return mapping.get(roof_block_name, "minecraft:stone_brick_stairs")


def apply_front_apron(local_builder, size, shop):
    w, total_h, d = size
    margin = shop.get("front_margin", 0)
    final = Builder(w, total_h, d + margin)

    for (x, y, z), (block_id, props, nbt) in local_builder.blocks.items():
        final.set(x, y, z + margin, block_id, props, nbt)

    apron = shop.get("apron")
    if apron and margin > 0:
        apron_block = "minecraft:" + apron
        for x in range(w):
            for z in range(margin):
                final.set(x, 0, z, apron_block)
                for y in (1, 2, 3):
                    final.set(x, y, z, "minecraft:air")

        stripe = shop.get("apron_stripe")
        if stripe and margin >= 3:
            stripe_block = "minecraft:" + stripe
            for x in range(0, w, 3):
                for z in range(1, margin - 1):
                    final.set(x, 0, z, stripe_block)

        if shop.get("lamp_posts") and margin >= 2:
            lamp_z = max(0, margin - 2)
            for lx in (0, w - 1):
                final.set(lx, 1, lamp_z, "minecraft:cobblestone_wall")
                final.set(lx, 2, lamp_z, "minecraft:glowstone")

        if shop.get("bushes") and margin >= 1:
            plant = "minecraft:dead_bush" if shop.get("rundown") else "minecraft:potted_red_tulip"
            bush_z = margin - 1
            for bx in (1, w - 2):
                if 0 < bx < w - 1:
                    final.set(bx, 1, bush_z, plant)

    return final, (w, total_h, d + margin)


def to_nbt(builder, size):
    palette = []
    palette_index = {}

    def pal_id(block_id, properties):
        key = (block_id, tuple(sorted((properties or {}).items())))
        if key not in palette_index:
            entry = Compound({"Name": String(block_id)})
            if properties:
                entry["Properties"] = Compound({k: String(v) for k, v in properties.items()})
            palette_index[key] = len(palette)
            palette.append(entry)
        return palette_index[key]

    blocks_list = []
    for (x, y, z), (block_id, properties, nbt) in builder.blocks.items():
        state = pal_id(block_id, properties)
        entry = Compound({
            "state": Int(state),
            "pos": List[Int]([Int(x), Int(y), Int(z)]),
        })
        if nbt:
            entry["nbt"] = dict_to_compound(nbt)
        blocks_list.append(entry)

    root = Compound({
        "DataVersion": Int(3465),
        "size": List[Int]([Int(size[0]), Int(size[1]), Int(size[2])]),
        "entities": List[Compound]([]),
        "blocks": List[Compound](blocks_list),
        "palette": List[Compound](palette),
    })
    return root


def dict_to_compound(d):
    if isinstance(d, dict):
        return Compound({k: dict_to_compound(v) for k, v in d.items()})
    if isinstance(d, bool):
        return Byte(1 if d else 0)
    if isinstance(d, int):
        return Int(d)
    if isinstance(d, str):
        return String(d)
    if isinstance(d, list):
        return List([dict_to_compound(v) for v in d])
    return d


def write_structure_json(shop):
    biomes = BIOME_OVERRIDES.get(shop["id"], BIOMES_DEFAULT)
    data = {
        "type": "minecraft:jigsaw",
        "biomes": biomes,
        "step": "surface_structures",
        "spawn_overrides": {},
        "terrain_adaptation": "beard_thin",
        "start_pool": f"rushops:{shop['id']}/start",
        "size": 1,
        "start_height": {"type": "minecraft:constant", "value": {"absolute": 0}},
        "use_expansion_hack": False,
        "project_start_to_heightmap": "WORLD_SURFACE_WG",
        "max_distance_from_center": 80,
    }
    with open(os.path.join(WG_STRUCT_DIR, shop["id"] + ".json"), "w") as f:
        json.dump(data, f, indent=2)
        f.write("\n")


def write_pool_json(shop):
    pool_dir = os.path.join(WG_POOL_DIR, shop["id"])
    os.makedirs(pool_dir, exist_ok=True)
    data = {
        "name": f"rushops:{shop['id']}/start",
        "fallback": "minecraft:empty",
        "elements": [
            {
                "weight": 1,
                "element": {
                    "element_type": "minecraft:single_pool_element",
                    "location": f"rushops:{shop['id']}",
                    "processors": "minecraft:empty",
                    "projection": "rigid",
                },
            }
        ],
    }
    with open(os.path.join(pool_dir, "start.json"), "w") as f:
        json.dump(data, f, indent=2)
        f.write("\n")


def write_structure_set_json(shop):
    data = {
        "structures": [{"structure": f"rushops:{shop['id']}", "weight": 1}],
        "placement": {
            "type": "minecraft:random_spread",
            "salt": shop["salt"],
            "frequency_reduction_method": "legacy_type_1",
            "frequency": 1.0,
            "spacing": shop["spacing"],
            "separation": shop["separation"],
            "locate_offset": [0, 0, 0],
        },
    }
    with open(os.path.join(WG_SET_DIR, shop["id"] + ".json"), "w") as f:
        json.dump(data, f, indent=2)
        f.write("\n")


def write_loot_table(shop):
    entries = []
    for (item_id, weight, lo, hi) in shop["loot"]:
        entry = {
            "type": "minecraft:item",
            "name": item_id,
            "weight": weight,
        }
        if not (lo == 1 and hi == 1):
            entry["functions"] = [
                {
                    "function": "minecraft:set_count",
                    "count": {"type": "minecraft:uniform", "min": lo, "max": hi},
                }
            ]
        entries.append(entry)
    data = {
        "type": "minecraft:chest",
        "pools": [
            {
                "rolls": {"type": "minecraft:uniform", "min": 3, "max": 6},
                "entries": entries,
            }
        ],
    }
    with open(os.path.join(LOOT_DIR, shop["id"] + ".json"), "w") as f:
        json.dump(data, f, indent=2)
        f.write("\n")


for shop in STRUCTURES:
    local_builder, local_size = build_local(shop)
    final_builder, final_size = apply_front_apron(local_builder, local_size, shop)
    nbt_root = to_nbt(final_builder, final_size)
    nbt_file = File(nbt_root, gzipped=True, root_name="")
    nbt_file.save(os.path.join(STRUCT_NBT_DIR, shop["id"] + ".nbt"))

    write_structure_json(shop)
    write_pool_json(shop)
    write_structure_set_json(shop)
    write_loot_table(shop)

print(f"Generated {len(STRUCTURES)} structures.")
