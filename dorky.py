name = "Derkon"

def menu():
    # Gives options for the user to use.
    menu = input("\n So... What now?\n \n 1 - Fun Fact\n 2 - Version Number\n 3 - Who are you?\n 4 - Change my name!\n 5 - What is my name?\n 6 - Next... \n Page 1 of 2\n\n Chooose a number : ")
    if menu == "1":
        menuop1()
    elif menu == "2":
        menuop2()
    elif menu == "3":
        menuop3()
    elif menu == "4":
        menuop4()
    elif menu == "5":
        menuop5()
    elif menu == "6":
        menu2b()
    
# Fun Fact

def menuop1():
    time.sleep(1)
    print("\nWell... You think the Kobold would actually code this in. Buuut... Nope. He's just a lazy lizard.\n")
    time.sleep(1)
    menu()
   
# Version Check 
   
def menuop2():
    print("\nHmm... Let me check.")
    time.sleep(1)
    print("\nWhere did I put it?! It was right here!")
    time.sleep(4)
    print("\nAha! This is... The beta?! Does that mean I'm unfinished?! Oh no!")
    menu()

# Who are you?

def menuop3():
    time.sleep(1)
    print("\nWho am I? I... Don't think anyone has ever asked! I'm Dorky! Only here to help out with whatever I possibly can!")
    time.sleep(1)
    menu()

# Name Changer

def menuop4():
    print("\nSo you want to change your name? Alright...")
    global name 
    name = input("So. What is it?")
    menu()
    
# Whats your name?

def menuop5():
    print("\nYour name is" , name, "!")
    menu()
    
# Random Number Gen

def menuop6():
    n = random.randomint(0,21)
    print("Your number is" , n, "!")
    menu2b()
    
# Calculator (But you know. The one that doesnt crash.)

global numsetask
global number
global hey
number = 0

def menum():
    choice = input("Calculator by LowerCaseDragon Vers 1.0\n\n Dividing and Multiplying havent been added! \n\nDo you want to : \n 1- Subtract\n 2 - Add to your number\n 3 - Set your number\n 4 - Multiply your number\n 5 - Divide your number\n 6 - Display your number?\n 7 - Exit to Menu\n Choice : ")
    if choice == "1":
        numsub()
    elif choice == "2":
        numadd()
    elif choice == "3":
        numset()
    elif choice == "4":
        print("Do you not understand what 'Not added' Means?")
    elif choice == "5":
        print("Do you not understand what 'Not added' Means?")
    elif choice == "6":
        numdisplay()
    elif choice == "7":
        menu2b()
    else:
        print("That's invalid! Try again why don't you?")
        menum()

def numdisplay():
    print("Your number is" , number, ".")
    menum()

def numset():
    global number    
    numset = input("What do you want to set your number to?\n\n Input :  ")
    number = int(numset)
    print("Your new number is" , number, ".")
    time.sleep(1.5)
    menum()

def numsub():
    global number
    if number == 0:
        print("Hey! Go set the number first!")
        menum()
    else:
        numsubask = input("What do you want to subtract from this number?\n\n Input :   ")
        number = number - int(numsubask)
        print("Your new number is" , number, ".")
        time.sleep(1.5)
        menum()

def numadd():
    global number
    if number == 0:
        print("Hey! Go set the number first!")
        menum()
    else:
        numaddask = input("What do you want to add to this number?\n\n Input :   ")
        number = number + int(numaddask)
        print("\nYour new number is" , number, ".")
        time.sleep(1.5)
        menum()
        
# Second Menu
        
def menu2b():
    print("\nWhelp. We're here. What did you expect?")
    time.sleep(5)
    print("\n...Wanna do some stuff?\n\n 1 - Random Number Generator\n 2 - Calculator\n 3 - Questionare\n 6 - Back\n Page 2 of 2\n")
    answer = input("Choooose a number : ")
    if answer == "1":
        menuop6()
    elif answer == "2":
        menum()
    elif answer == "3":
        agequestionare()
    elif answer == "6":
        menu()
        

import time
import random

time.sleep(1)
print("   ")

print("Hello! I'm your friend! My name is Dorky!")

# Asking for USERS name

name = input("Who are you? ")

if name == "Derkon":
    print("  ")
    print('\nHi, Derkon... I think I remember you!')
    time.sleep(2.5)
    print("\nActually... Let me just...")
    time.sleep(2.5)
    print("\nHere we go!")
    menu()
else:
    print("  ")
    print("Hello " + name + "! Are you new around here?")

time.sleep(1)
print("\n Give me a second... \n")
time.sleep(1)

skip = input("Would you like to skip this or not? You can come back to it later on.\n 1 - Yes\n 2 - No\n Choose a number : ")

if skip == "1":
    menu()
if skip == "2":
    agequestionare()

# Questionare (Age)

def agequestionare():
    global age
    age = int(input("Alright... How old are you? "))
    print("  ")
    time.sleep(1.2)
    if age > 20:
        print("Wow! You're " , age,". That's old!")
        moodquestionare()
    else:
        print("Hey! You're " , age,"! That's pretty young, " , name, "!")
        moodquestionare()
    
# Asking for their mood

def moodquestionare():
    global mood
    mood = input("How are you feeling? (G)ood or (B)ad?... Or something (W)eird? ")
    if mood == "G":
        print("That's good to know " + name + "!")
        questionarefirst()
    elif mood == "B":
        print("Well that's not good " + name + "...")
        questionarefirst()
    else:
        print("I'm not sure how to feel about that " + name + "...")
        questionarefirst()

#Judging their age

#First Question
def questionarefirst():
    ques1 = input("How has your day been?")
    print("Hmm.\n")
    time.sleep(1)
    print("\nThat's neat! Even if I can't truely understand that!")
    print("\nNext question!")
    questionaresecond()

#Second question
    
def questionaresecond():
    ques2 = input("\nGot anything special planned?")
    time.sleep(1)
    print("Hmmm... Interesting...")
    time.sleep(1)
    if mood == "G":
        print("You're feeling good," + name + "!")
    elif mood == "B":
        print("You aren't feeling so well," + name + "!")
    else:
        print("You feel... Something I don't understand.")


#Opening up into the menu
def menustart():
    time.sleep(2)
    print("...")
    time.sleep(4)
    print("...Give me some time.")
    time.sleep(1)
    menu()