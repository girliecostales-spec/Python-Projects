# Velocity Vortex 🎢

## Project Description

Velocity Vortex is a Python roller coaster ticketing program. It checks whether a guest meets the minimum height requirement and calculates the ticket price based on age, promotional eligibility, and the choice to purchase a souvenir photo.

## Features

* Checks the minimum height requirement.
* Assigns ticket prices according to age.
* Offers an optional $3 souvenir photo.
* Calculates and displays the total cost.

## Skills and Concepts Practised

* Converting text input into integers with `int()`.
* Using comparison operators.
* Using `if`, `elif`, and `else` statements.
* Writing nested conditional statements.
* Displaying results with f-strings.

## How It Works

The program first checks the guest’s height. Eligible guests enter their age, which determines the ticket price and promotional eligibility. If they choose a souvenir photo, $3 is added before the total is displayed.

## Example

```text
Welcome to Velocity Vortex!

What is your height in cm?
165

You are eligible to ride the roller coaster.

How old are you?
25

Adult tickets are $12.

Would you like to take home a souvenir photo of your roller coaster experience? Type Yes or No
Yes

Your Velocity Vortex experience costs $15.
```

## How to Run the Project

1. Make sure Python is installed.
2. Download `roller-coaster-ticketing-machine.py`.
3. Open a terminal in the folder containing the file.
4. Enter:

```bash
python "roller coaster ticketing machine.py"
```

5. Enter your height and age, then choose whether you want a photo.

## Challenge and Solution

One challenge was making sure the souvenir-photo charge was added to the correct ticket price. I solved this by assigning every eligible guest’s ticket price to the bill variable first and then using bill += 3 when the guest selected a photo.

## Possible Improvements

* Accept different versions of yes and no.
* Let users retry after invalid input.
* Add group or family tickets.
* Include more ride packages.
* Display a detailed receipt.
