fim = int(input ('Digite um número: '))
x = 0
while x <= fim  :
    print(x)
    x = x + 2

qtd_notas = int(input('Quantas notas? '))
n = 1 
soma = 0
while n<=qtd_notas:
    nota = float(input(f' Digite {n}ª nota:'))
    soma = soma + nota
    n = n + 1
print(f'Média: {soma/qtd_notas}')