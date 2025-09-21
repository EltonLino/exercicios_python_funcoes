lista_produtos = input('Digite os produtos separados por vírgula: ').strip().split(',')
lista_precos = input('Digite os preços separados por vírgula: ').strip().split(',')

lista_precos = list(map(float, lista_precos)) #converte string em float

produtos_precos = dict(zip(lista_produtos, lista_precos)) # cria um dicionário associando produto com o preço

for produto in lista_produtos:
    print(f'{produto.strip()}: R$ {produtos_precos[produto]:.2f}')
    

print('\n------Solução do instrutor------')


produtos = input("Digite os produtos separados por vírgula: ").split(",") 
precos = input("Digite os preços separados por vírgula: ").split(",") 
 
for produto, preco in zip(produtos, precos): 
    print(f"{produto.strip()}: {preco.strip()}") 