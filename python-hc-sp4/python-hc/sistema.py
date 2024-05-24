# sistema.py
from interface.interface import *
from arquivo.arquivo import *
from time import sleep

cabecalho('Chatbot HC/ICr')

pacientes = ler_dados_pacientes('listaPacientes.txt')

while True:
    resposta = menu(['Visualizar Exames', 'Cadastrar Paciente', 'Mostrar Pacientes', 'Sair do chat'])
    if resposta == 1:
        mostrar_opcoes_exames()
        opcao_exame = leiaInt("Escolha um exame: ")
        exibir_informacoes_exame(opcao_exame)
        # Implemente a lógica para registrar o exame visualizado pelo paciente
    elif resposta == 2:
        cabecalho('Novo Cadastro')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        if nome in pacientes:
            print("Paciente já cadastrado!")
        else:
            cadastrar('listaPacientes.txt', nome, idade)
            pacientes = ler_dados_pacientes('listaPacientes.txt')  # Atualiza o dicionário de pacientes
    elif resposta == 3:
        cabecalho('Lista de Pacientes')
        for nome, dados in pacientes.items():
            print(f"- {nome}:")
            print(f"  Idade: {dados['idade']}")
            print(f"  Exames: {', '.join(dados['exames']) if dados['exames'] else 'Nenhum'}")
    elif resposta == 4:
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mErro! Digite uma opção válida!\033[m')
    sleep(3)