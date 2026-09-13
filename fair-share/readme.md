# FairShare – Tip Calculator

## Project Description

FairShare is a Python program that calculates how much each person should contribute when sharing a bill. It adds the selected tip percentage to the original bill and divides the total equally among the group. 
A very small modification I made is to accept different percentages as tips as the mathematical formula works for all valid numerical inputs.

## Features

* Accepts the total bill amount
* Accepts a custom tip percentage
* Accepts the number of people sharing the bill
* Calculates the value of the tip
* Adds the tip to the original bill
* Divides the final bill equally
* Rounds each person’s contribution to two decimal places

## Skills and Concepts Practised

* Converting input with `float()` and `int()`
* Storing numerical values in variables
* Using arithmetic operators
* Applying the order of operations
* Rounding numbers with `round()`
* Displaying results with f-strings

## How It Works

The program asks the user for the original bill, preferred tip percentage, and number of people sharing the expense.

It converts the tip percentage into a decimal, adds it to the original bill, and divides the result by the number of people.

The calculation follows this formula:

```text
Contribution per person = Bill × (1 + Tip ÷ 100) ÷ Number of people
```

For example, a 15% tip is converted to:

```text
15 ÷ 100 = 0.15
```

The bill is then multiplied by `1.15` to include both the original amount and the tip.

## Example Code

```python
contribution = (bill * (1 + (tip / 100))) / people

print(f"Each person should contribute ${round(contribution, 2)}")
```

## Example Output

```text
Welcome to FairShare!
It's time to split the bill. I'll help you share the bill equally.

How much is the total bill?
$100

How much tip would you like to give?
15

How many people are to split the bill?
4

Each person should contribute $28.75
```

## How to Run the Project

1. Download `tip-calculator.py`.
2. Open it in a Python-compatible editor.
3. Run the program.
4. Enter the total bill amount.
5. Enter the preferred tip percentage.
6. Enter the number of people sharing the bill.
7. Review the contribution per person.

## Challenge and Solution

The main challenge was creating a calculation that adds a percentage-based tip before dividing the final amount among several people.

I solved this by dividing the tip percentage by 100, adding it to `1`, and multiplying the result by the original bill. I then divided the total by the number of people and rounded the result to two decimal places.

## Possible Improvements

* Validate that the user enters numerical values
* Prevent zero or negative values
* Format the result so it always displays two decimal places
* Display the total tip amount
* Display the complete bill after adding the tip
* Allow unequal contributions
* Let the user perform another calculation

