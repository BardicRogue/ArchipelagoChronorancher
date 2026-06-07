from __future__ import annotations

import math
from typing import TYPE_CHECKING
from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasAll, Rule, HasGroup
from . import world, locations

if TYPE_CHECKING:
    from .world import ChronoRancherWorld

def set_all_rules(world: ChronoRancherWorld) -> None:
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)

def set_all_entrance_rules(world : ChronoRancherWorld) :
    menu_to_fluff = world.get_entrance("Menu to Fluff")
    menu_to_spike = world.get_entrance("Menu to Spike")
    menu_to_blob = world.get_entrance("Menu to Blob")
    menu_to_brick = world.get_entrance("Menu to Brick")
    fluff_to_spike = world.get_entrance("Fluff to Spike")
    fluff_to_blob = world.get_entrance("Fluff to Blob")
    fluff_to_brick = world.get_entrance("Fluff to Brick")
    spike_to_blob = world.get_entrance("Spike to Blob")
    spike_to_brick = world.get_entrance("Spike to Brick")
    blob_to_brick = world.get_entrance("Blob to Brick")
    fluff_spike_to_blob = world.get_entrance("Fluff Spike to Blob")
    fluff_spike_to_brick = world.get_entrance("Fluff Spike to Brick")
    fluff_blob_to_brick = world.get_entrance("Fluff Blob to Brick")
    spike_blob_to_brick = world.get_entrance("Spike Blob to Brick")
    fluff_spike_blob_to_brick = world.get_entrance("Fluff Spike Blob to Brick")

    fluff = Has("Fluff")
    world.set_rule(menu_to_fluff, fluff)

    spike = Has("Spike")
    world.set_rule(menu_to_spike, spike)
    world.set_rule(fluff_to_spike, spike)

    blob = Has("Blob")
    world.set_rule(menu_to_blob, blob)
    world.set_rule(fluff_to_blob, blob)
    world.set_rule(spike_to_blob, blob)
    world.set_rule(fluff_spike_to_blob, blob)

    brick = Has("Brick")
    world.set_rule(menu_to_brick, brick)
    world.set_rule(fluff_to_brick, brick)
    world.set_rule(spike_to_brick, brick)
    world.set_rule(blob_to_brick, brick)
    world.set_rule(fluff_spike_to_brick, brick)
    world.set_rule(fluff_blob_to_brick, brick)
    world.set_rule(spike_blob_to_brick, brick)
    world.set_rule(fluff_spike_blob_to_brick, brick)

def set_all_location_rules(world : ChronoRancherWorld) -> None:
    #rules need to be set if there are locked levels
    if world.options.lock_levels == 1 :
        for i in range(1,31) :
            #ignores all tutorial levels
            if not i in locations.TUTORIAL_LEVELS :
                location_name = "Level " + str(i) + " Complete"
                level = world.get_location(location_name)
                unlock_name = "Level " + str(i) + " Unlock"
                unlock = Has(unlock_name)
                world.set_rule(level, unlock)
                event_level_name = "Completed Level " + str(i)
                event_level = world.get_location(event_level_name)
                world.set_rule(event_level, unlock)
    #currently locks all key levels
    elif world.options.lock_levels >= 2 :
        for i in range(1,31) :
            if i in locations.KEY_LEVELS :
                location_name = "Level " + str(i) + " Complete"
                level = world.get_location(location_name)
                unlock_name = "Level " + str(i) + " Unlock"
                unlock = Has(unlock_name)
                world.set_rule(level, unlock)
                event_level_name = "Completed Level " + str(i)
                event_level = world.get_location(event_level_name)
                world.set_rule(event_level, unlock)

def set_completion_condition(world : ChronoRancherWorld) -> None:
    if world.options.victory_condition == 0 :
        percent_levels_needed = world.options.goal_level_percent
        levels_needed = math.floor(percent_levels_needed * 30 / 100)
        enough_levels_completed = Has("Level Completed", count=levels_needed)
        world.set_completion_rule(enough_levels_completed)
    else :
        #don't yet have a way to implement the other victory condition
        pass
