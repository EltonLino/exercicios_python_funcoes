num_1 = int(input('Digite o primeiro número: '))
num_2 = int(input('Digite o segundo número: '))
op = input('Escolha a operação (| + | - | * | / |): ')

match op:
    case '+':
        res = lambda x, y: x + y
        print(f'O resultado é: {res(num_1, num_2)}')
    case '-':
        res = lambda x, y: x - y
        print(f'O resultado é: {res(num_1, num_2)}')
    case '*':
        res = lambda x, y: x * y
        print(f'O resultado é: {res(num_1, num_2)}')
    case '/':
        res = lambda x, y: x / y
        print(f'O resultado é: {res(num_1, num_2)}')
