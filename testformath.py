number = 0
import time

def menu2():
    print("Goodbye!")
    menum()

def menum():
    choice = input("Calculator by LowerCaseDragon Vers 1.0\n\n Dividing and Multiplying havent been added! \n\nDo you want to : \n 1- Subtract\n 2 - Add to your number\n 3 - Set your number\n 4 - Multiply your number\n 5 - Divide your number\n 6 - Display your number?\n Choice : ")
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
        menu2()
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

menum()