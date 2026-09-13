import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
user_choice=input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors.\n")
if user_choice == "0":
    print("You chose:")
    print(rock)
elif user_choice == "1":
    print("You chose:")
    print(paper)
elif user_choice == "2":
    print("You chose:")
    print(scissors)
else:
    print("That is not a valid input. Type 0, 1 or 2. \n")
computer_choice = random.randint(0,2)
if computer_choice == 0:
    print("Computer chose:")
    print(rock)
elif computer_choice==1:
    print("Computer chose:")
    print(paper)
else:
    print("Computer chose:")
    print(scissors)
final_answer = [user_choice, computer_choice]
print (final_answer)
if final_answer == ["1",0] or final_answer == ["0",2] or final_answer == ["2",1]:
    print("You win!")
elif final_answer == ["0",0] or final_answer == ["1",1] or final_answer == ["2",2]:
    print("It's a tie!")
else:
    print ("You lose!")