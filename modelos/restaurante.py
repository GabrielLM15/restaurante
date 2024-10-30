from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.title()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'

    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome:'.ljust(25)} |{'Categoria:'.ljust(25)} |{'Avaliação:'.ljust(25)} |{'Disponível:'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} |{restaurante._categoria.ljust(25)} |{str(restaurante.media_avaliacoes).ljust(25)} |{restaurante.ativo}')

    @property
    def ativo(self):
        return '☑' if self._ativo else '☒'

    def alterar_estado(self):
        self._ativo = not self._ativo

    def receber_avalicao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '--'
        soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_notas = len(self._avaliacao)
        media = soma_notas/quantidade_notas
        return media

    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        print(f'Cardápio do restaurante {self._nome}')
        for i, item in enumerate(self._cardapio, start=1):
            if hasattr(item, 'descricao'):
                mensagem_prato = f'{i}. Nome: {item._nome.ljust(20)} | Preço: R${str(item._preco).ljust(20)} | Descrição: {item.descricao}'
                print(mensagem_prato)
            elif hasattr(item, 'tamanho'):
                mensagem_bebida = f'{i}. Nome: {item._nome.ljust(20)} | Preço: R${str(item._preco).ljust(20)} | Tamanho: {item.tamanho}'
                print(mensagem_bebida)
            else:
                mensagem_sobremesa = f'{i}. Nome: {item._nome.ljust(20)} | Preço: R${str(item._preco).ljust(20)} | Tipo: {item.tipo} | Tamanho: {item.tamanho} | Descrição: {item.descricao}'
                print(mensagem_sobremesa)





    