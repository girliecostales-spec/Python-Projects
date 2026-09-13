# The Deep Diver’s Dilemma

## Project Description

The Deep Diver’s Dilemma is my original project inspired by the Treasure Island project. It is a text-based, choose-your-own-adventure game created in Python with an original storyline. The player becomes a diver whose friend is swept away by a strong underwater current. Each decision determines the ending. 

I developed the storyline and its branching paths to strengthen my understanding of nested conditional statements.

## Features

* Original underwater adventure storyline
* Multiple decision points
* Several branching story paths
* Different winning, survival, and game-over endings
* Flexible text input
* Opening ASCII artwork
* Choices involving exploration, rescue, and risk

## Skills and Concepts Practised

* Using nested conditional statements
* Applying `.strip()` and `.lower()`
* Planning branching program logic
* Creating multiline prompts
* Managing multiple variables
* Writing interactive narratives
* Testing different routes through a program

## How It Works

The player reads each situation and enters the word for their chosen action. The program normalises the response using `.strip().lower()` and uses nested conditional statements to select the next scene.

Every decision moves the player farther along a particular branch until an ending is reached.

## Example Code

```python
choice = input(
    'Type "return" to return to the boat.\n'
    'Type "follow" to follow your friend.\n'
    'Type "wait" for the current to weaken.\n'
)

if choice.strip().lower() == "follow":
    print("The current carries you away.")
elif choice.strip().lower() == "wait":
    print("You wait until the current weakens.")
else:
    print("You return to the boat.")
```

## How to Run the Project

1. Download `the-divers-dilemma.py`.
2. Open it in a Python-compatible editor.
3. Run the program.
4. Read each situation carefully.
5. Type one of the displayed choices and press Enter.

## Challenge and Solution

The greatest challenge was managing a large number of connected choices without mixing up the story paths. I solved this by placing conditional statements inside their corresponding branches and using descriptive variable names that represent the sequence of decisions.

## Possible Improvements

* Validate every response instead of treating unexpected input as a default choice
* Add a replay feature
* Divide the different scenes into functions
* Add an inventory or oxygen system
* Track the player’s decisions
* Create a visual or browser-based version
