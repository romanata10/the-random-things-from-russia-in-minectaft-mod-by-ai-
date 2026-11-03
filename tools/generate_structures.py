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


def build_shop(shop):
    w, core_h, d = shop["size"]
    total_h = core_h + 1  # +1 extra empty layer on top to host the standalone sign
    rnd = random.Random(shop["id"])
    b = Builder(w, total_h, d)

    wall = "minecraft:" + shop["wall"]
    floor = "minecraft:" + shop["floor"]
    roof = "minecraft:" + shop["roof"]
    accent = "minecraft:" + shop["accent"]
    glass = "minecraft:" + shop["glass"]
    rundown = shop.get("rundown", False)

    # floor
    for x in range(w):
        for z in range(d):
            b.set(x, 0, z, floor)

    # walls
    wall_top = core_h - 1  # topmost wall row index (roof sits at core_h)
    for y in range(1, core_h):
        for x in range(w):
            for z in range(d):
                if is_perimeter(x, z, w, d):
                    block = wall
                    if rundown and rnd.random() < 0.18:
                        block = "minecraft:mossy_cobblestone"
                    b.set(x, y, z, block)

    # window band just below the roof
    window_y = max(1, core_h - 2)
    for x in range(w):
        for z in (0, d - 1):
            if 1 < x < w - 2 and x % 2 == 0:
                b.set(x, window_y, z, glass)
    for z in range(d):
        for x in (0, w - 1):
            if 1 < z < d - 2 and z % 2 == 0:
                b.set(x, window_y, z, glass)

    # doorway on the front wall (z = 0)
    door_h = min(3, core_h - 2) if core_h > 3 else core_h - 1
    door_h = max(2, door_h)
    cx = w // 2
    door_xs = [cx - 1, cx] if w >= 6 else [cx]
    for x in door_xs:
        for y in range(1, 1 + door_h):
            b.set(x, y, 0, "minecraft:air")

    # roof (flat, with a simple parapet trim on the edge)
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

    # sign standing on the roof parapet above the entrance
    sign_text = shop["ru"][:15]
    b.set(cx, core_h + 1, 0, "minecraft:oak_sign", {"rotation": "8", "waterlogged": "false"},
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

    return b, (w, total_h, d)


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
    builder, size = build_shop(shop)
    nbt_root = to_nbt(builder, size)
    nbt_file = File(nbt_root, gzipped=True, root_name="")
    nbt_file.save(os.path.join(STRUCT_NBT_DIR, shop["id"] + ".nbt"))

    write_structure_json(shop)
    write_pool_json(shop)
    write_structure_set_json(shop)
    write_loot_table(shop)

print(f"Generated {len(STRUCTURES)} structures.")
