def total_de_vendas(lista):
    soma = 0
    for venda in lista:
        venda_convertida = float(venda)
        soma += venda_convertida
    return print(f'O total de vendas foi: {soma}')


vendas = input('Digite os valores das vendas: ')
lista_de_vendas = vendas.split()
total_de_vendas(lista_de_vendas)

print('-----Solução do instrutor-------')

valores = input("Digite os valores das vendas: ").split() 
total = sum(map(float, valores)) #Função map() -> converte os valores digitados e função sum() soma todos eles 
print(f"O total de vendas foi: {total}") 