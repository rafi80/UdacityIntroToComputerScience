
# przypisanie do zmiennej spy obiektu typu lista
spy = [0,0,7]

# przypisanie do zmiennej agent obiektu typu lista / obydwie zmienne agent i spy mają referencję do tego samego obiektu
agent = spy

print agent, spy


# tutaj odbywa się cała MAGIA:
spy = ['bla','bla']

print agent, spy
