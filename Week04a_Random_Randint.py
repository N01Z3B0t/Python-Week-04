'''
Created on Feb 4, 2019
    Random Numbers - Craps Roller Program
    
    Use randint() and randrange() - returns an integer random number
    Demonstrate random number generation
    
    1) Import random - import statement allows you to import or load modules
    
    2) Modules - are files that contian codes that are grouped together that are meant to be used in other programes, eg random
    
    3) moduleName.functionName() -> eg random.randrange(6)
    
    4) randint(start,end) -> die starts at 1 and ends with 6
    
    5) randrange(n)-> returns a range of number from 0 to (n - 1)
                -> num = random.randrange(10)    1 2 3 4 5 6 7 8 9
                -> num = random.randrange(5,10)    5 6 7 8 9
                -> num = random.randrange(0, 101, 10)     0 10 20 ...90 100  
                                        start end step
                
    
@author: Ernie Reynoso
'''

#import libraries
import random

#generate random number 1 - 6
die1=random.randint(1,6)
die2=random.randrange(6)+1 #range shifts from 0 to 5 to 1 to 6

total=die1+die2

print("You rolled a", die1, "and a", die2, "for a total of", total)

''' output 

You rolled a 4 and a 1 for a total of 5

'''









