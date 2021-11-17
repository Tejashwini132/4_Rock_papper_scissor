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
game = [rock, paper, scissors]
choice = int(input("What do you choose? Type 0 for rock , 1 for Paper and 2 for Scissors\n"))
if choice < 0 or choice > 2:
    print("Invaild Choice , You lose")
else:
    print(game[choice])

    comp = random.randint(0, 2)
    print("Computer Choice:")
    print(game[comp])

    if choice == comp:
        print("It a draw")
    elif choice == 0 and comp == 1:
        print("computer won")
    elif choice == 0 and comp == 2:
        print("You won!")
    elif choice == 1 and comp == 0:
        print("Computer won")
    elif choice == 1 and comp == 2:
        print("Computer won")
    elif choice == 2 and comp == 0:
        print("Computer won")
    elif choice == 2 and comp == 1:
        print("You won!")
    else:
        print("ERROR")
