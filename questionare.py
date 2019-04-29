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

# Skipping the questionare

skip = input("Would you like to skip this or not? You can come back to it later on.\n 1 - Yes\n 2 - No\n Choose a number : ")

if skip == "1":
    menu()
if skip == "2":
    agequestionare()