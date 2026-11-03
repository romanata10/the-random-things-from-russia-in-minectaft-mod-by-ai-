# The Random Things From Russia (Minecraft mod, by AI)

A Minecraft **Forge 1.20.1** mod that scatters 11 Russian retail-chain buildings around the
Overworld as generated structures, each stocked with a loot chest full of themed items -
food & drinks, toys, electronics, spoiled goods, cosmetics and household chemicals.

This is an unofficial fan/parody project built entirely out of vanilla blocks. It is not
affiliated with or endorsed by any of the real brands referenced.

## ⬇️ Download

Every push to this branch is automatically compiled by GitHub Actions (see
`.github/workflows/build.yml`). Grab the built jar from:

- **Releases → [`latest`](../../releases/tag/latest)** - always the newest automated build, or
- **Actions tab → latest successful run → Artifacts → `rushops-mod-jar`**

Requires **Minecraft 1.20.1** + **Minecraft Forge 47.x** (recommended `47.4.28`).
Drop the jar into your `.minecraft/mods` folder.

> Why isn't the jar committed straight into the repo? This sandbox environment has no
> network access to the Minecraft/Forge/Mojang servers that Gradle needs to compile the mod
> (only GitHub, npm and PyPI are reachable here), so the jar is built by GitHub Actions
> instead, which does have full internet access. The full, buildable source code lives in
> this repo either way.

## 🏬 Structures (11)

Each one is a standalone building made of vanilla blocks, with its own sign, windows,
shelving and a loot chest, generated naturally while exploring the Overworld
(plains / forest / savanna-type biomes; rarity controlled per store):

| # | Store | Flavor |
|---|-------|--------|
| 1 | **Fix Price** | Small budget shop, often found on a mall's 2nd floor - here a standalone red & white box |
| 2 | **Пятёрочка (Pyaterochka)** | Small neighbourhood grocery store |
| 3 | **Ярче (Yarche)** | Siberian discount chain (Yashkino/Kireshki-style snacks) |
| 4 | **Светофор (Svetofor)** | Run-down, out-of-town store - mossy blocks, cobwebs, spoiled loot |
| 5 | **ДНС (DNS)** | Electronics store |
| 6 | **Магнит (Magnit)** | Neighbourhood grocery store |
| 7 | **Детский мир (Detsky Mir)** | Colourful toy & kids' clothes store |
| 8 | **Street Kiosk / Ларёк** | Tiny standalone newspaper/snack kiosk |
| 9 | **SPAR** | Larger, higher-quality supermarket |
| 10 | **Лента / Metro** | Big-box hypermarket/warehouse store |
| 11 | **Ашан (Auchan)** | Large anchor-store building |

Each has a unique size, block palette and loot table (see
`src/main/resources/data/rushops/loot_tables/chests/`).

## 🛒 Items (34)

| Category | Examples |
|---|---|
| Food & drinks | Kvass, kefir, tushonka, condensed milk, glazed curd snack, Yarche cookies/crackers, budget soda, bread, instant noodles |
| Toys | Toy car, teddy bear, puzzle cube, building blocks set |
| Electronics | Smartphone, laptop, wireless headphones, power bank |
| Spoiled goods | Moldy bread, rotten sausage, expired milk, spoiled meat (eating them triggers hunger/poison/nausea, like vanilla rotten flesh) |
| Cosmetics / hygiene | Shampoo, soap, toothpaste, perfume |
| Household chemicals | Bleach, washing powder, dish soap, toilet cleaner |
| Other store goods | Shopping cart token, price tag gun, cardboard box, plastic bag |

All items are registered in `com.rushops.mod.ModItems` and collected into a dedicated
**"Магазины России / Russia Shops"** creative inventory tab.

## 🛠️ Building locally

You need a machine with internet access to Mojang/Forge's servers (this sandbox does not
have that, which is why it relies on CI - see above).

```bash
git clone <this repo> rushops
cd rushops
./gradlew build
```

The compiled jar will appear in `build/libs/`. Use `./gradlew runClient` to launch a dev
client straight away.

## 📁 Project layout

- `src/main/java/com/rushops/mod/` - mod source (`RuShopsMod`, `ModItems`)
- `src/main/resources/assets/rushops/` - item models, textures, `en_us`/`ru_ru` lang
- `src/main/resources/data/rushops/` - structures (`.nbt`), structure/structure_set/template_pool
  world-gen definitions, chest loot tables
- `tools/` - the Python generators (`mod_data.py`, `generate_items.py`,
  `generate_structures.py`, `placeholder_icons.py`) used to produce the above resources
  from a single data table, so content can be tweaked/extended by editing `tools/mod_data.py`
  and re-running the two generator scripts.

## License

MIT - see [LICENSE](LICENSE).
