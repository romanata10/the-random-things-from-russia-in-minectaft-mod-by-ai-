import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from mod_data import ITEMS, CATEGORY_LABEL_RU

ROOT = os.path.join(os.path.dirname(__file__), "..")
JAVA_DIR = os.path.join(ROOT, "src/main/java/com/rushops/mod")
ASSETS_DIR = os.path.join(ROOT, "src/main/resources/assets/rushops")

os.makedirs(JAVA_DIR, exist_ok=True)
os.makedirs(os.path.join(ASSETS_DIR, "models/item"), exist_ok=True)
os.makedirs(os.path.join(ASSETS_DIR, "lang"), exist_ok=True)
os.makedirs(os.path.join(ASSETS_DIR, "textures/item"), exist_ok=True)

EFFECT_FIELD = {
    "minecraft:hunger": "MobEffects.HUNGER",
    "minecraft:poison": "MobEffects.POISON",
    "minecraft:nausea": "MobEffects.CONFUSION",
}


def camel(item_id):
    return "".join(p.capitalize() for p in item_id.split("_"))


def java_field(item_id):
    return item_id.upper()


lines = []
lines.append("package com.rushops.mod;")
lines.append("")
lines.append("import net.minecraft.world.effect.MobEffectInstance;")
lines.append("import net.minecraft.world.effect.MobEffects;")
lines.append("import net.minecraft.world.food.FoodProperties;")
lines.append("import net.minecraft.world.item.Item;")
lines.append("import net.minecraftforge.registries.DeferredRegister;")
lines.append("import net.minecraftforge.registries.ForgeRegistries;")
lines.append("import net.minecraftforge.registries.RegistryObject;")
lines.append("")
lines.append("import java.util.ArrayList;")
lines.append("import java.util.List;")
lines.append("import java.util.function.Supplier;")
lines.append("")
lines.append("/**")
lines.append(" * All items added by the mod. Generated from tools/mod_data.py - see tools/generate_items.py.")
lines.append(" */")
lines.append("public class ModItems {")
lines.append(f"    public static final DeferredRegister<Item> ITEMS = DeferredRegister.create(ForgeRegistries.ITEMS, RuShopsMod.MODID);")
lines.append("")
lines.append("    // Keep a list of every item we register so the creative tab can show all of them in order.")
lines.append("    public static final List<RegistryObject<Item>> ALL_ITEMS = new ArrayList<>();")
lines.append("")

for it in ITEMS:
    item_id = it["id"]
    food = it.get("food")
    stack = it.get("stack")
    props_parts = []
    if stack:
        props_parts.append(f".stacksTo({stack})")
    if food:
        builder = "new FoodProperties.Builder()"
        builder += f".nutrition({food['nutrition']}).saturationMod({food['saturation']}f)"
        if food.get("always_eat"):
            builder += ".alwaysEat()"
        if food.get("effect"):
            eff_id, duration, amplifier, probability = food["effect"]
            eff_field = EFFECT_FIELD[eff_id]
            builder += f".effect(() -> new MobEffectInstance({eff_field}, {duration}, {amplifier}), {probability}f)"
        builder += ".build()"
        props_parts.append(f".food({builder})")
    props = "new Item.Properties()" + "".join(props_parts)
    field = java_field(item_id)
    lines.append(f'    public static final RegistryObject<Item> {field} = register("{item_id}", () -> new Item({props}));')

lines.append("")
lines.append("    private static RegistryObject<Item> register(String name, Supplier<Item> supplier) {")
lines.append("        RegistryObject<Item> item = ITEMS.register(name, supplier);")
lines.append("        ALL_ITEMS.add(item);")
lines.append("        return item;")
lines.append("    }")
lines.append("}")

with open(os.path.join(JAVA_DIR, "ModItems.java"), "w") as f:
    f.write("\n".join(lines) + "\n")

# ---------------- item models ----------------
for it in ITEMS:
    model = {
        "parent": "minecraft:item/generated",
        "textures": {"layer0": f"rushops:item/{it['id']}"},
    }
    with open(os.path.join(ASSETS_DIR, "models/item", it["id"] + ".json"), "w") as f:
        json.dump(model, f, indent=2, ensure_ascii=False)
        f.write("\n")

# ---------------- lang ----------------
en_path = os.path.join(ASSETS_DIR, "lang/en_us.json")
ru_path = os.path.join(ASSETS_DIR, "lang/ru_ru.json")
en = json.load(open(en_path)) if os.path.exists(en_path) else {}
ru = json.load(open(ru_path)) if os.path.exists(ru_path) else {}

for it in ITEMS:
    en[f"item.rushops.{it['id']}"] = it["en"]
    ru[f"item.rushops.{it['id']}"] = it["ru"]

with open(en_path, "w") as f:
    json.dump(en, f, indent=2, ensure_ascii=False, sort_keys=True)
    f.write("\n")
with open(ru_path, "w") as f:
    json.dump(ru, f, indent=2, ensure_ascii=False, sort_keys=True)
    f.write("\n")

print(f"Generated {len(ITEMS)} items.")
