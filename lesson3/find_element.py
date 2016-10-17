



#My
def find_element(list, element_to_find):
    index = 0
    for e in list:
        if e == element_to_find:
            return index
        index += 1
    return -1

#Udacity
def find_element2(p, t):
    i = -1
    while i < len(p):
        if p[i] == t:
            return i
        i=i+1
    return -1

#z uzciem indexu. Rzuca wyjatek, jezeli nie ma elementu
def find_element_index(p,t):
    if t in p:
        return p.index(t)
    else:
        return -1

lista1=[1,2,3,4]
lista2 = [2,3,4]
lista3 = [3,1,1]

print find_element(lista1,1)
print find_element(lista2,1)
print find_element(lista3,1)

print find_element_index(lista1,1)
print find_element_index(lista2,1)
print find_element_index(lista3,1)