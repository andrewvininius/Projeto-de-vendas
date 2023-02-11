#carinho de compra e menu
carrinho = []
print("""
Menu
0 - Finalizar programa
1 - Adicionar produto
2 - Ver carrinho
3 - Confirma produto
4 - Ver total
0 - sair
""")
#escolhas de opcoes
escolha = input('Escolha uma opção: ')

while escolha != 0:
    if escolha == 1:
        item = input('Adicionado Produto: ')
        if item in carrinho:
            print('Produto já está no carrinho:')
            x = int(input('Deseja mudar a quantidade? 1 para sim, 2 para não:'))
            if x == 1:
                novaquantidade = int(input('Informe a nova quantidade do produto:'))
                item = 0
                quantidade = novaquantidade
                input(item)
        else:
            quantidade = int(input("Entre a quantidade: "))
            carrinho.append(item)


    if escolha == 2:
        print("Exibindo produtos...")
        contador = 0
        for item in carrinho:
            print(contador,item,":",quantidade)
            contador = contador + 1

    if escolha == 3:
        posicao = int(input(f'Digite a posição do item'))
        posicao_int = int(posicao)
        preco = input(f"Digite o preço do produto {carrinho[posicao_int][1]}")
        carrinho[item] = "OK"
        carrinho[posicao][3] = preco
    escolha = int(input("Escolha mais uma opção: "))



else:
   print("Programa encerrado")