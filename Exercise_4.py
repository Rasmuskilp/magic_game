#magic number game
#prompt the user for input
#def magic_number_game(number_guess):
number_guess = int(input('Enter a number from 0 to 99:'))
import random
magic_number = random.randint(0,99)
#generate a random number using a python library
number_tries= [0,1,2,3,4,5]
count = 0
for item in number_tries:
    if count >= 5:
        print('you lost the game!')
        break
    if number_guess == magic_number:
        print('you guessed the right answer')
        break
    elif number_guess > magic_number:
        print('your answer was above the number,try again')
        count += 1
        number_guess = int(input('Enter a number from 0 to 99:'))
        continue
    else:
        print('sorry but your answer was below the number, try again')
        count += 1
        number_guess = int(input('Enter a number from 0 to 99:'))
        continue
        #return number_guess





#check the number against a magic number
#let the user know if he/she won or lost
#if the guess was above or under magic number