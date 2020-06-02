from random import *


guess = ""
password = input("Enter your password: ")
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

while guess != password:
    guess = ""
    for letter in password:
        guessLetter = letters[randint(0, 25)]
        guess = str(guessLetter) + str(guess)
    print(guess)
print("Password guessed!")
input("")
