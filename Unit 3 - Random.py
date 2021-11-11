# Python has a built in library for random data
import random

random_integer = random.randint(1, 100)
print(random_integer)
# The randint() function generates a random number between two values
# This program uses randint() to simulate dice with any number of sides
import random

sides = int(input('How many sides does the dice have? '))
random_integer = random.randint(1, sides)  # will choose a random number between 1 and the number of sides you input
print('You rolled a {}'.format(random_integer))

# Rock, paper, scissors
import random


def rock_paper_scissors():
    random_number = random.randint(1, 3)
    if random_number == 1:
        hand = 'rock'
    elif random_number == 2:
        hand = 'paper'
    else:
        hand = 'scissors'
    return hand


choice = input('rock, paper or scissors? ')
result = rock_paper_scissors()
print('They chose {}'.format(result))

# Roulette
import random

number_choice = int(input('Pick a number from 1-100: '))
colour_choice = input('Pick a colour, red or black: ')
bet = int(input('How much would you like to bet? '))


def colour():
    random_colour = random.randint(1, 2)
    if random_colour == 1:
        colour = 'red'
    else:
        colour = 'black'
    return colour


def number():
    random_number = random.randint(1, 100)
    if random_number == number_choice:
        number = 'win'
    else:
        number = 'lose'
    return number


if number == 'win' and colour == colour_choice:
    print('You win' + str(bet * 100))
elif number == 'win' and not colour == colour_choice:
    print('You win' + str(bet * 2))
elif not number == 'win' and colour == colour_choice:
    print('You keep your bet')
else:
    print('You lose')
