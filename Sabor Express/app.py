import os

restaurantes = [{'nome': 'Praça', 'categoria': 'Italiano', 'ativo' :False}, 
                {'nome': 'Pizza Suprema', 'categoria': 'Pizza', 'ativo' :True}, 
                {'nome': 'Sabor do Mar', 'categoria': 'Japones', 'ativo' :False}]


def texto(msg):
    """ Essa função tem a responsabilidade de exibir um texto formatado no console"""

    print('-' * 30)
    print(msg.center(30))
    print('-' * 30)


def voltar_menu():
    """ Essa função tem a responsabilidade de exibir uma mensagem para o usuário e voltar para o menu principal"""

    input('Digite uma tecla para voltar ao menu principal...')
    main()


def exibir_subtitulo(msg):
    """ Essa função tem a responsabilidade de exibir um subtítulo formatado no console"""

    os.system('cls')
    texto(msg)
    

def finalizar_app():
    """ Essa função tem a responsabilidade de finalizar o programa exibindo uma mensagem para o usuário"""

    os.system('cls')
    texto('Sair do programa')


def opcao_invalida():
    """ Essa função tem a responsabilidade de exibir uma mensagem para o usuário quando ele escolher uma opção inválida no menu"""

    print('Opção inválida. Tente novamente.\n')
    input('Digite uma tecla para voltar ao menu principal...')     
    main()


def exibir_nome_do_programa():
    """ Essa função tem a responsabilidade de exibir o nome do programa formatado no console"""
    print('-' * 30)
    print('𝕊𝕒𝕓𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤'.center(30))
    print('-' * 30)


def exibir_menu():
    """ Essa função tem a responsabilidade de exibir o menu principal do programa para o usuário"""
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar status do restaurante')
    print('4. Sair do programa\n')


def cadastrar_restaurante():
    """ Essa função tem a responsabilidade de cadastrar um novo restaurante
    Inputs: 
    - nome do restaurante
    - categoria do restaurante
    Outputs:
    - Adiciona um novo restaurante a lista de restaurantes
    """

    exibir_subtitulo('Cadastrar restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria_restaurante = input(f'Digite o nome da categoria do restaurante {nome_restaurante}: ')
    dados_do_restaurante = {'nome': nome_restaurante, 
                            'categoria': categoria_restaurante, 
                            'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!')
    voltar_menu()


def listar_restaurantes():
    """ Essa função tem a responsabilidade de listar os restaurantes cadastrados"""

    exibir_subtitulo('Lista de restaurantes')
    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Status'}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo_restaurante = 'Ativo' if restaurante['ativo'] else 'Inativo'
        print(f'- {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo_restaurante}')  
    voltar_menu()


def alternar_status_restaurante():
    """ Essa função tem a responsabilidade de alternar o status de um restaurante entre ativo e inativo"""

    exibir_subtitulo('Alternando status do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja ativar/desativar: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem_status = f'O restaurante {nome_restaurante} foi ativado com sucesso!'  if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!'
            print(mensagem_status)
    if not restaurante_encontrado:
        print(f'O restaurante {nome_restaurante} não foi encontrado. Tente novamente.')
    voltar_menu()


def escolher_opção():
    """Essa função tem a responsabilidade de receber a opção escolhida pelo usuário e chamar a função correspondente"""

    try:
        opcao_escolhida = int(input('Digite a opção desejada: '))

        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_status_restaurante()   
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()


def main():
    """Essa função tem a responsabilidade de iniciar o programa exibindo o nome do programa e o menu para o usuário"""
    
    os.system('cls')
    exibir_nome_do_programa()
    exibir_menu()
    escolher_opção()


if __name__ == '__main__':
    main()
