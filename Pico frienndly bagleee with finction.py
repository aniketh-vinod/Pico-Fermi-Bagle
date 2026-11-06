import random
def pfb(guess,str_digits):
    num=1
    clue=[]
    for i in range (0,3):
        if guess[i]==str_digits[i]:
            clue.append("Fermi")
        elif guess[i] in str_digits:
            clue.append("Pico")
        elif guess==str_digits:
            print("Congrats!")
            break
    if len(clue)==0:
        print("Bagle")
    else:
        print(clue)
    return
while True:
    maxguess=10
    digits = [1,2,3,4,5,6,7,8,9]
    random.shuffle(digits)
    str_digits=''
    for i in range(3):
        str_digits=str_digits+str(digits[i])
    num=1
    while num<=maxguess:
        guess=input("Guess number: ")
        if len(guess)!=3 or guess.isdigit()==False:
            print("Enter a valid input")
            break
        else:
            pfb(guess, str_digits)
        num = num + 1
    print(str_digits)
    chance=input("Do you want to play again? (y/n): ")
    if chance=="n":
        break
