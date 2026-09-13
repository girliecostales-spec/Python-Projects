# CipherPhrase – Wi-Fi Password Generator

## Project Description

CipherPhrase is a Python program that creates a customised Wi-Fi password using memorable information supplied by the user. It rearranges the characters from a memorable name and date, adds a selected number of random symbols, and then shuffles all the characters to produce the final password.

The idea for this project arose from the need to have strong security passwords. However, as a password user, I would still want to use characters that have some significance to me. Working on this project allowed me to apply and strengthen the skills I learned while creating a basic random password generator.

## Features

* Accepts the name of a memorable person
* Accepts a memorable date
* Uses every character from the supplied name
* Uses every character from the supplied date
* Shuffles the name and date characters separately
* Allows the user to choose how many symbols to include
* Randomly selects symbols from a predefined list
* Combines and reshuffles all password characters
* Displays the completed Wi-Fi password

## Skills and Concepts Practised

* Importing and using the `random` module
* Converting strings into lists with `list()`
* Shuffling lists with `random.shuffle()`
* Iterating directly through lists
* Repeating actions with `for` loops
* Using `range()` to repeat an action a selected number of times
* Selecting random items with `random.choice()`
* Building strings using `+=`
* Combining strings and lists
* Collecting and converting user input
* Displaying results with f-strings

## How It Works

The program asks the user to enter the name of a memorable person. It converts the name into a list and shuffles its characters. A `for` loop then goes through the shuffled list and joins the characters into a new string.

The same process is applied to the memorable date. The program then asks how many symbols the user wants and uses `random.choice()` repeatedly to select that number of symbols.

Finally, the shuffled name, date, and symbols are combined into one list. This complete list is shuffled again before another `for` loop joins all the characters into the final Wi-Fi password.

## Example Code

```python
word_list = list(word)
random.shuffle(word_list)

word_code = ""

for char in word_list:
    word_code += char
```

The same approach is used to rearrange the date:

```python
digits_list = list(digits)
random.shuffle(digits_list)

digit_code = ""

for char in digits_list:
    digit_code += char
```

The complete password is then shuffled:

```python
password_list = list(word_code + digit_code + symbol_code)
random.shuffle(password_list)

final_password = ""

for char in password_list:
    final_password += char
```

## Example Output

```text
Discover what's possible with CipherPhrase, your handy-dandy random password generator.
Answer the following questions to generate your password.

Give me a name of a memorable person.
Rebecca

Give me a memorable date in dd-mm-yyyy format.
12-05-2020

How many symbols would you like to use?
3

Here's your new wi-fi password: 0e@2b1-0c5a2R-%0
```

The generated result will be different each time because the characters and symbols are randomly arranged.

## How to Run the Project

1. Download `wifi-password-generator.py`.
2. Open it in a Python-compatible editor.
3. Run the program.
4. Enter the requested name.
5. Enter a memorable date in the requested format.
6. Enter the number of symbols to include.
7. Copy the generated password.

## Challenge and Solution

The main challenge was preventing the program from repeatedly selecting some characters while leaving out others. In the earlier version, `random.choice()` selected characters independently, so the same letter or digit could appear more than once.

I solved this by converting the name and date into lists and applying `random.shuffle()` to them. I then used `for char in word_list` and `for char in digits_list` to add every shuffled character exactly once.

Another challenge was ensuring that the letters, digits, and symbols did not remain grouped according to category. I solved this by combining all the generated characters into one list and shuffling the complete list again before creating the final password.

## Possible Improvements

* Avoid asking users to enter real names or personal dates
* Generate a password from non-personal memorable words
* Add uppercase and lowercase characters
* Let the user choose the total password length
* Validate the format of the entered date
* Prevent zero or negative symbol quantities
* Add a password-strength indicator
* Use Python’s `secrets` module for stronger randomisation
* Place repeated character-joining steps inside a function
* Use `"".join()` to simplify the loops that rebuild the strings

## Security Notice

This program was created to practise Python and demonstrate password-generation concepts. Passwords containing personal information may be easier for attackers to guess. For real accounts, users should avoid names, birthdays, and other identifiable information and store passwords in a trusted password manager.
