package com.rushops.mod;

import net.minecraft.world.effect.MobEffectInstance;
import net.minecraft.world.effect.MobEffects;
import net.minecraft.world.food.FoodProperties;
import net.minecraft.world.item.Item;
import net.minecraftforge.registries.DeferredRegister;
import net.minecraftforge.registries.ForgeRegistries;
import net.minecraftforge.registries.RegistryObject;

import java.util.ArrayList;
import java.util.List;
import java.util.function.Supplier;

/**
 * All items added by the mod. Generated from tools/mod_data.py - see tools/generate_items.py.
 */
public class ModItems {
    public static final DeferredRegister<Item> ITEMS = DeferredRegister.create(ForgeRegistries.ITEMS, RuShopsMod.MODID);

    // Keep a list of every item we register so the creative tab can show all of them in order.
    public static final List<RegistryObject<Item>> ALL_ITEMS = new ArrayList<>();

    public static final RegistryObject<Item> KVASS_BOTTLE = register("kvass_bottle", () -> new Item(new Item.Properties().food(new FoodProperties.Builder().nutrition(3).saturationMod(0.4f).build())));
    public static final RegistryObject<Item> KEFIR_CARTON = register("kefir_carton", () -> new Item(new Item.Properties().food(new FoodProperties.Builder().nutrition(3).saturationMod(0.5f).build())));
    public static final RegistryObject<Item> TUSHONKA_CAN = register("tushonka_can", () -> new Item(new Item.Properties().food(new FoodProperties.Builder().nutrition(6).saturationMod(0.6f).build())));
    public static final RegistryObject<Item> SGUSHENKA_CAN = register("sgushenka_can", () -> new Item(new Item.Properties().food(new FoodProperties.Builder().nutrition(5).saturationMod(0.9f).build())));
    public static final RegistryObject<Item> GLAZED_CHEESE_CURD = register("glazed_cheese_curd", () -> new Item(new Item.Properties().food(new FoodProperties.Builder().nutrition(4).saturationMod(0.5f).build())));
    public static final RegistryObject<Item> YARCHE_COOKIES = register("yarche_cookies", () -> new Item(new Item.Properties().food(new FoodProperties.Builder().nutrition(3).saturationMod(0.3f).build())));
    public static final RegistryObject<Item> YARCHE_CRACKERS = register("yarche_crackers", () -> new Item(new Item.Properties().food(new FoodProperties.Builder().nutrition(2).saturationMod(0.2f).build())));
    public static final RegistryObject<Item> FIX_PRICE_SODA = register("fix_price_soda", () -> new Item(new Item.Properties().food(new FoodProperties.Builder().nutrition(2).saturationMod(0.3f).build())));
    public static final RegistryObject<Item> PYATEROCHKA_BREAD = register("pyaterochka_bread", () -> new Item(new Item.Properties().food(new FoodProperties.Builder().nutrition(5).saturationMod(0.6f).build())));
    public static final RegistryObject<Item> INSTANT_NOODLES = register("instant_noodles", () -> new Item(new Item.Properties().food(new FoodProperties.Builder().nutrition(6).saturationMod(0.4f).build())));
    public static final RegistryObject<Item> PELMENI_PACK = register("pelmeni_pack", () -> new Item(new Item.Properties().food(new FoodProperties.Builder().nutrition(6).saturationMod(0.7f).build())));
    public static final RegistryObject<Item> MAYONNAISE_JAR = register("mayonnaise_jar", () -> new Item(new Item.Properties().food(new FoodProperties.Builder().nutrition(3).saturationMod(0.8f).build())));
    public static final RegistryObject<Item> SUNFLOWER_SEEDS_PACK = register("sunflower_seeds_pack", () -> new Item(new Item.Properties().food(new FoodProperties.Builder().nutrition(2).saturationMod(0.3f).alwaysEat().build())));
    public static final RegistryObject<Item> SUSHKI_PACK = register("sushki_pack", () -> new Item(new Item.Properties().food(new FoodProperties.Builder().nutrition(3).saturationMod(0.3f).build())));
    public static final RegistryObject<Item> PRYANIKI_PACK = register("pryaniki_pack", () -> new Item(new Item.Properties().food(new FoodProperties.Builder().nutrition(4).saturationMod(0.5f).build())));
    public static final RegistryObject<Item> SALO_PIECE = register("salo_piece", () -> new Item(new Item.Properties().food(new FoodProperties.Builder().nutrition(5).saturationMod(0.9f).build())));
    public static final RegistryObject<Item> TOY_CAR = register("toy_car", () -> new Item(new Item.Properties()));
    public static final RegistryObject<Item> TEDDY_BEAR = register("teddy_bear", () -> new Item(new Item.Properties()));
    public static final RegistryObject<Item> RUBIKS_CUBE = register("rubiks_cube", () -> new Item(new Item.Properties()));
    public static final RegistryObject<Item> BUILDING_BLOCKS_SET = register("building_blocks_set", () -> new Item(new Item.Properties()));
    public static final RegistryObject<Item> SMARTPHONE = register("smartphone", () -> new Item(new Item.Properties().stacksTo(1)));
    public static final RegistryObject<Item> LAPTOP = register("laptop", () -> new Item(new Item.Properties().stacksTo(1)));
    public static final RegistryObject<Item> WIRELESS_HEADPHONES = register("wireless_headphones", () -> new Item(new Item.Properties().stacksTo(1)));
    public static final RegistryObject<Item> POWER_BANK = register("power_bank", () -> new Item(new Item.Properties().stacksTo(1)));
    public static final RegistryObject<Item> MOLDY_BREAD = register("moldy_bread", () -> new Item(new Item.Properties().food(new FoodProperties.Builder().nutrition(2).saturationMod(0.1f).alwaysEat().effect(() -> new MobEffectInstance(MobEffects.HUNGER, 600, 0), 0.85f).build())));
    public static final RegistryObject<Item> ROTTEN_SAUSAGE = register("rotten_sausage", () -> new Item(new Item.Properties().food(new FoodProperties.Builder().nutrition(2).saturationMod(0.1f).alwaysEat().effect(() -> new MobEffectInstance(MobEffects.POISON, 100, 0), 0.6f).build())));
    public static final RegistryObject<Item> EXPIRED_MILK = register("expired_milk", () -> new Item(new Item.Properties().food(new FoodProperties.Builder().nutrition(1).saturationMod(0.1f).alwaysEat().effect(() -> new MobEffectInstance(MobEffects.CONFUSION, 200, 0), 0.5f).build())));
    public static final RegistryObject<Item> SPOILED_MEAT = register("spoiled_meat", () -> new Item(new Item.Properties().food(new FoodProperties.Builder().nutrition(2).saturationMod(0.1f).alwaysEat().effect(() -> new MobEffectInstance(MobEffects.POISON, 140, 1), 0.9f).build())));
    public static final RegistryObject<Item> SHAMPOO_BOTTLE = register("shampoo_bottle", () -> new Item(new Item.Properties()));
    public static final RegistryObject<Item> SOAP_BAR = register("soap_bar", () -> new Item(new Item.Properties()));
    public static final RegistryObject<Item> TOOTHPASTE_TUBE = register("toothpaste_tube", () -> new Item(new Item.Properties()));
    public static final RegistryObject<Item> PERFUME_BOTTLE = register("perfume_bottle", () -> new Item(new Item.Properties()));
    public static final RegistryObject<Item> BLEACH_BOTTLE = register("bleach_bottle", () -> new Item(new Item.Properties()));
    public static final RegistryObject<Item> WASHING_POWDER = register("washing_powder", () -> new Item(new Item.Properties()));
    public static final RegistryObject<Item> DISH_SOAP = register("dish_soap", () -> new Item(new Item.Properties()));
    public static final RegistryObject<Item> TOILET_CLEANER = register("toilet_cleaner", () -> new Item(new Item.Properties()));
    public static final RegistryObject<Item> SHOPPING_CART_TOKEN = register("shopping_cart_token", () -> new Item(new Item.Properties().stacksTo(16)));
    public static final RegistryObject<Item> PRICE_GUN = register("price_gun", () -> new Item(new Item.Properties().stacksTo(1)));
    public static final RegistryObject<Item> CARDBOARD_BOX = register("cardboard_box", () -> new Item(new Item.Properties()));
    public static final RegistryObject<Item> PLASTIC_BAG = register("plastic_bag", () -> new Item(new Item.Properties()));

    private static RegistryObject<Item> register(String name, Supplier<Item> supplier) {
        RegistryObject<Item> item = ITEMS.register(name, supplier);
        ALL_ITEMS.add(item);
        return item;
    }
}
