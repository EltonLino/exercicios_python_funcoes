def valor_final(desconto, compra):
    def resultado():
        return f'Preço final com desconto é: {compra - compra * (desconto/100)}'
    print(resultado())
    
desconto = int(input('Digite o porcentual do desconto: '))
compra = float(input('Digite o valor da compra: '))

valor_final(desconto, compra)