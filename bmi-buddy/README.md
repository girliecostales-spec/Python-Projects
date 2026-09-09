# BMI Buddy – BMI Calculator

## Project Description

BMI Buddy is a Python program that calculates a user’s Body Mass Index (BMI) using their height in metres and weight in kilograms. It displays the calculated BMI and classifies the result into a corresponding BMI category.

This is one of the tasks suggested in "100 Days of Code™: The Complete Python Pro Bootcamp". I used this program as a basis for my other project called WeightWise.

## Features

* Collects the user’s height in metres
* Collects the user’s weight in kilograms
* Calculates the user’s BMI
* Rounds the result to one decimal place
* Displays the corresponding BMI category

## Skills and Concepts Practised

* Collecting user input with `input()`
* Converting input using `float()`
* Storing data in variables
* Using exponentiation with `**`
* Rounding numbers with `round()`
* Displaying results with f-strings
* Using `if`, `elif`, and `else` statements

## How It Works

The program calculates BMI using the following formula:

```text
BMI = weight in kilograms ÷ height in metres²
```

It then uses conditional statements to classify the result as:

* Underweight
* Healthy weight
* Overweight
* Obese Class I
* Obese Class II
* Obese Class III

## Example

```text
This is BMI Buddy!
Knowing your BMI matters. It helps you determine your risk for chronic health issues like type 2 diabetes, heart disease, and high blood pressure. Answer the questions to find out your BMI now.
What is your height in m?
1.65
What is your weight in kg?
60

Your BMI is 22.0.
You are in the healthy weight range.
```

## How to Run the Project

1. Make sure Python is installed on your computer.
2. Download `bmi-calculator.py`.
3. Open the file in a Python-compatible editor.
4. Run the program.
5. Enter your height and weight when prompted.

## Challenge and Solution

The challenging part of this project is ensuring that user's inputs are properly categorised. I used an `if-elif-else` structure with upper limits so that Python checks each range in the correct order.

## Future Improvements

* Accept height and weight in different measurement units
* Check that the user enters valid numerical values
* Prevent zero or negative measurements

## Disclaimer

This program was created for educational and programming-practice purposes. BMI is a general screening measurement and does not account for every factor affecting a person’s health. The results should not be considered medical advice.
