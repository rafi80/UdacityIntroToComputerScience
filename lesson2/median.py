def bigger(a,b):
    if a > b:
        return a
    else:
        return b


def biggest(a, b, c):
    return bigger(a, bigger(b, c))


def bigger_or_equal(a, b):
    if a >= b:
        return True
    else:
        return False

#  RAF:
# def median(a, b, c):
#
#     result = a
#     if biggest(a, b, c) == a:
#         if bigger_or_equal(b, c):
#             result = b
#         else:
#             result = c
#     if biggest(a, b, c) == b:
#         if bigger_or_equal(a, c):
#             result = a
#         else:
#             result = c
#     if biggest(a, b, c) == c:
#         if bigger_or_equal(b, a):
#             result = b
#         else:
#             result = a
#     return result

# Udacity
# Big Median Small


def median(a, b, c):
    big = biggest(a, b, c)
    if big == a:
        return bigger(b, c)
    if big == b:
        return bigger(a, c)
    else:
        return bigger(a, b)

print(median(1, 2, 3))
#>>> 2

print(median(9,3,6))
# #>>> 6
#
print(median(7,8,7))
# #>>> 7
#
print(median(2,1,3))
# #>>> 2