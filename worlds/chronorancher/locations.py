from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items

if TYPE_CHECKING:
    from .world import ChronoRancherWorld


LOCATION_NAME_TO_ID = {
    "Level 1 Complete": 1,
    "Level 2 Complete": 2,
    "Level 3 Complete": 3,
    "Level 4 Complete": 4,
    "Level 5 Complete": 5,
    "Level 6 Complete": 6,
    "Level 7 Complete": 7,
    "Level 8 Complete": 8,
    "Level 9 Complete": 9,
    "Level 10 Complete": 10,
    "Level 11 Complete": 11,
    "Level 12 Complete": 12,
    "Level 13 Complete": 13,
    "Level 14 Complete": 14,
    "Level 15 Complete": 15,
    "Level 16 Complete": 16,
    "Level 17 Complete": 17,
    "Level 18 Complete": 18,
    "Level 19 Complete": 19,
    "Level 20 Complete": 20,
    "Level 21 Complete": 21,
    "Level 22 Complete": 22,
    "Level 23 Complete": 23,
    "Level 24 Complete": 24,
    "Level 25 Complete": 25,
    "Level 26 Complete": 26,
    "Level 27 Complete": 27,
    "Level 28 Complete": 28,
    "Level 29 Complete": 29,
    "Level 30 Complete": 30,
    "Chrono-Rancher Bestiary": 100,
    "Fluff Bestiary": 101,
    "Spike Bestiary": 102,
    "Blob Bestiary": 103,
    "Brick Bestiary": 104
}

TUTORIAL_LEVELS = [1,2,3,4,5,6,15,21]
KEY_LEVELS = [20,30]

class ChronoRancherLocation(Location):
    game: "The Chrono-Rancher"


def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


def create_all_locations(world: ChronoRancherWorld) -> None:
    create_regular_locations(world)
    create_events(world)


def create_regular_locations(world: ChronoRancherWorld) -> None:

    menu = world.get_region("Menu")
    fluff_levels = world.get_region("Fluff Levels")
    spike_levels = world.get_region("Spike Levels")
    blob_levels = world.get_region("Blob Levels")
    brick_levels = world.get_region("Brick Levels")
    fluff_spike_levels = world.get_region("Fluff Spike Levels")
    fluff_blob_levels = world.get_region("Fluff Blob Levels")
    fluff_brick_levels = world.get_region("Fluff Brick Levels")
    spike_blob_levels = world.get_region("Spike Blob Levels")
    spike_brick_levels = world.get_region("Spike Brick Levels")
    blob_brick_levels = world.get_region("Blob Brick Levels")
    fluff_spike_blob_levels = world.get_region("Fluff Spike Blob Levels")
    fluff_spike_brick_levels = world.get_region("Fluff Spike Brick Levels")
    fluff_blob_brick_levels = world.get_region("Fluff Blob Brick Levels")
    spike_blob_brick_levels = world.get_region("Spike Blob Brick Levels")
    fluff_spike_blob_brick_levels = world.get_region("Fluff Spike Blob Brick Levels")

    menu_locations = get_location_names_with_ids(
        ["Level 1 Complete"]
    )
    menu.add_locations(menu_locations, ChronoRancherLocation)

    fluff_locations = get_location_names_with_ids(
        ["Level 2 Complete", "Level 3 Complete", "Level 4 Complete", "Level 6 Complete","Level 8 Complete", "Level 13 Complete"]
    )
    fluff_levels.add_locations(fluff_locations, ChronoRancherLocation)

    spike_locations = get_location_names_with_ids(
        ["Level 5 Complete", "Level 7 Complete", "Level 11 Complete", "Level 14 Complete"]
    )
    spike_levels.add_locations(spike_locations, ChronoRancherLocation)

    blob_locations = get_location_names_with_ids(
        ["Level 15 Complete", "Level 16 Complete"]
    )
    blob_levels.add_locations(blob_locations, ChronoRancherLocation)

    brick_locations = get_location_names_with_ids(
        ["Level 21 Complete", "Level 23 Complete"]
    )
    brick_levels.add_locations(brick_locations, ChronoRancherLocation)

    fluff_spike_locations = get_location_names_with_ids(
        ["Level 9 Complete", "Level 10 Complete", "Level 12 Complete"]
    )
    fluff_spike_levels.add_locations(fluff_spike_locations, ChronoRancherLocation)

    fluff_blob_locations = get_location_names_with_ids(
        ["Level 17 Complete", "Level 19 Complete"]
    )
    fluff_blob_levels.add_locations(fluff_blob_locations, ChronoRancherLocation)

    fluff_brick_locations = get_location_names_with_ids(
        ["Level 24 Complete"]
    )
    fluff_brick_levels.add_locations(fluff_brick_locations, ChronoRancherLocation)

    spike_blob_locations = get_location_names_with_ids(
        ["Level 18 Complete"]
    )
    spike_blob_levels.add_locations(spike_blob_locations, ChronoRancherLocation)

    spike_brick_locations = get_location_names_with_ids(
        []
    )
    spike_brick_levels.add_locations(spike_brick_locations, ChronoRancherLocation)

    blob_brick_locations = get_location_names_with_ids(
        ["Level 22 Complete", "Level 25 Complete", "Level 28 Complete"]
    )
    blob_brick_levels.add_locations(blob_brick_locations, ChronoRancherLocation)

    fluff_spike_blob_locations = get_location_names_with_ids(
        ["Level 20 Complete"]
    )
    fluff_spike_blob_levels.add_locations(fluff_spike_blob_locations, ChronoRancherLocation)

    fluff_spike_brick_locations = get_location_names_with_ids(
        ["Level 27 Complete"]
    )
    fluff_spike_brick_levels.add_locations(fluff_spike_brick_locations, ChronoRancherLocation)

    fluff_blob_brick_locations = get_location_names_with_ids(
        []
    )
    fluff_blob_brick_levels.add_locations(fluff_blob_brick_locations, ChronoRancherLocation)

    spike_blob_brick_locations = get_location_names_with_ids(
        []
    )
    spike_blob_brick_levels.add_locations(spike_blob_brick_locations, ChronoRancherLocation)

    fluff_spike_blob_brick_locations = get_location_names_with_ids(
        ["Level 26 Complete", "Level 29 Complete", "Level 30 Complete"]
    )
    fluff_spike_blob_brick_levels.add_locations(fluff_spike_blob_brick_locations, ChronoRancherLocation)

    #Add code for if bestiary is enabled
    if world.options.checks_critter_sanity :
        chronorancher_bestiary = get_location_names_with_ids(
            ["Chrono-Rancher Bestiary"]
        )
        menu.add_locations(chronorancher_bestiary, ChronoRancherLocation)

        fluff_bestiary = get_location_names_with_ids(
            ["Fluff Bestiary"]
        )
        fluff_levels.add_locations(fluff_bestiary, ChronoRancherLocation)

        spike_bestiary = get_location_names_with_ids(
            ["Spike Bestiary"]
        )
        spike_levels.add_locations(spike_bestiary, ChronoRancherLocation)

        blob_bestiary = get_location_names_with_ids(
            ["Blob Bestiary"]
        )
        blob_levels.add_locations(blob_bestiary, ChronoRancherLocation)

        brick_bestiary = get_location_names_with_ids(
            ["Brick Bestiary"]
        )
        brick_levels.add_locations(brick_bestiary, ChronoRancherLocation)

def create_events(world: ChronoRancherWorld) -> None :
    menu = world.get_region("Menu")
    fluff_levels = world.get_region("Fluff Levels")
    spike_levels = world.get_region("Spike Levels")
    blob_levels = world.get_region("Blob Levels")
    brick_levels = world.get_region("Brick Levels")
    fluff_spike_levels = world.get_region("Fluff Spike Levels")
    fluff_blob_levels = world.get_region("Fluff Blob Levels")
    fluff_brick_levels = world.get_region("Fluff Brick Levels")
    spike_blob_levels = world.get_region("Spike Blob Levels")
    spike_brick_levels = world.get_region("Spike Brick Levels")
    blob_brick_levels = world.get_region("Blob Brick Levels")
    fluff_spike_blob_levels = world.get_region("Fluff Spike Blob Levels")
    fluff_spike_brick_levels = world.get_region("Fluff Spike Brick Levels")
    fluff_blob_brick_levels = world.get_region("Fluff Blob Brick Levels")
    spike_blob_brick_levels = world.get_region("Spike Blob Brick Levels")
    fluff_spike_blob_brick_levels = world.get_region("Fluff Spike Blob Brick Levels")
    match world.options.victory_condition :
        case 0 :
            #percent of levels need to be completed
            menu.add_event("Completed Level 1", "Level Completed", location_type=ChronoRancherLocation, item_type=items.ChronoRancherItem)

            fluff_levels.add_event("Completed Level 2", "Level Completed", location_type=ChronoRancherLocation, item_type=items.ChronoRancherItem)
            fluff_levels.add_event("Completed Level 3", "Level Completed", location_type=ChronoRancherLocation, item_type=items.ChronoRancherItem)
            fluff_levels.add_event("Completed Level 4", "Level Completed", location_type=ChronoRancherLocation, item_type=items.ChronoRancherItem)
            fluff_levels.add_event("Completed Level 6", "Level Completed", location_type=ChronoRancherLocation, item_type=items.ChronoRancherItem)
            fluff_levels.add_event("Completed Level 8", "Level Completed", location_type=ChronoRancherLocation, item_type=items.ChronoRancherItem)
            fluff_levels.add_event("Completed Level 13", "Level Completed", location_type=ChronoRancherLocation, item_type=items.ChronoRancherItem)

            spike_levels.add_event("Completed Level 5", "Level Completed", location_type=ChronoRancherLocation, item_type=items.ChronoRancherItem)
            spike_levels.add_event("Completed Level 7", "Level Completed", location_type=ChronoRancherLocation, item_type=items.ChronoRancherItem)
            spike_levels.add_event("Completed Level 11", "Level Completed", location_type=ChronoRancherLocation, item_type=items.ChronoRancherItem)
            spike_levels.add_event("Completed Level 14", "Level Completed", location_type=ChronoRancherLocation, item_type=items.ChronoRancherItem)

            blob_levels.add_event("Completed Level 15", "Level Completed", location_type=ChronoRancherLocation, item_type=items.ChronoRancherItem)
            blob_levels.add_event("Completed Level 16", "Level Completed", location_type=ChronoRancherLocation, item_type=items.ChronoRancherItem)

            brick_levels.add_event("Completed Level 21", "Level Completed", location_type=ChronoRancherLocation, item_type=items.ChronoRancherItem)
            brick_levels.add_event("Completed Level 23", "Level Completed", location_type=ChronoRancherLocation, item_type=items.ChronoRancherItem)

            fluff_spike_levels.add_event("Completed Level 9", "Level Completed", location_type=ChronoRancherLocation, item_type=items.ChronoRancherItem)
            fluff_spike_levels.add_event("Completed Level 10", "Level Completed", location_type=ChronoRancherLocation, item_type=items.ChronoRancherItem)
            fluff_spike_levels.add_event("Completed Level 12", "Level Completed", location_type=ChronoRancherLocation, item_type=items.ChronoRancherItem)

            fluff_blob_levels.add_event("Completed Level 17", "Level Completed", location_type=ChronoRancherLocation, item_type=items.ChronoRancherItem)
            fluff_blob_levels.add_event("Completed Level 19", "Level Completed", location_type=ChronoRancherLocation, item_type=items.ChronoRancherItem)

            fluff_brick_levels.add_event("Completed Level 24", "Level Completed", location_type=ChronoRancherLocation, item_type=items.ChronoRancherItem)

            spike_blob_levels.add_event("Completed Level 18", "Level Completed", location_type=ChronoRancherLocation, item_type=items.ChronoRancherItem)

            blob_brick_levels.add_event("Completed Level 22", "Level Completed", location_type=ChronoRancherLocation, item_type=items.ChronoRancherItem)
            blob_brick_levels.add_event("Completed Level 25", "Level Completed", location_type=ChronoRancherLocation, item_type=items.ChronoRancherItem)
            blob_brick_levels.add_event("Completed Level 28", "Level Completed", location_type=ChronoRancherLocation, item_type=items.ChronoRancherItem)

            fluff_spike_blob_levels.add_event("Completed Level 20", "Level Completed", location_type=ChronoRancherLocation, item_type=items.ChronoRancherItem)

            fluff_spike_brick_levels.add_event("Completed Level 27", "Level Completed", location_type=ChronoRancherLocation, item_type=items.ChronoRancherItem)

            fluff_spike_blob_brick_levels.add_event("Completed Level 26", "Level Completed", location_type=ChronoRancherLocation, item_type=items.ChronoRancherItem)
            fluff_spike_blob_brick_levels.add_event("Completed Level 29", "Level Completed", location_type=ChronoRancherLocation, item_type=items.ChronoRancherItem)
            fluff_spike_blob_brick_levels.add_event("Completed Level 30", "Level Completed", location_type=ChronoRancherLocation, item_type=items.ChronoRancherItem)
        case 1 :
            #number of key levels need to be completed
            if "All" in world.options.key_levels_to_beat or len(world.options.key_levels_to_beat.value) == 0:
                #all key levels are considered valid
                fluff_spike_blob_levels.add_event("Completed Level 20", "Level Completed",
                                                  location_type=ChronoRancherLocation,
                                                  item_type=items.ChronoRancherItem)
                fluff_spike_blob_brick_levels.add_event("Completed Level 30", "Level Completed",
                                                  location_type=ChronoRancherLocation,
                                                  item_type=items.ChronoRancherItem)
            else :
                if "Level 20" in world.options.key_levels_to_beat :
                    fluff_spike_blob_levels.add_event("Completed Level 20", "Level Completed",
                                                       location_type=ChronoRancherLocation,
                                                       item_type=items.ChronoRancherItem)
                if "Level 30" in world.options.key_levels_to_beat :
                    fluff_spike_blob_brick_levels.add_event("Completed Level 30", "Level Completed",
                                                       location_type=ChronoRancherLocation,
                                                       item_type=items.ChronoRancherItem)


