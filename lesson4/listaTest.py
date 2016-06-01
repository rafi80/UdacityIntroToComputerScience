'''
Created on 9 lut 2014

@author: Stefan
'''

def pobierz(lista, value):
    for element in lista:
        if element[0] == value:
            return lista.index(element)   


lista = [['element1',['bal1','bal2']],['element2',['lab1', 'lab2','lab3']]]
lista2 = [['elem1',['bl1','bl2']],['elem2',['lb1', 'lb2','lb3']]]

#print lista.index('element2')

#===============================================================================
# if 'element2' in lista[0]:
#     print "chaka chaaa!"
#===============================================================================    

wynik = pobierz(lista, 'element2')

print wynik

     
  
     
