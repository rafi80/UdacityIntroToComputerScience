def bigger(a,b):
    if a >= b:
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger(bigger(a,b),c)

# def biggest(a,b,c):
#     if a>= b and a >= c:
#         return a
#     else:
#         if a <= b and b>=c:
#             return b
#         else:
#             return c



# def biggest(a,b,c):
#     return max(a,b,c)

print biggest(3, 6, 9)
#>>> 9

print biggest(6, 9, 3)
#>>> 9

print biggest(9, 3, 6)
#>>> 9

print biggest(3, 3, 9)
#>>> 9

print biggest(9, 3, 9)
#>>> 9

print biggest(2, 2, 1)
