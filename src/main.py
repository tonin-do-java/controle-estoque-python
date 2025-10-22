from controllers.estoque_controller import (
    carregar_estoque,
    adicionar_produto,
    listar_produtos,
    atualizar_quantidade,
    remover_produto,
    gerar_relatorio
)

def menu():
    print("""
========== MENU ==========
1. Adicionar Produto
2. Listar Produtos
3. Atualizar Quantidade
4. Remover Produto
5. Gerar Relatório
6. Sair
==========================
""")

def main():
    estoque = carregar_estoque()

    while True:
        try:
            menu()
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Digite apenas números!")
            continue

        if opcao == 1:
            c = input('Código: ')
            n = input('Nome: ')
            q = int(input('Quantidade: '))
            p = float(input('Preço: '))
            adicionar_produto(estoque, c, n, q, p)

        elif opcao == 2:
            listar_produtos(estoque)

        elif opcao == 3:
            cod = input('Código do produto: ')
            tipo = int(input('1. Adicionar | 2. Retirar: '))
            q = int(input('Quantidade: '))
            if tipo == 1:
                atualizar_quantidade(estoque, cod, 'adicionar', q)
            elif tipo == 2:
                atualizar_quantidade(estoque, cod, 'retirar', q)
            else:
                print('Opção inválida!')

        elif opcao == 4:
            cod = input('Código do produto: ')
            remover_produto(estoque, cod)

        elif opcao == 5:
            gerar_relatorio(estoque)

        elif opcao == 6:
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
