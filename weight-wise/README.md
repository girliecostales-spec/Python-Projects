# WeightWise – Healthy Weight Range Calculator

## Project Description

WeightWise is a Python program that estimates a healthy weight range based on the user’s height. It accepts height in metres or feet and inches and allows the user to enter their weight in kilograms or pounds.

The program compares the user’s current weight with the calculated range and displays whether it is within, above, or below that range. If the weight is outside the range, the program calculates the difference between the current weight and the estimated range.

I independently developed this project to apply and strengthen the Python concepts I had learned.

## Features

* Accepts height in metres or feet / inches
* Accepts weight in kilograms or pounds
* Converts between imperial and metric measurements
* Calculates an estimated healthy weight range
* Calculates suggested weight loss / weight gain

## Skills and Concepts Practised

* Collecting user input with `input()`
* Converting values using `int()` and `float()`
* Creating and using variables
* Applying formula to convert measurement units
* Using nested conditional statements
* Normalising text with `.strip()` and `.lower()`
* Rounding numerical results
* Displaying results with f-strings

## How It Works

The program first asks whether the user wants to enter their height in metres or feet. When feet are selected, the program collects the feet and inches separately and converts the complete measurement into metres.

It estimates a weight range using BMI reference values of 18.5 and 24.9:

```text
Minimum weight = 18.5 × height²
Maximum weight = 24.9 × height²
```

The user can then enter their current weight in kilograms or pounds. The program converts measurements when necessary and compares the current weight with the calculated range.

## Example

```text
What unit would you like to use? Type m or feet.
m

What is your height in m?
1.65

Your healthy weight range is 50.4 kg to 67.8 kg.

What unit would you like to use? Type kg or lbs.
kg

What is your weight in kg?
60

You are in the healthy range. Keep it up!
```

## How to Run the Project

1. Make sure Python is installed on your computer.
2. Download `healthy-weight-range.py`.
3. Open the file in a Python-compatible editor.
4. Run the program.
5. Select your preferred measurement units.
6. Enter your height and current weight when prompted.

## Challenges and Solutions

### Supporting different units

It was challenging to allow users to choose between metric and imperial measurements. I used nested conditional statements to follow the correct calculation path based on the selected units.

### Making user input more flexible

Users may enter units with capital letters or extra spaces. I used `.strip()` to remove surrounding spaces and `.lower()` to make the unit comparisons case-insensitive.

### Comparing the current weight with a range

I used comparison operators and conditional statements to determine whether the user’s weight was below, within, or above the estimated range.

## Future Improvements

* Add error handling for non-numerical input
* Prevent zero or negative height and weight values
* Let users restart the calculator without rerunning the script
* Organise repeated calculations into functions
* Reduce repeated sections of code

## Disclaimer

This program was created for educational and programming-practice purposes. The calculated range is a general estimate based on BMI reference values and does not account for factors such as age, body composition, medical conditions, or individual health needs. It should not be considered medical advice.
