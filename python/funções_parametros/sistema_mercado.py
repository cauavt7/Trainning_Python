# Função para adicionar produto
def adicionar_produto():
    nome = input("Nome do produto: ")
    preco = float(input("Preço do produto: "))
    return {"nome": nome, "preco": preco}


def mostrar_carrinho(carrinho):
    if len(carrinho) == 0:
        print("\nCarrinho vazio!")
    else:
        print("\n--- Carrinho ---")
        for i, item in enumerate(carrinho):
            print(f"{i+1}. {item['nome']} - R${item['preco']:.2f}")


def calcular_total(carrinho):
    total = 0
    for item in carrinho:
        total += item["preco"]
    return total


def sistema_mercado():
    carrinho = []

    while True:
        print("\n=== MENU ===")
        print("1 - Adicionar produto")
        print("2 - Ver carrinho")
        print("3 - Finalizar compra")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            produto = adicionar_produto()
            carrinho.append(produto)

        elif opcao == "2":
            mostrar_carrinho(carrinho)

        elif opcao == "3":
            mostrar_carrinho(carrinho)
            total = calcular_total(carrinho)
            print(f"\nTotal da compra: R${total:.2f}")
            print("Compra finalizada!")
            break

        elif opcao == "0":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida!")


# Executar sistema
sistema_mercado()