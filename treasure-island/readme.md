# Treasure Island

## Project Description

Treasure Island is a short text-based adventure game created in Python. The player must make the correct decisions at a crossroads, a lake, and a mysterious house to reach the hidden treasure.

## Features

* Interactive choose-your-own-adventure gameplay
* Three main decision points
* Multiple game-over outcomes
* One winning path
* Flexible, case-insensitive input
* Treasure-chest ASCII artwork

## Skills and Concepts Practised

* Collecting user input
* Using nested conditional statements
* Applying `.strip()` and `.lower()`
* Comparing strings
* Creating multiline prompts
* Controlling a program’s flow
* Designing branching story paths
* Displaying ASCII artwork with raw strings

## How It Works

The player makes a choice at each stage of the adventure. Each response is cleaned with `.strip()` and converted to lowercase with `.lower()`.

Nested conditional statements determine whether the player continues to the next scene, wins the game, or receives a game-over ending.

## Example Code

```python
turn_1 = input(
    "You're at a crossroads. Where do you want to go?\n"
    'Type "left" or "right".\n'
)

if turn_1.strip().lower() == "left":
    print("You continue towards the lake.")
else:
    print("You fell into a hole. Game Over.")
```

## How to Run the Project

1. Download `treasure-island.py`.
2. Open it in a Python-compatible editor.
3. Run the program.
4. Read the available choices.
5. Type your selected action and press Enter.

## Challenge and Solution

The main challenge was connecting several choices while ensuring that only the correct path reached the treasure. I solved this by nesting each new decision inside the condition that allows the player to continue and using separate outcomes for the other choices.

## Possible Improvements

* Add more locations and decision points
* Validate unexpected responses separately
* Allow the player to restart the game
* Add an inventory or health system
* Create several winning endings
* Divide each scene into a function
