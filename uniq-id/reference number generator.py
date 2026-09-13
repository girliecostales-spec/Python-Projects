import random
print("Meet UniqID, your partner in creating unique reference codes that fit your needs.")
name_number=input("How many words are there in your company's name? \n")
if name_number == "1":
    company_name=input("What is the name of your company? \n")
    letter1=company_name[0]
    letter2=company_name[1]
    company_code = letter1.upper() + letter2.upper() 
else:
    company_name_1=input("What is the first word of your company's name? \n")
    company_name_2=input("What is the last word of your company's name? \n")
    letter1=company_name_1[0]
    letter2=company_name_2[0]
    company_code = letter1.upper() + letter2.upper() 
letter=int(input("How many letters would you like to use for your reference code? \n"))
uppercase = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
letter_code = ""
for char in range(0, letter):
    letter_code += random.choice(uppercase)
number=int(input("How many numbers would you like to use your reference code? \n"))
digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
number_code = ''
for char in range(0, number):
    number_code += random.choice(digits)
print(f"Here is your reference code: {company_code}-{letter_code}-{number_code}.")
print("Thank you for using UniqID. We hope to serve you again soon!")
