# questão 1

a = int(input("Insira o primeiro valor inteiro: "))
b = int(input("Insira o segundo valor inteiro: "))
if a>b:
    print(f'{a} é maior que {b}')
if b>a:
    print(f'{b} é maior que {a}')

# questão 2

velocidade = float(input("Insira a velocidade: "))  
if velocidade>80:
    multa= (velocidade-80)*5.0
    print(f'Você terá que pagar R$ {multa} ')

# questão 3

velocidade = float(input('Insira a velocidade: '))
valor_80 = 0
valor_140 = 0
if velocidade>80 and velocidade<140:
    valor_80 = (velocidade - 80)*5.0
    print(f'Multado no valor de R$ {valor_80}')
if velocidade > 140:
    valor_80 = (140-80)*5.0
    valor_140 = (velocidade-140)*8.0
    print(f'Multado no valor de R$ {valor_80 + valor_140}')