import random
print("Discover what's possible with CipherPhrase, your handy-dandy random wi-fi password generator.")
print("Answer the following questions to generate your password.")
word=input("Give me a memorable word. \n")
word_list= list(word)
random.shuffle(word_list)
word_len=len(word)
word_code=""
for char in word_list:
    word_code += char
digits=input("Give me a memorable 8-digit number. \n")
digits_list= list(digits)
random.shuffle(digits_list)
digit_code=""
for char in digits_list:
    digit_code += char
symbol=int(input(
    "How many symbols would you like to use? \n"
    "We suggest a minimum of 1 to generate a strong passwword. \n"
))
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', "@"]
symbol_code=""
for char in range(0, symbol):
    symbol_code +=random.choice(symbols)
password_list = list(word_code + digit_code + symbol_code)
random.shuffle(password_list)
final_password=""
for char in password_list:
    final_password += char
print(f"Here's your new wi-fi password: {final_password}")
