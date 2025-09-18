def idade(nascimento, ano_atual):
    return f'A idade é {ano_atual - nascimento}'

nascimento = int(input('Digite o ano de nascimento: '))
ano_atual = int(input('Digite o ano atual: '))
print(idade(nascimento, ano_atual))

