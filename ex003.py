def saudacao(hora):
    if hora < 12:
        return 'Bom dia'
    elif 12 > hora < 18:
        return 'Boa tarde'
    else:
        return'Boa noite'
    
hora = int(input('Digite a hora atual (0-23): '))
print(saudacao(hora))