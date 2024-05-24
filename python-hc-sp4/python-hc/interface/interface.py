def mostrar_opcoes_exames():
    """Mostra as opções de exames disponíveis."""
    print("\n=== Opções de Exames ===")
    print("1. Hemograma Completo")
    print("2. Raio-X")
    print("3. Radiografia")

def exibir_informacoes_exame(opcao):
    """Exibe informações sobre o exame selecionado."""
    if opcao == 1:
        print("\n--- Hemograma Completo ---")
        print("Avalia as células sanguíneas, incluindo glóbulos vermelhos, glóbulos brancos e plaquetas.")
        print('O hemograma avalia as informações sobre\nos tipos e quantidades dos componentes no sangue')
        print('\033[34mhttps://techdobem.com.br/examedesangue\033[m \n')
        print('\n\033[31muma Imagem com a cor vermelha\n\033[m')
    elif opcao == 2:
        print('Raio-X é um exame que usa radiação ionizan44te\npara captar imagens internas de diferentes partes do corpo')
        print('\033[34mhttps://techdobem.com.br/raiox\033[m \n')
        print('\033[34muma Imagem com a cor azul\n\033[m')
    elif opcao == 3:
        print('A radiografia é o método de exame de imagem mais\nprontamente disponível. Tipicamente, é o primeiro\nmétodo de imagem indicado para avaliação de\nextremidades, tórax e algumas vezes coluna e abdome.')
        print('\033[34mhttps://techdobem.com.br/rediografia\033[m \n')
        print('\033[33mUma Imagem com a cor amarela\n\033[m')
    else:
        print("Opção inválida!")

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro valido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuario preferiu não digitar esse número\033[m')
            return 0
        else:
            return n


def linha(tam = 42):
    return'-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

# a cada funcionalidade nova criada, sempre testar antes de fazer a proxima 
# nunca fazer ela toda para depois testar 
def menu(lista):
    cabecalho('Menu Principal')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1 
    print(linha())
    opc = leiaInt('\033[32mSua opção: \033[m')
    return opc
