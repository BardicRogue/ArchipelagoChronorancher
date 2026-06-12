# The Chrono-Rancher Setup Guide

## Required Software
- A copy of "The Chrono-Rancher Archipelago"
  - Can be found on the game's [itch page](https://bardicrogue.itch.io/the-chrono-rancher-archipelago).
  - You can either run the game in browser, or download the windows version (see below for more details on differences between versions).
- [Archipelago](https://github.com/ArchipelagoMW/Archipelago/releases/latest)
- Chrono-Rancher's APWorld
  - Can be found on the itch page among the downloads

## Install the APWorld
1. Download `chronorancher.apworld`.
2. Double-click it in your files to add it to your Archipelago world.
3. If that doesn't work, you may need to place it manually in the `custom_worlds` folder in your Archipelago directly.

## Running the Game
There are two ways to run the game:
- directly on the itch page, using the web build
- through the windows build you download from the itch page.

The two versions have a few differences, so here's how you run each of them.

### Web Version
1. Click `Run Game` on the itch page.
2. When it finishes loading, you will be presented with options to connect to a multiworld slot.
3. Connect to the Multiworld slot. If you don't know how:
    - `ip`: server/host name - If running the game through the archipelago website, this will be `archipelago.gg`
    - `Port`: Server port - on an archipelago website page, this will be the numbers after the colon in `archipelago.gg:*****`
    - `Slot`: Your player name
    - `Password`: If your host has made a password, put it here and check the checkbox.
    - Finally, click the button that says `Connect`
4. If you did everything correctly, the game should bring you to the main menu screen.

### Windows Executable
1. Extract the `chronorancher_ap_windows` zip.
2. Run the `chronorancher_archipelago.exe` file.
3. Similar to the web version, you will be presented with options to connect to a multiworld slot.
4. Follow step 3 for the web version above if you don't know how to connect to a multiworld slot.

The Windows version of the game also has a text client you can open and connect/reconnect through.
On the initial connect screen, the Windows version has a button for you to open the text client.
Once you've started the game, you can also find that button under Options → Archipelago Options.
The text client will pop up as a second window, and can be used to connect or disconnect from your slot.
It will also function like most text clients, logging when items are collected.
It has a `hints` tab that will show any item and location hints related to your slot.

## Connection FAQ

### My slot got disconnected, how do I reconnect?
If you start a level, there should be a button at the top of the screen that shows the connection status.
Clicking that button while disconnected will attempt to reconnect you.

### I need to change my port or slot name, what do I do?
If playing the Windows version, you can open the text client, disconnect, and then change the details as you need.
if you attempt to connect to a different slot while in the middle of a level, the game may force you to return to the main menu.

If playing on the Web version, you'll need to reload the page and reconnect from the start screen.

### When I click to connect, the game stays in a `Connecting...` state and never finished connecting.
Double-check that your port and slot are correct.
This usually happens when the port is not correctly filled in and you try to connect via text client.
