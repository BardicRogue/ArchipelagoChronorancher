# The Chrono-Rancher Player Options
Description of the various options in a .yaml for The Chrono-Rancher Archipelago.

## Victory Conditions
There are two possible victory conditions for The Chrono-Rancher:
- `percent_of_levels`: Beat a certain percent of all levels in the game.
The exact percent is defined in the option `goal_level_percent`.
- `key_levels`: Beat a certain number of key levels in the game.
You can set which key levels are included with `key_levels_to_beat` and how many of them need to be beaten with `num_key_levels`.
  - Currently, only levels 20 and 30 can be included for the "Key Levels" goal.

## Lock Levels
Depending on which setting is set, this will add "Level Unlock" items to the pool that you need to collect in order to play certain levels.
- `none`: All levels are unlocked from the start.
- `all`: All levels except tutorial levels are locked from the start (Levels 1-6, 15, and 21 are tutorial levels).
Adds 22 progression items to the pool, greatly decreasing the number of filler items in the pool.
- `all_key_levels`: Levels 20 and 30 will be locked, adding 2 progression items to the pool.
- `goal_key_levels`: Levels included in the `key_levels_to_beat` setting will be locked.
Will not lock any levels if victory condition is `percent_of_levels`. Adds up to 2 progression items to the pool.

## Checks CritterSanity
If enabled, the bestiary entries on the main menu page will be checks
(when you complete a tutorial level that introduces a new critter, it adds a corresponding sprite to the main menu.
When that sprite is clicked, it opens a bestiary entry, which sends a check if this setting is enabled).
Adds 5 locations and items to the pool. Suggested to enable if playing with `lock_levels: all`.

