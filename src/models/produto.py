from datetime import datetime

class Produto:
    def __init__(self, codigo, nome, quantidade, preco, data_entrada=None):
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco
        self.data_entrada = data_entrada or datetime.now().strftime('%d/%m/%Y')

    def mostrar_informacoes(self):
        print('Código:', self.codigo)
        print('Nome:', self.nome)
        print('Quantidade:', self.quantidade)
        print(f'Preço: R${self.preco:.2f}')
        print('Data de entrada:', self.data_entrada)
