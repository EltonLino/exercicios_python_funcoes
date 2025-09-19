telefones = ["11987654321", "21912345678", "31987654321", "11911223344"]
telefones_convertidos = []

def converter_str_para_int(telefones):
    for telefone in telefones:
        telefones_convertidos.append(int(telefone))

def verificar_conversao(telefones_convertidos):
    for telefone in telefones_convertidos:
        if not isinstance(telefone, int):
            print('Falha na conversão')
            break
    print('Todos os números foram convertidos corretamente')

converter_str_para_int(telefones)
verificar_conversao(telefones_convertidos)
