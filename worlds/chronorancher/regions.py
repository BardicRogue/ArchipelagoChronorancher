from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from .world import ChronoRancherWorld



def create_and_connect_regions(world: ChronoRancherWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: ChronoRancherWorld) -> None:

    menu = Region("Menu", world.player, world.multiworld)
    fluff_levels = Region("Fluff Levels", world.player, world.multiworld)
    spike_levels = Region("Spike Levels", world.player, world.multiworld)
    blob_levels = Region("Blob Levels", world.player, world.multiworld)
    brick_levels = Region("Brick Levels", world.player, world.multiworld)
    fluff_spike_levels = Region("Fluff Spike Levels", world.player, world.multiworld)
    fluff_blob_levels = Region("Fluff Blob Levels", world.player, world.multiworld)
    fluff_brick_levels = Region("Fluff Brick Levels", world.player, world.multiworld)
    spike_blob_levels = Region("Spike Blob Levels", world.player, world.multiworld)
    spike_brick_levels = Region("Spike Brick Levels", world.player, world.multiworld)
    blob_brick_levels = Region("Blob Brick Levels", world.player, world.multiworld)
    fluff_spike_blob_levels = Region("Fluff Spike Blob Levels", world.player, world.multiworld)
    fluff_spike_brick_levels = Region("Fluff Spike Brick Levels", world.player, world.multiworld)
    fluff_blob_brick_levels = Region("Fluff Blob Brick Levels", world.player, world.multiworld)
    spike_blob_brick_levels = Region("Spike Blob Brick Levels", world.player, world.multiworld)
    fluff_spike_blob_brick_levels = Region("Fluff Spike Blob Brick Levels", world.player, world.multiworld)

    regions = [menu, fluff_levels, spike_levels, blob_levels, brick_levels, fluff_spike_levels, fluff_blob_levels, fluff_brick_levels, spike_blob_levels, spike_brick_levels, blob_brick_levels, fluff_spike_blob_levels, fluff_spike_brick_levels, fluff_blob_brick_levels, spike_blob_brick_levels, fluff_spike_blob_brick_levels]

    world.multiworld.regions += regions


def connect_regions(world: ChronoRancherWorld) -> None:
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

    menu.connect(fluff_levels, "Menu to Fluff")
    menu.connect(spike_levels, "Menu to Spike")
    menu.connect(blob_levels, "Menu to Blob")
    menu.connect(brick_levels, "Menu to Brick")
    fluff_levels.connect(fluff_spike_levels, "Fluff to Spike")
    fluff_levels.connect(fluff_blob_levels, "Fluff to Blob")
    fluff_levels.connect(fluff_brick_levels, "Fluff to Brick")
    #spike_levels.connect(fluff_spike_levels, "Spike to Fluff")
    spike_levels.connect(spike_blob_levels, "Spike to Blob")
    spike_levels.connect(spike_brick_levels, "Spike to Brick")
    #blob_levels.connect(fluff_blob_levels, "Blob to Fluff")
    #blob_levels.connect(spike_blob_levels, "Blob to Spike")
    blob_levels.connect(blob_brick_levels, "Blob to Brick")
    #brick_levels.connect(fluff_brick_levels, "Brick to Fluff")
    #brick_levels.connect(spike_brick_levels, "Brick to Spike")
    #brick_levels.connect(blob_brick_levels, "Brick to Blob")
    fluff_spike_levels.connect(fluff_spike_blob_levels, "Fluff Spike to Blob")
    fluff_spike_levels.connect(fluff_spike_brick_levels, "Fluff Spike to Brick")
    #fluff_blob_levels.connect(fluff_spike_blob_levels, "Fluff Blob to Spike")
    fluff_blob_levels.connect(fluff_blob_brick_levels, "Fluff Blob to Brick")
    #fluff_brick_levels.connect(fluff_spike_brick_levels, "Fluff Brick to Spike")
    #fluff_brick_levels.connect(fluff_blob_brick_levels, "Fluff Brick to Blob")
    #spike_blob_levels.connect(fluff_spike_blob_levels, "Spike Blob to Fluff")
    spike_blob_levels.connect(spike_blob_brick_levels, "Spike Blob to Brick")
    #spike_brick_levels.connect(fluff_spike_brick_levels, "Spike Brick to Fluff")
    #spike_brick_levels.connect(spike_blob_brick_levels, "Spike Brick to Blob")
    #blob_brick_levels.connect(fluff_blob_brick_levels, "Blob Brick to Fluff")
    #blob_brick_levels.connect(spike_blob_brick_levels, "Blob Brick to Spike")
    fluff_spike_blob_levels.connect(fluff_spike_blob_brick_levels, "Fluff Spike Blob to Brick")
    #fluff_spike_brick_levels.connect(fluff_spike_blob_brick_levels, "Fluff Spike Brick to Blob")
    #fluff_blob_brick_levels.connect(fluff_spike_blob_brick_levels, "Fluff Blob Brick to Spike")
    #spike_blob_brick_levels.connect(fluff_spike_blob_brick_levels, "Spike Blob Brick to Fluff")