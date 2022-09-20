import random
"""
library that we use in order to choose random words from a list

"""
name= input("what is your name ?")# enter your name
print("Good Luck !", name)
words=['rainbow','computer','science','python program','math','player','water','board','mobile',]
       # function will choose one random words from the list
word= random.choice(words)
print("Guss the character")

guesses=' '
# any number of turns can be used here
turns=12
while turns>0:
    failed = 0
    # count the number of times a user fails
    
    for char in word:
        if char in guesses:
            print(char,end=" ")
        else:
            print("_")
            print(char,end=" ")
            #for every failure 1 will be incremented 
            failed +=1
    if failed == 0:
        #user will win the game if failure is 0 and ' you win ' will be given as output
        
        print("you win")
        # this print the correct word
        print("The word is:",word)
        break
    #if user has input the wrong alphabet then
    #it will ask user to enter another alphabet
    print()
    guess=input("guess a character:")
    #every input character will be stored in guesses
    guesses +=guess

    #check input with the character in word
    if guess not in word:
        truns -=1
        # if the character doesn't match the word then 'wrong' will be given as output

        print("wrong")
        #this will print the number of turns left for the user
        print("you have",+turns, 'more guesses')
        if turns==0:
            print("you loose")
        
    
