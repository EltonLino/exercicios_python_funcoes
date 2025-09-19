def numero_par(n):
    return n % 2 == 0

numeros = input('Digite os números separados por espaço: ').split()
numeros_convertidos = list(map(int, numeros))
numeros_pares = list(filter(numero_par, numeros_convertidos))
print('Números pares: ',end='')
for numero in numeros_pares:
    print(numero, end=' ')

print('\n------Solução do instrutor------')

numeros = input("Digite os números separados por espaço: ").split() 
pares = filter(lambda x: int(x) % 2 == 0, numeros) 
print("Números pares:", " ".join(pares)) 