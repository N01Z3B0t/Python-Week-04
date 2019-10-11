'''
Created on Feb 6, 2019

@author: noizebot
'''



'''
Find the sum and average
of a series of numbers entered by the user.
Use a flag or sentinel
to stop the loop
'''
BOARDER='*********************************'

#initialization
sum=0
count=0

print(BOARDER)
print('Sum and Average program')
print('\n')

#input
num=float(input('Enter a number '))

while num!=-999:
    sum+=num
    count+=1
    num=float(input('Enter a number '))

if count!=0:
    avg=sum/count
    print('###############################')
    print('The sum is ', sum)
    print('The average is ', avg)
    print('\n')
    print(BOARDER)
else:
    print('Divide by 0 error')
    print('\n')
    print(BOARDER)
    
#Test Case Output
# Sum and Average program
# 
# 
# Enter a number 4
# Enter a number 3
# Enter a number 2
# Enter a number 1
# Enter a number 4
# Enter a number 3
# Enter a number 4
# Enter a number 3
# Enter a number 4
# Enter a number -999
# ###############################
# The sum is  28.0
# The average is  3.111111111111111
# 
# 
# *********************************
