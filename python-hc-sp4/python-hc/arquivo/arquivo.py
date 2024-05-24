# arquivo.py
def arquivoExiste(nome):
    """Verifica se um arquivo existe."""
    try:
        with open(nome, 'rt') as arquivo:
            return True
    except FileNotFoundError:
        return False

def criarArquivo(nome):
    """Cria um arquivo."""
    try:
        with open(nome, 'wt+') as arquivo:
            print(f'Arquivo {nome} criado com sucesso!')
    except Exception as e:
        print(f'Houve um erro na criação do arquivo: {e}')

def cadastrar(arq, nome="desconhecido", idade=0):
    """Cadastra um novo paciente no arquivo."""
    try:
        with open(arq, 'a') as arquivo:
            arquivo.write(f'{nome};{idade}\n')
            print(f'Novo registro de "{nome}" adicionado.')
    except Exception as e:
        print(f'Houve um erro ao cadastrar o paciente: {e}')

def ler_dados_pacientes(arq):
    """Lê os dados dos pacientes do arquivo e retorna um dicionário."""
    pacientes = {}
    try:
        with open(arq, 'r') as arquivo:
            for linha in arquivo:
                nome, idade = linha.strip().split(';')
                if nome not in pacientes:
                    pacientes[nome] = {'idade': int(idade), 'exames': []}
    except Exception as e:
        print(f'Houve um erro ao ler os dados dos pacientes: {e}')
    return pacientes