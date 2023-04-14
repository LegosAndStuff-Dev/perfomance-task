import random

code = [random.randint(1, 9), random.randint(1, 9), random.randint(1,9), random.randint(1,9)]
CurrentCode = [0, 0, 0, 0]
userCode = [0, 0, 0, 0]

GameRunning = True

tries = 0

def checkCode(slot):
    userInput = userCode[slot]
    if userInput == code[slot]:
        CurrentCode[slot] = code[slot]
    
    else:
        pass

print("                               Code Guesser                               ")
print("")
print("------------------------------- Directions --------------------------------")
print()
print("1) You have to guess the 4 diget code")
print("2) It will show when you have the digets correct and which ones are correct")
print("\n")


while GameRunning == True:
    userCode[0] = int(input("Enter the first diget of the code (1 - 9): "))
    userCode[1] = int(input("Enter the second diget of the code (1 - 9): "))
    userCode[2] = int(input("Enter the third diget of the code (1 - 9): "))
    userCode[3] = int(input("Enter the forth diget of the code (1 - 9): "))

    checkCode(0)
    checkCode(1)
    checkCode(2)
    checkCode(3)

    print("\nYour Current Code:\n")
    for i in range(len(CurrentCode)):
        if CurrentCode[i] == 0:
            print(" _ ", end="")
        else:
            print(f" {CurrentCode[i]} ", end="")

    print("\n")

    if CurrentCode == code and userCode == code:
        GameRunning = False

    tries += 1

print("Congrats you got the code all right!")
print(f"It took you {tries} tries")