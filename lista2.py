lista = [1,2,4,5]
lista.append(6)
lista_final  = lista[:2] + [3] + lista[2:]
print(lista_final)