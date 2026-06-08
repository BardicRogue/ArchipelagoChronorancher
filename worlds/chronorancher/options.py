from dataclasses import dataclass

from Options import Choice, OptionGroup, OptionSet, PerGameCommonOptions, NamedRange, Range, Toggle

class VictoryCondition(Choice):
    """
    What the Victory Condition should be.
    **Percent of Levels** requires the player to beat a certain percent of all levels (determined in goal_level_percent option)
    **Key Levels** requires the player to beat certain key levels (which levels and how many are set in key_levels_to_beat and num_key_levels)
    """

    display_name = "Victory Condition"

    option_percent_of_levels = 0
    option_key_levels = 1

    default = option_percent_of_levels


class GoalLevelPercent(NamedRange):
    """
    If **Percent of Levels** goal is set, what percent of levels need to be beaten to win? (Rounds up)
    """

    display_name = "Goal Level Percent"

    range_start = 1
    range_end = 100
    special_range_names = {
        "half": 50,
        "all": 100
    }

    default = "half"


class KeyLevelsToBeat(OptionSet):
    """
    If **Key Levels** goal is set, select all the levels which are valid levels for you to beat.
    Possible levels are ["Level 21", "Level 30"]
    Can also be set to "All" to include all key levels.
    """

    display_name = "Key Levels to Beat"

    valid_keys = frozenset({
        "Level 20",
        "Level 30",
        "All"
    })

    default = frozenset({"All"})

class NumKeyLevels(Range):
    """
    How many of the Key Levels defined above you need to win the game. (0 == All)
    **Only enabled if Key Levels goal is set**
    """
    display_name = "Number of Key Levels to Beat"

    range_start = 0
    range_end = 5#need to figure out how many key levels there are gonna be
    default = 0
    special_range_names = {
        "all": 0,
        "single": 1
    }


class LockLevels(Choice):
    """
    Which levels to lock behind 'keys' if any.
    If goal_key_levels is selected and key_levels is not the goal, no levels will be locked
    """

    display_name = "Lock Levels"

    option_none = 0
    option_all_levels = 1
    option_all_key_levels = 2
    option_goal_key_levels = 3

    default = option_all_levels


class ChecksCritterSanity(Toggle):
    """
    Whether bestiary entries on the main menu are checks.
    If enabled, each check requires beating the level which introduces that critter, then clicking on that critter on the main menu.
    Adds 4* checks.
    """
    display_name = "CritterSanity"


class TrapChance(Range):
    """
    Percent chance for filler items to be replaced with traps.
    """

    display_name = "Trap Chance"

    range_start = 0
    range_end = 100

    default = 0

@dataclass
class ChronoRancherOptions(PerGameCommonOptions) :
    victory_condition : VictoryCondition
    goal_level_percent : GoalLevelPercent
    key_levels_to_beat : KeyLevelsToBeat
    num_key_levels : NumKeyLevels
    lock_levels : LockLevels
    checks_critter_sanity : ChecksCritterSanity
    trap_chance : TrapChance