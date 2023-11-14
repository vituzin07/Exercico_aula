#questão 1
a = int(input('Insira o primeiro valor (a): '))
b = int(input('Insira o segundo valor (b): '))
operacao = input('Insira a operação (+, -, *, /): ')
match operacao:
    case '+':
        print(f'{a} + {b} = {a + b}')
    case '-':
        print(f'{a} - {b} = {a - b}')
    case '*':
        print(f'{a} * {b} = {a * b}')
    case '/':
        print(f'{a} / {b} = {a / b}')
    case other:
        print('Está operação não é válida.')
# questão 2
print(''' Escolha um jogo:
 1 - Overwacth
 2 - Call of duty
 3 - GTA V
 4 - Minecraft
 5 - Diablo IV''')
Jogo = int(input('Insira o número do jogo correspondente ao qual você deseja: '))
match Jogo:
    case 1:
        print('Você é uma pessoa triste')
    case 2: 
        print('Já foi um bom jogo')
    case 3: 
        print('Muito bom')
    case 4:
        print('QUADRADO')
    case 5:
        print('Deus é mais')
    case other:
        print('TEM NÃO.')
