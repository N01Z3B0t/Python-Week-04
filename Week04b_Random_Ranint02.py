'''
Created on May 30, 2019

@author: noizebot

'''

#Student Name
#Sutdent ID
#Description
BOARDER='*********************************'

import random

print(BOARDER)
print('Guess my number between 1 to 100') 
print(BOARDER)

#input/set initial values
myNumber=random.randint(1,100)
guess=int(input('\nTake a guess '))
tries=1

#Processing
while guess != myNumber:
    if guess>myNumber:
        print('Lower...\n')
        tries+=1
    else:
        print('Higher...\n')
        tries+=1

    guess=int(input('Take a guess '))

print('\n')
print(BOARDER)
print('You guessed it!  The number is ', myNumber)
print('You took', tries, 'tries')

# OUTPUT
# *********************************
# Guess my number between 1 to 100
# *********************************
# 
# Take a guess 1
# Higher...
# 
# Take a guess 2
# Higher...
# 
# Take a guess 3
# Higher...
# 
# Take a guess 4
# Higher...
# 
# Take a guess 5
# Higher...
# 
# Take a guess 99
# Lower...
# 
# Take a guess 50
# Higher...
# 
# Take a guess 75
# Higher...
# 
# Take a guess 80
# Higher...
# 
# Take a guess 85
# Higher...
# 
# Take a guess 90
# Higher...
# 
# Take a guess 91
# Higher...
# 
# Take a guess 92
# 
# 
# *********************************
# You guessed it!  The number is  92
# You took  13  tries
# *********************************

