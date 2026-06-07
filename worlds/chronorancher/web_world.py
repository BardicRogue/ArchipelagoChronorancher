from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld

#from .options import option_groups, option_presets

class ChronoRancherWebWorld(WebWorld):
    game : "The Chrono-Rancher"

    theme = "grass"

    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Chrono-Rancher for MultiWorld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["BardicRogue"],
    )

    tutorial_en = [setup_en]