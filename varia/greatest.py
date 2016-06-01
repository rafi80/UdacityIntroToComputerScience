'''
Created on 22 wrz 2013

@author: Stefan
'''
#===============================================================================
# def greatest(list_of_numbers):
#     biggest = []
#     for x in list_of_numbers:
#         biggest.append(list_of_numbers.pop())
#         if x>biggest[0]:
#             biggest[0]=x
#         else:
#             continue
#     if len(biggest)>0:
#         return biggest[0]
#     else:
#         return 0
#===============================================================================

def greatest(p):
    big=0
    for i in p:
        if i > big:
            big = i
    return big 


print greatest([4,23,1])
#>>> 23
print greatest([1,2,3])
#>>> 0