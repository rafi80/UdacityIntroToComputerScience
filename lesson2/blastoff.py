def countdown(number):
    if number > 1:
        while number > 0:
            print number
            number -= 1
        print 'Blastoff!'
    else:
        print "I cannot countdown from a negative number or zero"

countdown(3)
