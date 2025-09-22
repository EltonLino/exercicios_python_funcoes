def soma_valores(n):
    if n == 1:
        return 1
    else:
        return n + soma_valores(n-1)


n = int(input('Digite um número: '))
print(f'A soma de 1 a {n} é {soma_valores(n)}')
