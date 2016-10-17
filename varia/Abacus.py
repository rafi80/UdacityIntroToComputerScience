'''
Created on 22 wrz 2013

@author: Stefan
'''
def print_abacus(value):
    i=10
    while i>0:
        i-=1
        line = '|00000*****   |'
        if (value // 10**i)>0:
            print line[:10-value // (10**i)+1]+' '*3+line[10-value // (10**i)+1:11] +"|"
            value = value%10**i
        else:
            print line

print_abacus(1236)