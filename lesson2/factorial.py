def factorial(number):
    i = 1
    factorial_value = 1
    while i < number:
        i = i+1
        factorial_value = factorial_value * i
    return factorial_value


print factorial(7)



