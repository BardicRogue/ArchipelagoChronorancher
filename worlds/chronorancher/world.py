from typing import Any, Mapping

from worlds.AutoWorld import World

from . import items, locations, regions, rules, web_world
from . import options as chronorancher_options

class ChronoRancherWorld(World):
    """
    The Chrono-Rancher is a puzzle game about time loops, originally designed for the 2025 GMTK Game Jam.
    Herd critters into time loops, but be sure not to be trapped yourself!
    """

    game = "The Chrono-Rancher"

    web = web_world.ChronoRancherWebWorld()

    options_dataclass = chronorancher_options.ChronoRancherOptions
    options : chronorancher_options.ChronoRancherOptions

    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID

    origin_region_name = "Menu"

    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name: str) -> items.ChronoRancherItem:
        return items.create_item_with_correct_classification(self, name)

    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)

    def fill_slot_data(self) -> Mapping[str, Any]:
        return self.options.as_dict(
            "victory_condition", "goal_level_percent", "key_levels_to_beat","num_key_levels","lock_levels","checks_critter_sanity"
        )