'''Week04 Feb 6, 2019
@author: noizebot
'''

'''Repetition (loops)

    2 main types of loops
    
        1.  while loops:
            conditioned-controlled
                
        2.  for loops:
            counter controlled '''


'''  1.
While loop

    while condition:
        statement1
        statement2
    
    2 parts
    _______
    
        1.  Condition to test True/False
        2.  Statements that are repeated if conditoin is true.
    '''
#Example
#Temperature check program

MAXTEMP = 102.5

temp=float(input("Enter a temperature "))

while temp > MAXTEMP:
    print("Temperature is too high. ")
    print("Turn on air conditioning. ")
    temp=float(input("Enter a temperature "))


print("Temperature is cooler now. ")
print("Check again in 30 minutes. ")


