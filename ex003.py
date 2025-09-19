def saudacao(hora):
    if hora < 12:
        return 'Bom dia'
    if 12 >= hora < 18:
        return 'Boa tarde'
    if hora >= 18:
        return'Boa noite'
    
hora = int(input('Digite a hora atual (0-23): '))
print(saudacao(hora))