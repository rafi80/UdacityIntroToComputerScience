def collatz(c):
    while c > 1:
        if c % 2:
            c = 3 * c + 1
        else:
            c /= 2
        yield c

for i in collatz(99999999991999999991999999999999999999999999999999999999999999999999999999999999):
    print i