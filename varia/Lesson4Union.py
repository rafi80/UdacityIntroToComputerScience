'''
Created on 22 wrz 2013

@author: Stefan
'''


# Define a procedure, union,
# that takes as inputs two lists.
# It should modify the first input
# list to be the set union of the two
# lists. You may assume the first list
# is a set, that is, it contains no 
# repeated elements.

def union(lista1, lista2):
    for x in lista2:
        if x in lista1:
            continue
        else:
            lista1.append(x)
    return lista1

# To test, uncomment all lines 
# below except those beginning with >>>.

a = [1,2,3]
b = [2,4,6]
union(a,b)
print a 
#>>> [1,2,3,4,6]
print b
#>>> [2,4,6]