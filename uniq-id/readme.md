# UniqID – Reference Number Generator

## Project Description

UniqID is a Python program that creates customised reference codes for businesses. It builds a company identifier from the company’s name and combines it with randomly selected letters and numbers.

This project was inspired by the random password generator I worked on in the course. I wanted to continue practising how to use loops, randomisation, string indexing, and user-selected code lengths.

## Features

* Creates a company code from a business name
* Allows users to choose the number of random letters and digits
* Generates a formatted reference code

## Skills and Concepts Practised

* Importing the `random` module
* Collecting and converting user input
* Applying `.upper()`
* Using conditional statements
* Repeating actions with `for` loops
* Using `range()`
* Selecting random list items
* Building strings with `+=`
* Formatting output with f-strings

## How It Works

For a one-word company name, the program uses its first two letters. For a company name with multiple words, it uses the first letters of the first and last words.

It then generates the requested number of random uppercase letters and digits before combining all three sections into one reference code.

## Example Code

```python
letter_code = ""

for char in range(0, letter):
    letter_code += random.choice(uppercase)

print(f"Here is your reference code: {company_code}-{letter_code}-{number_code}.")
```

Example result:

```text
GC-XPF-8305
```

## How to Run the Project

1. Download `reference-number-generator.py`.
2. Open it in a Python-compatible editor.
3. Run the program.
4. Answer the questions about the company and reference-code length.

## Challenge and Solution

One challenge was generating several random characters and displaying them as one continuous code. I solved this by starting with empty strings and using `for` loops to repeatedly add randomly selected letters and numbers.

## Possible Improvements

* Check that the company name contains enough characters
* Validate numerical input
* Prevent negative code lengths
* Generate several codes at once
* Check previously generated codes to prevent duplicates
* Save generated codes to a file or database
