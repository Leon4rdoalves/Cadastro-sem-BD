from cadastro.lib.interface import *


def arquivoexiste(ficha):
    try:
        arquivo = open(ficha, 'rt')
        arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criandoarquivo(ficha='ficha'):
    try:
        arquivo = open(ficha, 'wt+')
        arquivo.close()
    except:
        print('Encontramos um erro ao criar o arquivo!')
    else:
        print(f'\033[31mArquivo {ficha} criado com sucesso!\033[m')


def lerarquivo(ficha='ficha'):
    try:
        arquivo = open(ficha, 'rt')
    except:
        print('Encontramos um erro ao ler o arquivo!')
    else:
        subtitulo('Pessoas Cadastradas')
        for l in arquivo:
            dado = l.split(';')
            dado[4] = dado[4].replace('\n', '')
            print(f' {dado[0]:<27}\033[33m|\033[m {dado[1]:^6}\033[33m|\033[m{dado[2]:^6}'
                  f'\033[33m|\033[m{dado[3]:^8}\033[33m|\033[m {dado[4]}')
    finally:
        arquivo.close()
    linha(cor=33)


def cadastro(ficha='ficha', nome='Não informado!', idade=0, sexo='N/S', estado='N/S', cidade='N/S'):
    try:
        arquivo = open(ficha, 'at')
    except:
        print('Erro ao abrir o arquivo.')
    else:
        try:
            arquivo.write(f'{nome};{idade};{sexo};{estado};{cidade}\n')
        except:
            print('Erro ao escrever o arquivo.')
        else:
            print(f'\033[33m{nome} adicionado com sucesso!\033[m')
            arquivo.close()
