'''
Created on 5 paz 2013

@author: Stefan
'''
def iteracja(lista):                
    i = 0
    j = 0
    for i in range(len(lista)):
        for j in range(len(lista)):
            print lista[i][j]
            
def is_integer(a):
    t = int(a)
    return t
        
correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

iteracja(correct)

print is_integer('a')