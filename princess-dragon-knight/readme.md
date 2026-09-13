# Princess, Dragon and Knight

## Project Description

Princess, Dragon and Knight is a Python game I created that is inspired by Rock, Paper, Scissors. In this game, the player selects a character while the computer randomly chooses its own. The rules are simple: 
- Princess charms Knight.
- Knight defeats Dragon.
- Dragon captures Princess.

I wanted to practise randomisation. Originally, I learnt to randomise results with similar data types, i.e. integer and integer. In this program, I used a string and int data types for the results to see if I could apply all that I have so far learnt. I also wanted to create extra effects by producing another ASCII art when the results are generated.

## Features

* Three playable characters
* Random computer selection
* Character ASCII artwork
* Win, lose, and tie outcomes
* Instructions explaining the game rules
* Special artwork showing each character encounter

## Skills and Concepts Practised

* Importing and using the `random` module
* Generating random integers
* Using variables and tuples
* Applying `if`, `elif`, and `else`
* Comparing combinations of values
* Creating multiline strings
* Displaying ASCII art

## How It Works

The player enters `p`, `d`, or `k` to select a character. The computer generates a random number from 1 to 3, with each number representing one of the characters.

The player's choice and computer's choice are placed in a tuple. Conditional statements compare the tuple with the possible winning and losing combinations to determine the result.

## Example Code

```python
computer_choice = random.randint(1, 3)
result = (user_choice, computer_choice)

if result == ("p", 3):
    print("Princess charms the knight. YOU WIN!")
elif result == ("k", 2):
    print("Knight defeats the dragon. YOU WIN!")
```

## How to Run the Project

1. Download `princess-dragon-knight.py`.
2. Open it in a Python-compatible editor.
3. Run the program.
4. Enter `p`, `d`, or `k` when prompted.

## Challenge and Solution

The main challenge I had is that uppercase inputs cause a bug in the game. It gives a default tie result. I solved this by attaching .strip().lower() to the input instead of result. This removes extra spaces and converts uppercase letters to lowercase, making input easier to compare and preventing errors. 

## Possible Improvements

* Reject invalid input before generating the computer’s choice
* Accept complete words such as `princess`
* Add a replay option
* Keep track of the score
* Organise the repeated code into functions
