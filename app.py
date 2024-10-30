from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa

padaria = Restaurante('Padaria Brasil Novo', 'Padaria')
padaria.alterar_estado()
padaria.receber_avalicao('João', 5)


bebida_suco = Bebida('Suco de Laranja', 5.00, 'Grande')
prato_pao = Prato('Pão', 2.00, 'O melhor da cidade')
sobremesa_bolo = Sobremesa('Bolo de chocolate', 25.00, 'Bolo', 'Médio', 'Delicioso bolo de chocolate com calda de chocolate')

padaria.adicionar_no_cardapio(bebida_suco)
padaria.adicionar_no_cardapio(prato_pao)
padaria.adicionar_no_cardapio(sobremesa_bolo)

def main():
    padaria.exibir_cardapio
    print('---------------------------------------------------------------')
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()