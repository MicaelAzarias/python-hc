from interface.interface import *
from arquivo.arquivo import *
from time import sleep

cabecalho('Chatbot HC/ICr')


acoesUsuario = []
arq = 'listaPacientes.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Exame de Sangue', 'Raio-X', 'Radiografia','Cadastro de Paciente', 'Sair do chat'])
    if resposta == 1:
        cabecalho('Exame de Sangue')
        acoesUsuario.append('Visualizou exame')
        print('O hemograma avalia as informações sobre\nos tipos e quantidades dos componentes no sangue')
        print('\033[34mhttps://techdobem.com.br/examedesangue\033[m \n')
        print('\n\033[31muma Imagem com a cor vermelha\n\033[m')
    elif resposta == 2:
        cabecalho('Raio-x')
        acoesUsuario.append('Visualizou exame')
        print('Raio-X é um exame que usa radiação ionizante\npara captar imagens internas de diferentes partes do corpo')
        print('\033[34mhttps://techdobem.com.br/raiox\033[m \n')
        print('\033[34muma Imagem com a cor azul\n\033[m')
    elif resposta == 3:
        cabecalho('Radiografia')
        acoesUsuario.append('Visualizou exame')
        print('A radiografia é o método de exame de imagem mais\nprontamente disponível. Tipicamente, é o primeiro\nmétodo de imagem indicado para avaliação de\nextremidades, tórax e algumas vezes coluna e abdome.')
        print('\033[34mhttps://techdobem.com.br/rediografia\033[m \n')
        print('\033[33mUma Imagem com a cor amarela\n\033[m')
    elif resposta == 4:
        cabecalho('Novo Cadastro')
        acoesUsuario.append('Visualizou exame')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 5:
        cabecalho('saindo do sistema... Até logo!')
        acoesUsuario.append('Visualizou exame')
        print(f"O total de interação do usuario foi: {item + 1}")
        break
    else:
        print('\033[31mErro! Digite uma opção válida!\033[m')
    
    for item in range(len(acoesUsuario)):
        pass
    sleep(4)