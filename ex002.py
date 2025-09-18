def contar_caractereres(palavra=0):
    return len(palavra)

palavra = input('Digite uma palavra: ')
caracteres = contar_caractereres(palavra)
print(f'Essa palavra tem {caracteres} caracteres.')