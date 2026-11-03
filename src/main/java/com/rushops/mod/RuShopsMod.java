package com.rushops.mod;

import com.mojang.logging.LogUtils;
import net.minecraft.core.registries.Registries;
import net.minecraft.network.chat.Component;
import net.minecraft.world.item.CreativeModeTab;
import net.minecraft.world.item.CreativeModeTabs;
import net.minecraftforge.event.BuildCreativeModeTabContentsEvent;
import net.minecraftforge.fml.common.Mod;
import net.minecraftforge.fml.event.lifecycle.FMLCommonSetupEvent;
import net.minecraftforge.fml.javafmlmod.FMLJavaModLoadingContext;
import net.minecraftforge.registries.DeferredRegister;
import net.minecraftforge.registries.RegistryObject;
import org.slf4j.Logger;

/**
 * "Random Things from Russia" - adds 11 Russian retail-chain buildings as generated
 * Overworld structures (Fix Price, Pyaterochka, Yarche, Svetofor, DNS, Magnit, Detsky Mir,
 * street kiosks, SPAR, Lenta/Metro and Auchan), each with its own loot-filled chest, plus
 * dozens of themed items: food &amp; drinks, toys, electronics, spoiled goods, cosmetics and
 * household chemicals.
 */
@Mod(RuShopsMod.MODID)
public class RuShopsMod {
    public static final String MODID = "rushops";
    private static final Logger LOGGER = LogUtils.getLogger();

    public static final DeferredRegister<CreativeModeTab> CREATIVE_MODE_TABS =
            DeferredRegister.create(Registries.CREATIVE_MODE_TAB, MODID);

    public static final RegistryObject<CreativeModeTab> RUSHOPS_TAB = CREATIVE_MODE_TABS.register(
            "rushops_tab",
            () -> CreativeModeTab.builder()
                    .withTabsBefore(CreativeModeTabs.COMBAT)
                    .icon(() -> ModItems.TUSHONKA_CAN.get().getDefaultInstance())
                    .title(Component.translatable("itemGroup.rushops"))
                    .displayItems((parameters, output) -> {
                        for (RegistryObject<net.minecraft.world.item.Item> item : ModItems.ALL_ITEMS) {
                            output.accept(item.get());
                        }
                    })
                    .build());

    public RuShopsMod(FMLJavaModLoadingContext context) {
        var modEventBus = context.getModEventBus();

        ModItems.ITEMS.register(modEventBus);
        CREATIVE_MODE_TABS.register(modEventBus);

        modEventBus.addListener(this::commonSetup);
        modEventBus.addListener(this::addCreative);
    }

    private void commonSetup(final FMLCommonSetupEvent event) {
        LOGGER.info("Random Things from Russia loaded: {} items registered, 11 store structures ready to generate.",
                ModItems.ALL_ITEMS.size());
    }

    // Also slot a couple of our food items into the vanilla Food & Drinks tab for discoverability.
    private void addCreative(final BuildCreativeModeTabContentsEvent event) {
        if (event.getTabKey() == CreativeModeTabs.FOOD_AND_DRINKS) {
            event.accept(ModItems.KVASS_BOTTLE);
            event.accept(ModItems.TUSHONKA_CAN);
            event.accept(ModItems.SGUSHENKA_CAN);
        }
    }
}
