def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError: #exeção
        return False
    else:
        return True
    


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um Erro na criação do arquivo')
    else:
        print(f'arquivo {nome} criado com sucesso!')


def cadastrar(arq, nome="desconhecido", idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome}; {idade}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo registro de "{nome}" adicionado.')
            a.close()
