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
    # get squeak entrances
    menu_to_squeak = world.get_entrance("Menu to Squeak")
    fluff_to_squeak = world.get_entrance("Fluff to Squeak")
    spike_to_squeak = world.get_entrance("Spike to Squeak")
    blob_to_squeak  = world.get_entrance("Blob to Squeak")
    brick_to_squeak = world.get_entrance("Brick to Squeak")
    fluff_spike_to_squeak = world.get_entrance("Fluff Spike to Squeak")
    fluff_blob_to_squeak = world.get_entrance("Fluff Blob to Squeak")
    fluff_brick_to_squeak = world.get_entrance("Fluff Brick to Squeak")
    spike_blob_to_squeak = world.get_entrance("Spike Blob to Squeak")
    spike_brick_to_squeak = world.get_entrance("Spike Brick to Squeak")
    blob_brick_to_squeak = world.get_entrance("Blob Brick to Squeak")
    fluff_spike_blob_to_squeak = world.get_entrance("Fluff Spike Blob to Squeak")
    fluff_spike_brick_to_squeak = world.get_entrance("Fluff Spike Brick to Squeak")
    fluff_blob_brick_to_squeak = world.get_entrance("Fluff Blob Brick to Squeak")
    spike_blob_brick_to_squeak = world.get_entrance("Spike Blob Brick to Squeak")
    fluff_spike_blob_brick_to_squeak = world.get_entrance("Fluff Spike Blob Brick to Squeak")

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

    squeak = Has("Squeak")
    world.set_rule(menu_to_squeak, squeak)
    world.set_rule(fluff_to_squeak, squeak)
    world.set_rule(spike_to_squeak, squeak)
    world.set_rule(blob_to_squeak, squeak)
    world.set_rule(brick_to_squeak, squeak)
    world.set_rule(fluff_spike_to_squeak, squeak)
    world.set_rule(fluff_blob_to_squeak, squeak)
    world.set_rule(fluff_brick_to_squeak, squeak)
    world.set_rule(spike_blob_to_squeak, squeak)
    world.set_rule(spike_brick_to_squeak, squeak)
    world.set_rule(blob_brick_to_squeak, squeak)
    world.set_rule(fluff_spike_blob_to_squeak, squeak)
    world.set_rule(fluff_spike_brick_to_squeak, squeak)
    world.set_rule(fluff_blob_brick_to_squeak, squeak)
    world.set_rule(spike_blob_brick_to_squeak, squeak)
    world.set_rule(fluff_spike_blob_brick_to_squeak, squeak)

def set_all_location_rules(world : ChronoRancherWorld) -> None:
    #rules need to be set if there are locked levels
    if world.options.lock_levels == 1 :
        for i in range(1,41) :
            #ignores all tutorial levels
            if not i in locations.TUTORIAL_LEVELS :
                location_name = "Level " + str(i) + " Complete"
                level = world.get_location(location_name)
                unlock_name = "Level " + str(i) + " Unlock"
                unlock = Has(unlock_name)
                world.set_rule(level, unlock)
                event_level_name = "Completed Level " + str(i)
                key_level_name = "Level " + str(i)
                if world.options.victory_condition == 0 :
                    event_level = world.get_location(event_level_name)
                    world.set_rule(event_level, unlock)
                #if playing for percent levels, only checks key levels
                elif key_level_name in world.options.key_levels_to_beat :
                    event_level = world.get_location(event_level_name)
                    world.set_rule(event_level, unlock)
    #currently locks all key levels
    elif world.options.lock_levels == 2 :
        for i in range(1,41) :
            if i in locations.KEY_LEVELS :
                location_name = "Level " + str(i) + " Complete"
                level = world.get_location(location_name)
                unlock_name = "Level " + str(i) + " Unlock"
                unlock = Has(unlock_name)
                world.set_rule(level, unlock)
                event_level_name = "Completed Level " + str(i)
                event_level = world.get_location(event_level_name)
                world.set_rule(event_level, unlock)
    elif world.options.lock_levels == 3 :
        if "All" in world.options.key_levels_to_beat or len(world.options.key_levels_to_beat.value) == 0:
            for x in locations.KEY_LEVELS:
                location_name = "Level " + str(x) + " Complete"
                level = world.get_location(location_name)
                unlock_name = "Level " + str(x) + " Unlock"
                unlock = Has(unlock_name)
                world.set_rule(level, unlock)
                event_level_name = "Completed Level " + str(x)
                event_level = world.get_location(event_level_name)
                world.set_rule(event_level, unlock)
        else :
            for lvl in world.options.key_levels_to_beat.value:
                location_name = lvl + " Complete"
                level = world.get_location(location_name)
                unlock_name = lvl + " Unlock"
                unlock = Has(unlock_name)
                world.set_rule(level, unlock)
                event_level_name = "Completed " + lvl
                event_level = world.get_location(event_level_name)
                world.set_rule(event_level, unlock)


def set_completion_condition(world : ChronoRancherWorld) -> None:
    if world.options.victory_condition == 0 :
        percent_levels_needed = world.options.goal_level_percent
        levels_needed = math.ceil(percent_levels_needed * 40 / 100)
        enough_levels_completed = Has("Level Completed", count=levels_needed)
        world.set_completion_rule(enough_levels_completed)
    else :
        levels_to_beat = world.options.key_levels_to_beat
        #if empty, the player will be given the 'All' option
        if len(levels_to_beat.value) == 0 :
            levels_to_beat = frozenset("All")
        key_levels = []
        if "All" in levels_to_beat :
            levels = []
            for lvl in locations.KEY_LEVELS :
                level_name = "Level " + str(lvl) + " Complete"
                levels.append(level_name)
            key_levels = levels
        else :
            for lvl in levels_to_beat :
                level_name = lvl + " Complete"
                key_levels.append(level_name)
        num_levels_to_beat = world.options.num_key_levels
        if num_levels_to_beat == 0 :
            num_levels_to_beat = len(key_levels)
        num_levels_to_beat = min(num_levels_to_beat, len(key_levels))
        #compare the number of levels to beat with the number of levels beaten
        enough_levels_completed = Has("Level Completed", count=num_levels_to_beat)
        world.set_completion_rule(enough_levels_completed)

        #don't yet have a way to implement the other victory condition
        pass
