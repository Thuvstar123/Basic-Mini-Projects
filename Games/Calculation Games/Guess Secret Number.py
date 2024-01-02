import random

lowest=-1
highest=101
value=0

print("Please think of a number between 0 and 100!")
value=random.randint(lowest+1,highest-1)
ans=input("Is your secret number "+str(value)+"?"+"\nEnter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

while ans!="c":
    if ans=="h":
        highest=value
    elif ans=="c":
        print("Game Over. Your secret number was:",value)
        break
    else:
        lowest=value
    value=random.randint(lowest+1,highest-1)
    ans=input("Is your secret number "+str(value)+"?"+"\nEnter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if highest-2==lowest:
        print("Game Over. Your secret number was:",value)
        break
else:
    print("Game Over. Your secret number was:",value)