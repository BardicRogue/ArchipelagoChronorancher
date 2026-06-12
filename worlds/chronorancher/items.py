from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

from . import locations
if TYPE_CHECKING:
    from .world import ChronoRancherWorld

#level unlocks start at 1
#Critter unlocks start at 100
#Filler start at 200
#Traps start at 300
ITEM_NAME_TO_ID = {
    #"Level 1 Unlock": 1 #Levels 1-6, 15, 21 are tutorials, so they don't have unlock items
    #"Level 2 Unlock": 2
    #"Level 3 Unlock": 3
    #"Level 4 Unlock": 4
    #"Level 5 Unlock": 5
    #"Level 6 Unlock": 6,
    "Level 7 Unlock": 7,
    "Level 8 Unlock": 8,
    "Level 9 Unlock": 9,
    "Level 10 Unlock": 10,
    "Level 11 Unlock": 11,
    "Level 12 Unlock": 12,
    "Level 13 Unlock": 13,
    "Level 14 Unlock": 14,
    #"Level 15 Unlock": 15
    "Level 16 Unlock": 16,
    "Level 17 Unlock": 17,
    "Level 18 Unlock": 18,
    "Level 19 Unlock": 19,
    "Level 20 Unlock": 20,
    #"Level 21 Unlock": 21
    "Level 22 Unlock": 22,
    "Level 23 Unlock": 23,
    "Level 24 Unlock": 24,
    "Level 25 Unlock": 25,
    "Level 26 Unlock": 26,
    "Level 27 Unlock": 27,
    "Level 28 Unlock": 28,
    "Level 29 Unlock": 29,
    "Level 30 Unlock": 30,
    "Fluff": 101,
    "Spike": 102,
    "Blob": 103,
    "Brick": 104,
    "Chrono-Rancher Bestiary": 200,
    "Fluff Bestiary": 201,
    "Spike Bestiary": 202,
    "Blob Bestiary": 203,
    "Brick Bestiary": 204,
    "Congratulatory Critter": 300,
    "Undo Trap": 400,
    "Inverted Controls Trap": 401
}


DEFAULT_ITEM_CLASSIFICATIONS = {
    #"Level 6 Unlock": ItemClassification.progression,
    "Level 7 Unlock": ItemClassification.progression,
    "Level 8 Unlock": ItemClassification.progression,
    "Level 9 Unlock": ItemClassification.progression,
    "Level 10 Unlock": ItemClassification.progression,
    "Level 11 Unlock": ItemClassification.progression,
    "Level 12 Unlock": ItemClassification.progression,
    "Level 13 Unlock": ItemClassification.progression,
    "Level 14 Unlock": ItemClassification.progression,
    #"Level 15 Unlock": 15
    "Level 16 Unlock": ItemClassification.progression,
    "Level 17 Unlock": ItemClassification.progression,
    "Level 18 Unlock": ItemClassification.progression,
    "Level 19 Unlock": ItemClassification.progression,
    "Level 20 Unlock": ItemClassification.progression,
    #"Level 21 Unlock": 21
    "Level 22 Unlock": ItemClassification.progression,
    "Level 23 Unlock": ItemClassification.progression,
    "Level 24 Unlock": ItemClassification.progression,
    "Level 25 Unlock": ItemClassification.progression,
    "Level 26 Unlock": ItemClassification.progression,
    "Level 27 Unlock": ItemClassification.progression,
    "Level 28 Unlock": ItemClassification.progression,
    "Level 29 Unlock": ItemClassification.progression,
    "Level 30 Unlock": ItemClassification.progression,
    "Fluff": ItemClassification.progression,
    "Spike": ItemClassification.progression,
    "Blob": ItemClassification.progression,
    "Brick": ItemClassification.progression,
    "Chrono-Rancher Bestiary": ItemClassification.filler,
    "Fluff Bestiary": ItemClassification.filler,
    "Spike Bestiary": ItemClassification.filler,
    "Blob Bestiary": ItemClassification.filler,
    "Brick Bestiary": ItemClassification.filler,
    "Congratulatory Critter": ItemClassification.filler,
    "Undo Trap": ItemClassification.trap,
    "Inverted Controls Trap": ItemClassification.trap
}

item_name_groups = {
    "Level Unlock" : {
        "Level 7 Unlock",
        "Level 8 Unlock",
        "Level 9 Unlock",
        "Level 10 Unlock",
        "Level 11 Unlock",
        "Level 12 Unlock",
        "Level 13 Unlock",
        "Level 14 Unlock",
        "Level 16 Unlock",
        "Level 17 Unlock",
        "Level 18 Unlock",
        "Level 19 Unlock",
        "Level 20 Unlock",
        "Level 22 Unlock",
        "Level 23 Unlock",
        "Level 24 Unlock",
        "Level 25 Unlock",
        "Level 27 Unlock",
        "Level 28 Unlock",
        "Level 29 Unlock",
        "Level 30 Unlock"
    },
    "Key Level Unlock" : {
        "Level 20 Unlock",
        "Level 30 Unlock"
    },
    "Bestiary" : {
        "Chrono-Rancher Bestiary",
        "Fluff Bestiary",
        "Spike Bestiary",
        "Blob Bestiary",
        "Brick Bestiary"
    }
}


class ChronoRancherItem(Item):
    game = "The Chrono-Rancher"



def get_random_filler_item_name(world: ChronoRancherWorld) -> str:
    if world.random.randint(0, 99) < world.options.trap_chance:
        return "Undo Trap"
    return "Congratulatory Critter"



def create_item_with_correct_classification(world: ChronoRancherWorld, name: str) -> ChronoRancherItem:
    
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]

    return ChronoRancherItem(name, classification, ITEM_NAME_TO_ID[name], world.player)



def create_all_items(world: ChronoRancherWorld) -> None:

    itempool: list[Item] = [
        world.create_item("Fluff"),
        world.create_item("Spike"),
        world.create_item("Blob"),
        world.create_item("Brick")
    ]

    item_ids = ITEM_NAME_TO_ID.values()
    if world.options.lock_levels.value == 1 :
        for x in range(99) :
            if x in item_ids :
                level = "Level " + str(x) + " Unlock"
                itempool.append(world.create_item(level))
    elif world.options.lock_levels.value == 2 :
        for x in world.locations.KEY_LEVELS :
            level = "Level " + str(x) + " Unlock"
            itempool.append(world.create_item(level))
    elif world.options.lock_levels.value == 3 :
        if "All" in world.options.key_levels_to_beat or len(world.options.key_levels_to_beat.value) == 0:
            for x in locations.KEY_LEVELS:
                level = "Level " + str(x) + " Unlock"
                itempool.append(world.create_item(level))
        else :
            for lvl in world.options.key_levels_to_beat.value:
                level = lvl + " Unlock"
                itempool.append(world.create_item(level))

    if world.options.checks_critter_sanity :
        itempool.append(world.create_item("Chrono-Rancher Bestiary"))
        itempool.append(world.create_item("Fluff Bestiary"))
        itempool.append(world.create_item("Spike Bestiary"))
        itempool.append(world.create_item("Blob Bestiary"))
        itempool.append(world.create_item("Brick Bestiary"))

    num_of_items = len(itempool)

    num_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))

    needed_number_of_filler_items = num_unfilled_locations - num_of_items

    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    world.multiworld.itempool += itempool