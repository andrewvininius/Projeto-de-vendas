#Quando o valor dos produtos adicionados ao carrinho for igual ou superior a R$ 250,00, o frete é grátis.
valor = int(input('valor do produto é para vermos seu frete? '))
if valor >= 1 and valor < 249:
    print('Na compra de R$250,00 você ganha frete gratis!!!')
elif valor >= 250 and valor< 100000 :
    print('Você recebe frete gratis!!!!')
