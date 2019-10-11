'''
Created on Feb 4, 2019
    Write a program to find the gas constant R.
        P*V=(m*R*T)/M
        
        P=1 (atm
        V=44.8l
        m=64g
        M=32.0gm^-1
        T=273Kelvin
        
        R= (MVP)/mT 
@author: noizebot
'''
P=1
V=44.8
m=64
M=32.0
T=273

R= (M*V*P)/(m*T)

print('P is', P,'atm, V is',V,'l, m', m, 'g, M is', M,'gm-1, T=', T,'k')
print('The gas constant R is', R,'atml/mglK')