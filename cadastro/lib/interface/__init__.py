def linteiro(txt):
    """
    Validação simples de número inteiro. Caso inserido valor diferente de inteiro,
    será solitado ao usuário digitar novamente, até que este seja um número inteiro.
    :param txt: Recebe o valor a ser testado pela def.
    :return: Retorna resposta para número inteiro ou erro para não.
    """
    while True:
        try:
            n = int(input(txt))
        except (ValueError, TypeError):
            print('\033[31m Ops! Você não inseriu um número válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[35m Entrada de dados interrompida pelo usuário.\033[m')
            return '-'
        else:
            return n


def linha(tam=72, cor=34):
    print(f'\033[{cor}m_\033[m' * tam, '\n')


def titulo(txt, n=1, cor=30):
    linha()
    print(f'\033[{n};{cor}m{txt.center(72)}\033[m')
    linha()


def subtitulo(txt, cor=33):
    linha()
    print(f'\033[{cor}m{txt.center(72)}\033[m')
    print(f'\033[{cor}m-\033[m' * 72)
    print(f'\033[{cor}m{" Nome":<28}|{" Idade":<2} |{" Sexo":<5} |{" Estado":<6} |{" Cidade":>10}\033[m')
    print(f'\033[{cor}m-\033[m' * 72)


def frase(txt, n=0, cor=34):
    print(f'\033[{n};{cor}m{txt.center(72)}\033[m')


def menu(list):
    cont = 1
    for item in list:
        print(f' {cont}  .  {item}')
        cont += 1
    linha()
    opc = linteiro(' Digite a opção desejada: ')
    return opc
