import json
from src.models.produto import Produto

ARQUIVO_ESTOQUE = 'src/data/estoque.json'

def salvar_estoque(estoque):
    with open(ARQUIVO_ESTOQUE, 'w', encoding='utf-8') as f:
        json.dump([vars(produto) for produto in estoque], f, ensure_ascii=False, indent=4)

def carregar_estoque():
    try:
        with open(ARQUIVO_ESTOQUE, 'r', encoding='utf-8') as f:
            dados = json.load(f)
            return [Produto(**d) for d in dados]
    except FileNotFoundError:
        return []

def adicionar_produto(estoque, codigo, nome, quantidade, preco):
    if any(produto.codigo == codigo for produto in estoque):
        print('Já existe um produto com esse código!')
        return
    novo_produto = Produto(codigo, nome, quantidade, preco)
    estoque.append(novo_produto)
    salvar_estoque(estoque)
    print('Produto adicionado com sucesso!')

def listar_produtos(estoque):
    if not estoque:
        print('Nenhum produto cadastrado.')
    else:
        for produto in estoque:
            produto.mostrar_informacoes()
            print('-' * 30)

def atualizar_quantidade(estoque, codigo, operacao, quantidade):
    for produto in estoque:
        if produto.codigo == codigo:
            if operacao == 'adicionar':
                produto.quantidade += quantidade
            elif operacao == 'retirar':
                if produto.quantidade >= quantidade:
                    produto.quantidade -= quantidade
                else:
                    print('Estoque insuficiente!')
                    return
            salvar_estoque(estoque)
            print(f'Quantidade atualizada! Nova quantidade: {produto.quantidade}')
            return
    print('Produto não encontrado!')

def remover_produto(estoque, codigo):
    for produto in estoque:
        if produto.codigo == codigo:
            estoque.remove(produto)
            salvar_estoque(estoque)
            print('Produto removido com sucesso!')
            return
    print('Produto não encontrado!')

def gerar_relatorio(estoque):
    if not estoque:
        print('Nenhum produto cadastrado.')
        return
    valor_total = 0
    for produto in estoque:
        produto.mostrar_informacoes()
        valor_item = produto.quantidade * produto.preco
        print(f'Valor total deste item: R${valor_item:.2f}')
        valor_total += valor_item
        print('-' * 30)
    print(f'💰 Valor total em estoque: R${valor_total:.2f}')
