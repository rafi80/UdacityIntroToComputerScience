

# My
def find_last(whole_string, searched_string):

    found_index = 0
    current_max = -1
    while found_index <= len(whole_string):
        if whole_string.find(searched_string, found_index) >= found_index:
            found_index = whole_string.find(searched_string,found_index)
            current_max = found_index
        found_index += 1

    return current_max


# Udacity
def find_last_udacity(whole_string, searched_string):

    last_pos = -1
    while True:
        pos = whole_string.find(searched_string, last_pos+1)
        if pos == -1:
            return last_pos
        last_pos = pos


string = "Ala ma kota"
string2 = "Kala lala lala baka"

#print string2.find('la',3)

print find_last('aaaa', 'a')
#>>> 3
print find_last('aaaaa', 'aa')
#>>> 3
print find_last('aaaa', 'b')

print find_last('222222222','')

#print '222222222'.rfind('')



#print find_last('aaaa', 'a')
#>>> 3

#print find_last('aaaaa', 'aa')
#>>> 3

#print find_last('aaaa', 'b')
#>>> -1

#print find_last("111111111", "1")
#>>> 8

#print find_last("222222222", "")
#>>> 9

#print find_last("", "3")
#>>> -1

#print find_last("", "")
#>>> 0