"""Shared data tables describing every item and structure the mod adds.
Used by tools/generate_items.py and tools/generate_structures.py.
"""

# -----------------------------------------------------------------------
# ITEMS
# -----------------------------------------------------------------------
# category: food_drinks, toys, electronics, spoiled, cosmetics, chemicals, other
#
# food: None, or dict with:
#   nutrition (int), saturation (float), always_eat (bool),
#   effect: None or (effect_id, duration_ticks, amplifier, probability)
#
# stack: max stack size (default 64 if omitted)

ITEMS = [
    # ---------------- FOOD & DRINKS ----------------
    dict(id="kvass_bottle", en="Bottle of Kvass", ru="Бутылка кваса",
         category="food_drinks",
         food=dict(nutrition=3, saturation=0.4, always_eat=False, effect=None)),
    dict(id="kefir_carton", en="Carton of Kefir", ru="Пакет кефира",
         category="food_drinks",
         food=dict(nutrition=3, saturation=0.5, always_eat=False, effect=None)),
    dict(id="tushonka_can", en="Can of Tushonka", ru="Банка тушёнки",
         category="food_drinks",
         food=dict(nutrition=6, saturation=0.6, always_eat=False, effect=None)),
    dict(id="sgushenka_can", en="Can of Condensed Milk", ru="Банка сгущёнки",
         category="food_drinks",
         food=dict(nutrition=5, saturation=0.9, always_eat=False, effect=None)),
    dict(id="glazed_cheese_curd", en="Glazed Curd Snack", ru="Сырок глазированный",
         category="food_drinks",
         food=dict(nutrition=4, saturation=0.5, always_eat=False, effect=None)),
    dict(id="yarche_cookies", en="\"Yarche\" Shortbread Cookies", ru="Печенье «Ярче»",
         category="food_drinks",
         food=dict(nutrition=3, saturation=0.3, always_eat=False, effect=None)),
    dict(id="yarche_crackers", en="\"Yarche\" Rye Crackers", ru="Сухарики «Ярче»",
         category="food_drinks",
         food=dict(nutrition=2, saturation=0.2, always_eat=False, effect=None)),
    dict(id="fix_price_soda", en="Fix Price Budget Soda", ru="Газировка из Fix Price",
         category="food_drinks",
         food=dict(nutrition=2, saturation=0.3, always_eat=False, effect=None)),
    dict(id="pyaterochka_bread", en="\"Pyaterochka\" Loaf of Bread", ru="Хлеб из «Пятёрочки»",
         category="food_drinks",
         food=dict(nutrition=5, saturation=0.6, always_eat=False, effect=None)),
    dict(id="instant_noodles", en="Cup of Instant Noodles", ru="Лапша быстрого приготовления",
         category="food_drinks",
         food=dict(nutrition=6, saturation=0.4, always_eat=False, effect=None)),

    # ---------------- TOYS (Detsky Mir) ----------------
    dict(id="toy_car", en="Toy Car", ru="Игрушечная машинка", category="toys", food=None),
    dict(id="teddy_bear", en="Teddy Bear", ru="Плюшевый мишка", category="toys", food=None),
    dict(id="rubiks_cube", en="Puzzle Cube", ru="Кубик-головоломка", category="toys", food=None),
    dict(id="building_blocks_set", en="Building Blocks Set", ru="Набор конструктора", category="toys", food=None),

    # ---------------- ELECTRONICS (DNS) ----------------
    dict(id="smartphone", en="Smartphone", ru="Смартфон", category="electronics", food=None, stack=1),
    dict(id="laptop", en="Laptop", ru="Ноутбук", category="electronics", food=None, stack=1),
    dict(id="wireless_headphones", en="Wireless Headphones", ru="Беспроводные наушники", category="electronics", food=None, stack=1),
    dict(id="power_bank", en="Power Bank", ru="Повербанк", category="electronics", food=None, stack=1),

    # ---------------- SPOILED GOODS (Svetofor) ----------------
    dict(id="moldy_bread", en="Moldy Bread", ru="Заплесневелый хлеб",
         category="spoiled",
         food=dict(nutrition=2, saturation=0.1, always_eat=True,
                    effect=("minecraft:hunger", 600, 0, 0.85))),
    dict(id="rotten_sausage", en="Rotten Sausage", ru="Протухшая колбаса",
         category="spoiled",
         food=dict(nutrition=2, saturation=0.1, always_eat=True,
                    effect=("minecraft:poison", 100, 0, 0.6))),
    dict(id="expired_milk", en="Expired Milk", ru="Просроченное молоко",
         category="spoiled",
         food=dict(nutrition=1, saturation=0.1, always_eat=True,
                    effect=("minecraft:nausea", 200, 0, 0.5))),
    dict(id="spoiled_meat", en="Spoiled Meat", ru="Испорченное мясо",
         category="spoiled",
         food=dict(nutrition=2, saturation=0.1, always_eat=True,
                    effect=("minecraft:poison", 140, 1, 0.9))),

    # ---------------- COSMETICS / HYGIENE ----------------
    dict(id="shampoo_bottle", en="Shampoo Bottle", ru="Флакон шампуня", category="cosmetics", food=None),
    dict(id="soap_bar", en="Bar of Soap", ru="Кусок мыла", category="cosmetics", food=None),
    dict(id="toothpaste_tube", en="Tube of Toothpaste", ru="Тюбик зубной пасты", category="cosmetics", food=None),
    dict(id="perfume_bottle", en="Perfume Bottle", ru="Флакон парфюма", category="cosmetics", food=None),

    # ---------------- CHEMICALS ----------------
    dict(id="bleach_bottle", en="Bottle of Bleach", ru="Бутылка отбеливателя", category="chemicals", food=None),
    dict(id="washing_powder", en="Washing Powder Box", ru="Коробка стирального порошка", category="chemicals", food=None),
    dict(id="dish_soap", en="Dish Soap", ru="Средство для посуды", category="chemicals", food=None),
    dict(id="toilet_cleaner", en="Toilet Cleaner", ru="Чистящее средство", category="chemicals", food=None),

    # ---------------- OTHER STORE GOODS ----------------
    dict(id="shopping_cart_token", en="Shopping Cart Token", ru="Жетон от тележки", category="other", food=None, stack=16),
    dict(id="price_gun", en="Price Tag Gun", ru="Этикет-пистолет", category="other", food=None, stack=1),
    dict(id="cardboard_box", en="Cardboard Box", ru="Картонная коробка", category="other", food=None),
    dict(id="plastic_bag", en="Plastic Bag", ru="Полиэтиленовый пакет", category="other", food=None),
]

CATEGORY_LABEL_RU = {
    "food_drinks": "Еда и напитки",
    "toys": "Игрушки",
    "electronics": "Техника",
    "spoiled": "Тухлые продукты",
    "cosmetics": "Косметика и гигиена",
    "chemicals": "Бытовая химия",
    "other": "Прочие товары",
}

# -----------------------------------------------------------------------
# STRUCTURES (store buildings)
# -----------------------------------------------------------------------
# size: (width X, height Y, depth Z)
# palette: wall, floor, roof, accent, glass
# rundown: bool - adds cobwebs / cracked blocks / mossy patches
# loot: list of (item_id namespaced or "rushops:xxx", weight, min, max)
# spacing/separation: structure-set placement tuning
# salt: unique int

STRUCTURES = [
    dict(id="fix_price_store", en="Fix Price", ru="Fix Price",
         size=(9, 5, 7), wall="white_concrete", floor="light_gray_concrete",
         roof="red_concrete", accent="yellow_concrete", glass="glass_pane",
         rundown=False,
         loot=[("rushops:fix_price_soda", 10, 1, 3), ("rushops:cardboard_box", 8, 1, 2),
               ("rushops:plastic_bag", 8, 1, 3), ("rushops:toy_car", 4, 1, 1),
               ("rushops:soap_bar", 5, 1, 2), ("rushops:rubiks_cube", 3, 1, 1)],
         spacing=22, separation=9, salt=10021001),
    dict(id="pyaterochka_store", en="Pyaterochka", ru="Пятёрочка",
         size=(9, 5, 7), wall="orange_concrete", floor="white_concrete",
         roof="green_concrete", accent="white_concrete", glass="glass_pane",
         rundown=False,
         loot=[("rushops:pyaterochka_bread", 10, 1, 3), ("rushops:kefir_carton", 8, 1, 2),
               ("rushops:sgushenka_can", 6, 1, 2), ("rushops:instant_noodles", 8, 1, 3),
               ("rushops:tushonka_can", 5, 1, 2)],
         spacing=20, separation=8, salt=10021002),
    dict(id="yarche_store", en="Yarche", ru="Ярче",
         size=(10, 5, 8), wall="yellow_concrete", floor="light_blue_concrete",
         roof="blue_concrete", accent="white_concrete", glass="glass_pane",
         rundown=False,
         loot=[("rushops:yarche_cookies", 10, 1, 3), ("rushops:yarche_crackers", 10, 1, 3),
               ("rushops:kvass_bottle", 6, 1, 2), ("rushops:glazed_cheese_curd", 6, 1, 2)],
         spacing=26, separation=10, salt=10021003),
    dict(id="svetofor_store", en="Svetofor", ru="Светофор",
         size=(11, 5, 8), wall="cobblestone", floor="coarse_dirt",
         roof="red_terracotta", accent="yellow_terracotta", glass="cobweb",
         rundown=True,
         loot=[("rushops:moldy_bread", 10, 1, 2), ("rushops:rotten_sausage", 10, 1, 2),
               ("rushops:expired_milk", 8, 1, 2), ("rushops:spoiled_meat", 8, 1, 2),
               ("rushops:cardboard_box", 4, 1, 2)],
         spacing=30, separation=10, salt=10021004),
    dict(id="dns_store", en="DNS", ru="ДНС",
         size=(9, 6, 7), wall="black_concrete", floor="gray_concrete",
         roof="orange_concrete", accent="orange_concrete", glass="glass_pane",
         rundown=False,
         loot=[("rushops:smartphone", 6, 1, 1), ("rushops:laptop", 5, 1, 1),
               ("rushops:wireless_headphones", 8, 1, 1), ("rushops:power_bank", 7, 1, 2)],
         spacing=28, separation=10, salt=10021005),
    dict(id="magnit_store", en="Magnit", ru="Магнит",
         size=(9, 5, 7), wall="red_concrete", floor="white_concrete",
         roof="black_concrete", accent="white_concrete", glass="glass_pane",
         rundown=False,
         loot=[("rushops:kefir_carton", 8, 1, 2), ("rushops:tushonka_can", 8, 1, 2),
               ("rushops:sgushenka_can", 6, 1, 2), ("rushops:instant_noodles", 6, 1, 2),
               ("rushops:fix_price_soda", 5, 1, 2)],
         spacing=20, separation=8, salt=10021006),
    dict(id="detsky_mir_store", en="Detsky Mir", ru="Детский мир",
         size=(11, 6, 9), wall="pink_concrete", floor="light_blue_concrete",
         roof="purple_concrete", accent="yellow_concrete", glass="glass_pane",
         rundown=False,
         loot=[("rushops:toy_car", 10, 1, 2), ("rushops:teddy_bear", 10, 1, 1),
               ("rushops:rubiks_cube", 8, 1, 2), ("rushops:building_blocks_set", 8, 1, 1)],
         spacing=32, separation=10, salt=10021007),
    dict(id="street_kiosk", en="Street Kiosk", ru="Ларёк",
         size=(5, 4, 4), wall="gray_concrete", floor="stone_bricks",
         roof="green_concrete", accent="white_concrete", glass="glass_pane",
         rundown=False,
         loot=[("rushops:kvass_bottle", 8, 1, 2), ("rushops:glazed_cheese_curd", 8, 1, 2),
               ("rushops:cardboard_box", 5, 1, 1), ("rushops:plastic_bag", 5, 1, 2)],
         spacing=16, separation=6, salt=10021008),
    dict(id="spar_store", en="SPAR", ru="SPAR",
         size=(13, 6, 10), wall="white_terracotta", floor="smooth_stone",
         roof="green_concrete", accent="red_concrete", glass="glass_pane",
         rundown=False,
         loot=[("rushops:perfume_bottle", 6, 1, 1), ("rushops:shampoo_bottle", 6, 1, 1),
               ("rushops:toothpaste_tube", 6, 1, 1), ("rushops:sgushenka_can", 6, 1, 2),
               ("rushops:glazed_cheese_curd", 6, 1, 2)],
         spacing=34, separation=12, salt=10021009),
    dict(id="lenta_metro_store", en="Lenta / Metro Hypermarket", ru="Лента / Metro",
         size=(19, 8, 15), wall="light_gray_concrete", floor="gray_concrete",
         roof="gray_concrete", accent="blue_concrete", glass="glass_pane",
         rundown=False,
         loot=[("rushops:instant_noodles", 6, 1, 3), ("rushops:tushonka_can", 6, 1, 2),
               ("rushops:washing_powder", 6, 1, 2), ("rushops:bleach_bottle", 6, 1, 1),
               ("rushops:power_bank", 4, 1, 1), ("rushops:toy_car", 4, 1, 1),
               ("rushops:shopping_cart_token", 10, 1, 2)],
         spacing=46, separation=14, salt=10021010),
    dict(id="auchan_store", en="Auchan", ru="Ашан",
         size=(17, 7, 13), wall="red_concrete", floor="white_concrete",
         roof="red_concrete", accent="white_concrete", glass="glass_pane",
         rundown=False,
         loot=[("rushops:pyaterochka_bread", 5, 1, 2), ("rushops:kefir_carton", 5, 1, 2),
               ("rushops:toothpaste_tube", 5, 1, 1), ("rushops:dish_soap", 5, 1, 1),
               ("rushops:building_blocks_set", 4, 1, 1), ("rushops:shopping_cart_token", 10, 1, 2),
               ("rushops:price_gun", 3, 1, 1)],
         spacing=42, separation=14, salt=10021011),
]
