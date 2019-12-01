from cadastro.lib.interface import *
from cadastro.lib.arquivo import *
from time import sleep

ficha = 'ficha'

if not arquivoexiste(ficha):
    criandoarquivo('ficha')

titulo('Cadastro de Usuários')
while True:
    resp = menu(['Novo Cadastro', 'Visualizar Cadastros', 'Sair do Sistema'])

    if resp == 1:
        titulo('Novo Cadastro')
        nome = str(input('Nome: ')).title()
        idade = linteiro('Idade: ')
        sexo = str(input('Sexo [M . F]: ')).upper()
        estado = str(input('Estado: ')).upper()
        cidade = str(input('Cidade: ')).title()
        cadastro(ficha, nome, idade, sexo, estado, cidade)
        linha(cor=33)

    elif resp == 2:
        lerarquivo('ficha')
        titulo('Cadastro de Usuários')
    elif resp == 3:
        print()
        frase('Por favor, aguarde enquanto finalizamos o sistema.')
        sleep(2)
        titulo('Sistema Encerrado!')
        frase('@ebony_prog', cor=31)
        break
    else:
        print('\033[1;31m Opção inválida! Tente: \033[m\n')
    sleep(1)
