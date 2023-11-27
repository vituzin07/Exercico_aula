lista1 = [1, 2 , 3 , 4 ,5]
index = 0
while index <= len (lista1) - 1:
    print(lista1[index] * 2)
    lista1[index] = lista1[index]* 2
    index= index +1   