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

#Write your code below this line 👇
from random import randint

user_choice = int(input('Type 0 for rock , 1 for paper and 2 for scissors'))
computer_choice = randint(0, 2)
if user_choice == 0:
    print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
    if computer_choice == 0:
        print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
        print('It is a draw')
    elif computer_choice == 1:
        print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
        print('The computer won')
    else:
        print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
        print('You won !')

elif user_choice == 1:
    print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
    if computer_choice == 0:
        print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
        print('You won')
    elif computer_choice == 1:
        print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
        print('it is a draw')
    else:
        print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
        print('You lost')
else:
    print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
    if computer_choice == 0:
        print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
        print('You lost')
    elif computer_choice == 1:
        print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
        print('You won')
    else:
        print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
        print('It is a draw')
