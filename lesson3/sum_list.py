# -*- coding: utf-8 -*-

# Sumowanie wszystkich elementów listy

lista = [1,2,3,5,7]

def sum_list(list):
    suma = 0
    for element in list:
        suma = suma+element
    return suma


print sum_list(lista)