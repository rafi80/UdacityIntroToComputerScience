'''
Created on 9 lut 2014

@author: Stefan
'''

index = []

#Moje
#===============================================================================
# def add_to_index(index,keyword,url):
#     listaKeywordow = []
#     for element in index:
#         listaKeywordow.append(element[0])
#     if keyword in listaKeywordow:
#         index[getIndexOfValue(index, keyword)][1].append(url)
#     else:
#         index.append([keyword,[url]])
#     
# def getIndexOfValue(lista, value):
#     for element in lista:
#         if element[0] == value:
#             return lista.index(element)
#===============================================================================
#Udacity            
def add_to_index(index,keyword,url):
    for element in  index:
        if element[0] ==keyword:
            element[1].append(url)
            return
    index.append([keyword,[url]])  

    
add_to_index(index,'udacity','http://udacity.com')
add_to_index(index,'computing','http://acm.org')
add_to_index(index,'udacity','http://npr.org')
print index
#>>> [['udacity', ['http://udacity.com', 'http://npr.org']], 
#>>> ['computing', ['http://acm.org']]] 