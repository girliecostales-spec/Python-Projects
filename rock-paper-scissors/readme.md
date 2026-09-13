# Rock, Paper, Scissors

## Project Description

This project is a Python version of the traditional Rock, Paper, Scissors game. The player chooses an option, the computer makes a random selection, and the program compares both choices to determine the winner.

I worked on this project as paart of the Python online course. However, the code that I wrote is different from the one presented in the course. Instead of using multiple elif statements and comparison of individual results, I summarised them using logical operators. and putting results in lists  

## Features

* Player-versus-computer gameplay
* Random computer choice
* Rock, paper, and scissors ASCII art
* Win, lose, and tie results
* Basic invalid-input message

## Skills and Concepts Practised

* Importing the `random` module
* Generating random integers
* Using lists to group related values
* Applying `if`, `elif`, and `else`
* Combining conditions with `or`
* Comparing strings and integers
* Displaying multiline ASCII art

## How It Works

The player enters `0`, `1`, or `2`. The computer randomly generates a number using the same range.

The program stores the player’s and computer’s choices in a list. Conditional statements compare this list with the winning and tying combinations. Any remaining valid combination is a loss.

## Example Code

```python
final_answer = [user_choice, computer_choice]

if final_answer == ["1", 0] or final_answer == ["0", 2] or final_answer == ["2", 1]:
    print("You win!")
elif final_answer == ["0", 0] or final_answer == ["1", 1] or final_answer == ["2", 2]:
    print("It's a tie!")
else:
    print("You lose!")
```

## How to Run the Project

1. Download `rock-paper-scissors.py`.
2. Open it in a Python-compatible editor.
3. Run the program.
4. Enter `0` for rock, `1` for paper, or `2` for scissors.

## Challenge and Solution

The main challenge was representing all the possible outcomes of the game. I solved this by storing both choices in a list and using conditional statements joined with `or` to identify the winning and tying combinations.

## Possible Improvements

* Stop the round when invalid input is entered
* Store the artwork in a list for simpler selection
* Add a replay option
* Track the player’s and computer’s scores
* Create a best-of-three mode
* Simplify the winner-selection logic
