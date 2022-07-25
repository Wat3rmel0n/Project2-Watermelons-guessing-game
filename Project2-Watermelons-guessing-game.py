import random
import time
from threading import Thread
num = random.randint(1, 10) 
print("""Welcome to watermelon's insane number guesser game!!!!
Here you will go through 3 watermelon number guessing levels.
If you will complete all of them and send proof to watermelon you will get a very cool prize.\n
Anyways good luck and let's begin.\n
Choose a number (1 - 10) you have 3 tries btw, but dont be scared ill guide you a bit.\n""")
guess_num = 0
while True:         #DONT CHEATTTTTTT
    if guess_num < 3:
        guess = int(input())
        guess_num+=1
        if guess < num:
            print("\nYour guess is too low\n")
        if guess > num:
            print("\nYour guess is too high\n")
        if guess == num:
            if guess_num == 1:
                print("\nCongrats you've passed watermelon's insane number guesser game's first level in 1 try!!!")
            else:
                print("\nCongrats you've passed watermelon's insane number guesser game's first level in " + str(guess_num) + " tries")
            break
    else:
        print("""\nUnfortuantely you've lost watermelons guessing game. 
        But don't be sad you can always try again.""")
        quit()
del(num) 
del(guess) 
del(guess_num)
time.sleep(2)
print("\nNow get ready for the next level it's gonna be a lil bit harder this time but the prize is worth it.")
time.sleep(2)
print("\nAnyways let's get started.")
print("Choose your number now (1 - 15) you have 4 tries.\n")
num = random.randint(1, 15) 
guess_num = 0
while True:         #DONT CHEATTTTTTT
    if guess_num < 4:
        guess = int(input())
        guess_num+=1
        if guess < num:
            print("\nYour guess is too low\n")
        if guess > num:
            print("\nYour guess is too high\n")
        if guess == num:
            if guess_num == 1:
                print("\nCongrats you've passed watermelon's insane number guesser game's second level in 1 try!!!")
            else:
                print("\nCongrats you've passed watermelon's insane number guesser game's second level in " + str(guess_num) + " tries")
            break
    else:
        print("""\nUnfortuantely you've lost watermelons guessing game. 
        But don't be sad you can always try again.""")
        quit()
time.sleep(2)

del(num)
del(guess)
del(guess_num)
print("""\nOoooOOoooO now its time for the third level it's gonna be scaaaaaaarrryy.
Here you will have to guess a number (1 - 30) and you will have 5 tries.\n""")
time.sleep(2)
print("Are you ready? (y/n)\n")

while True:
    answer = input()
    if answer == "y":
        break
    if answer == "n":
        print("\nOk... Are you ready now?\n")
    else:
        print("\ny or n\n")
num = random.randint(1, 30)
guess_num = 0
while True:         #DONT CHEATTTTTTT
    if guess_num < 5:
        guess = int(input())
        guess_num+=1
        if guess < num:
            print("\nYour guess is too low\n")
        if guess > num:
            print("\nYour guess is too high\n")
        if guess == num:
            if guess_num == 1:
                print("\nCongrats you've passed watermelon's insane number guesser game's LAST level in 1 try!!!!!!!!!!!")
            else:
                print("\nCongrats you've passed watermelon's insane number guesser game's LAST level in " + str(guess_num) + " tries!!!")
            break
    else:
        print("""\nUnfortuantely you've lost watermelons guessing game. 
        But don't be sad you can always try again.""")
        quit()
print("Thanks for playing watermelon's insane number guesser! I hope you liked it and didnt cheat ofc.\n")
time.sleep(3)
print("Srry if that 3rd level was a bit too hard\n")
time.sleep(3)
print("Anyways here is the prize for now (ill add a bigger one in the future dw\n")
time.sleep(3)
print("""⠀⠀⠀⠀⠀⣀⣤⣀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣶⠿⣿⠯⠻⣷⣿⠙⠶⢶⣄⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠁⠀⠸⣿⣠⠉⢻⣤⡀⠉⢉⠽⠳⣤⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⠐⠀⠀⢈⣙⣶⣿⡉⢳⠒⠁⣀⠴⠊⠻⣦⡀⠀
⠀⠀⠀⠀⠀⠀⠀⣀⡴⠋⢹⣄⣠⡶⢏⣹⠿⠁⢀⡼⠧⣌⡡⢀⡀⠀⠉⠻⡄
⠀⠀⠀⠀⣠⠤⠊⠁⠀⠢⢤⠬⠛⠏⠽⠧⠟⢉⣁⣀⣀⣈⣳⣤⣤⡀⠁⢰⣿
⠀⣀⡴⠞⢁⣀⣀⡀⠤⠤⠴⠒⢒⡀⠨⠭⠭⠭⠭⠭⠽⠿⠿⠿⢭⣉⠻⡏⠐
⢰⠟⣠⡤⠙⠛⠉⠉⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡇⣷⠀
⢸⡄⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣠⡤⣶⣤⣤⣤⣴⣖⣿⣿⡯⠿⠿⣧⢿⠀
⠀⣧⠤⣶⣶⣶⣾⣯⡿⠿⠿⠿⠿⢷⡿⢍⠛⠛⠉⠉⢡⠞⠀⢻⡄⠀⣿⢸⡀
⠀⣿⠋⠁⠀⣠⠾⠋⠘⣆⠀⠀⢀⡎⠀⠀⠳⣄⠀⠀⡟⠀⠰⠈⢻⡀⣿⢸⣏
⠀⣿⠀⠀⢸⡃⠰⠟⢐⡏⠀⠀⠘⣧⣀⣃⣀⣽⣆⣀⣉⣒⣒⣺⢿⣶⡏⢸⡇
⠀⢸⣆⣤⣤⣭⣿⣷⡿⣳⣿⠿⢿⣿⣟⣿⣿⠽⠛⠛⠛⠛⠛⠛⠋⠉⡷⢸⣷
⠀⠘⣿⠚⠛⠛⠛⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠃⣸⠟
⠀⠀⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣤⣤⣤⡤⠴⠶⠾⠟⠉⠀
⠀⠀⠸⣧⣤⣤⡤⠴⠒⠒⠚⠛⠛⠛⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
time.sleep(2)
print("\nmmm tasty cake")
time.sleep(2)
print("""\nWell you can take the cake and go now.
Come back if ull want to play again and eat some cake. Byeeee""")
quit()