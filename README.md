# Cyber Quest : System Override
#### Video Demo: https://youtu.be/2WUEKW0k46s
#### Description:

Cyber Quest: System Override is a turn-based, command-line battle game built entirely in Python. The player takes on the role of a system administrator fighting off a rogue "Virus Boss" that has breached the mainframe. The game features interactive turn-based combat, dynamic ASCII health and energy bars, randomized damage calculations, and a fully colorized terminal UI.

While many beginner programming projects rely on standard scrolling text, Cyber Quest was designed to feel like a classic retro video game. It achieves this by constantly clearing and redrawing the terminal screen, creating a static, immersive frame where the action happens in place.

## Features and Mechanics

The core loop of the game pits the player (100 HP) against the Virus Boss (150 HP). The combat system relies heavily on resource management.

On each turn, the player is presented with a menu of strategic options:
1. **Quick Strike**: A highly reliable attack that deals moderate damage (10-15) and generates 15 Energy.
2. **Heavy Hack**: A risky, high-variance attack that can deal massive damage or barely scratch the enemy (5-25) and generates 10 Energy.
3. **Firewall**: A defensive move that cuts incoming boss damage by 50% for one turn while generating a large burst of 20 Energy.
4. **System Patch**: A healing move to restore the player's health (15-20).
5. **Overclock Ultimate**: Once the player accumulates 50 Energy, they unlock this devastating attack that deals 40-50 damage.

After the player acts, the Virus Boss automatically counter-attacks with its own randomized damage output, occasionally landing a "Critical Data Spike" that requires the player to adapt their strategy on the fly.

## File Structure & Design Choices

The project strictly adheres to CS50P's architectural requirements, with all core logic separated into distinct, testable functions outside of `main()`.

### `project.py`
This is the main application file. It imports `time` for pacing the battle, `os` for clearing the screen, `random` for number generation, and `colorama` for text styling.

Key design choices in `project.py`:
* **`create_bar(value, max_value)`**: Instead of just printing raw numbers, this function calculates the percentage of a resource remaining and constructs a 20-character string of block characters (`█`) and dashes (`-`). It actively prevents negative health or over-healing from breaking the bar's UI formatting.
* **`calculate_value(action)`**: Rather than scattering `random.randint()` calls throughout the main loop, I centralized all combat math into this single function. This makes it incredibly easy to balance the game later by changing values in just one place.
* **`check_battle_status(player_hp, boss_hp)`**: This function isolates the win/loss condition logic. I designed it so that if both the player and the boss happen to drop to 0 HP on the exact same turn, the game defaults to a loss.

### `test_project.py`
This file contains the `pytest` test suite. Testing a game with random variables presents a unique challenge.
To test `calculate_value()`, I utilized a `for` loop that runs the function 20 times per action type, using `assert` to guarantee the random output never falls outside the expected minimum and maximum bounds. I also aggressively tested the `create_bar` function to ensure it properly handles edge cases.

### `requirements.txt`
This file contains the required external pip dependencies:
* `colorama`: Used extensively throughout the game to color-code elements (Green for player health, Yellow for energy, Red for the boss, Cyan for attacks).
* `pytest`: Required for running the test suite.
