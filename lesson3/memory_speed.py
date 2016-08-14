# -*- coding: utf-8 -*-

# Obliczanie odległości jaką pokona światło w czasie odpowiedzi
# różnych rodzajów pamięci

#c - predkosc swiatla m / s

c = 300000000


# 1. żarówka jako baza przechowująca jeden bit pamięci
# Ilość danych: 1 Bit
# Koszt za bit: $0,5
# Czas odpowiedzi (opóźnienie): 1 sekunda
# Odległość pokonana przez światło

#Tu wynik w kilometrach, wiec / 1000
zarowka = c * 1 / 1000
print zarowka


# 2. Rejestr w procesorze
# Ilość danych: 1 kByte
# Koszt za bit: $0.001
# Czas odpowiedzi (opóźnienie): 0.4 ns
# Odległość pokonana przez światło

procesor = c * 0.4*10**(-9)
print procesor

# 3. Kość DRAM
# Ilość danych: Kilka Giga
# Koszt za bit: nano$ 0.58 10^-9
# Czas odpowiedzi (opóźnienie): 12ns
# Odległość pokonana przez światło

dram = c * 12*10**(-9)
print dram

# 4. Twardy dysk
# Ilość danych: Kilka Tera
# Koszt za bit: $100 za 8*2**40 Bitów (1TB)
# Czas odpowiedzi (opóźnienie): 7ms
# Odległość pokonana przez światło

# odleglosc w km
dysk = c * 7*10**(-3) / 1000
#Koszt bita na dysku w nano dollarach
kosztBitaDysk = 100.0 * 10**(9)/(8*2**40)
print dysk
print kosztBitaDysk