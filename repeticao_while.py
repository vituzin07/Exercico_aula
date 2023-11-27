# fim = int(input ('Digite um número: '))
# x = 0
# while x <= fim  :
#     print(x)
#     x = x + 2

# qtd_notas = int(input('Quantas notas? '))
# n = 1 
# soma = 0
# while n<=qtd_notas:
#     nota = float(input(f' Digite {n}ª nota:'))
#     soma = soma + nota
#     n = n + 1
# print(f'Média: {soma/qtd_notas}')
# print('''1- Sanduíche
# 2- Pizza
# 3- Milkshake''')
# pedido = ''
# while True:
#     x = int(input('Escolha seu pedido ou 0 para finalizar: ' ))
#     match x:
#         case 0:
#             break
#         case 1:
#             pedido = pedido + 'Sanduíche\n'
#         case 2:
#             pedido = pedido + 'Pizza\n'
#         case 3:
#             pedido = pedido + 'Milkshake\n'
            
# print(f'Seu pedido: {pedido}')

tabuada = 1
while tabuada <= 9:
    numero = 1
    while numero <= 9:
        print(f'{tabuada}.{numero}={tabuada*numero}')
        numero+=1
    print('\n')
    tabuada+=1