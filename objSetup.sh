#!/bin/bash

# Non-descriptive name. So what?
_() {
    screen -p 0 -S "Minecraft" -X eval "stuff \'scoreboard objectives add $1\'\015"
}

#_ "say script test: $1"

# Stats. linears
_ "animalsBred stat.animalsBred"
_ "boatOneCm stat.boatOneCm"
_ "climbOneCm stat.climbOneCm"
_ "crouchOneCm stat.crouchOneCm"
_ "damageDealt stat.damageDealt"
_ "damageTaken stat.damageTaken"
_ "deaths stat.deaths"
_ "diveOneCm stat.diveOneCm"
_ "drop stat.drop"
_ "fishCaught stat.fishCaught"
_ "flyOneCm stat.flyOneCm"
_ "horseOneCm stat.horseOneCm"
_ "jump stat.jump"
_ "fallOneCm stat.fallOneCm"
_ "junkFished stat.junkFished" 
_ "ReaveGame stat.leaveGame"
_ "rinecartOneCm stat.minecartOneCm"
_ "mobKills stat.mobKills"
_ "pigOneCm stat.pigOneCm"
_ "playerKills stat.playerKills"
_ "playOneMinute stat.playOneMinute"
_ "sprintOneCm stat.sprintOneCm"
_ "swimOneCm stat.swimOneCm"
_ "talkedToVillager stat.talkedToVillager"
_ "tradedWVillager stat.tradedWithVillager"
_ "treasureFished stat.treasureFished"
_ "walkOneCm stat.walkOneCm"

# Crafting
_ "craftAnvil stat.craftItem.minecraft.anvil"
_ "craftBeacon stat.craftItem.minecraft.beacon"
_ "craftBrewStand stat.craftItem.minecraft.brewing_stand"
_ "craftCake stat.craftItem.minecraft.cake"
_ "craftJukebox stat.craftItem.minecraft.jukebox"

# Using
# Redstone stuff
_ "useActivRail stat.useItem.minecraft.activator_rail"
_ "useComparator stat.useItem.minecraft.comparator"
_ "useDetector_Rail stat.useItem.minecraft.detector_rail"
_ "useDispenser stat.useItem.minecraft.dispenser"
_ "useDropper stat.useItem.minecraft.dropper"
_ "useLever stat.useItem.minecraft.lever"
_ "useNoteblock stat.useItem.minecraft.noteblock"
_ "usePiston stat.useItem.minecraft.piston"
_ "useRepeater stat.useItem.minecraft.repeater"
_ "useStone_PP stat.useItem.minecraft.stone_pressure_plate"
_ "useWooden_PP stat.useItem.minecraft.wooden_pressure_plate"

# Mining stuff
_ "mineNetherrack stat.mineBlock.minecraft.netherrack"
_ "mineDirt stat.mineBlock.minecraft.dirt"
_ "mineSand stat.mineBlock.minecraft.sand"
_ "mineNether_Brick stat.mineBlock.minecraft.nether_brick"
_ "mineSandstone stat.mineBlock.minecraft.sandstone"
_ "mineCobblestone stat.mineBlock.minecraft.cobblestone"
_ "mineStone stat.mineBlock.minecraft.stone"
_ "mineMossCob stat.mineBlock.minecraft.mossy_cobblestone"
_ "mineQuartz_Ore stat.mineBlock.minecraft.quartz_ore"
_ "mineIron_Ore stat.mineBlock.minecraft.iron_ore"
_ "mineGold_Ore stat.mineBlock.minecraft.gold_ore"
_ "mineRedstone_Ore stat.mineBlock.minecraft.redstone_ore"
_ "mineLapis_Ore stat.mineBlock.minecraft.lapis_ore"
_ "mineDiamond_Ore stat.mineBlock.minecraft.diamond_ore"
_ "mineObsidian stat.mineBlock.minecraft.obsidian"


