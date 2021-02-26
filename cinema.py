print('\nSejam bem viados ao nosso clube!\n')

nome = input('Digite seu nome: \n- ')

py_student = input(f'\nOlá {nome}!\nVocê é estudante de Python? \nDigite "sim", ou "não": \n- ').lower()

idade = int(input('\nDigite sua idade: \n- '))


if idade >= 18 and py_student == 'sim':
    print('\nEscolha seu ingresso: \n1. Padrão: R$ 17,50 (50% OFF) \n2.    VIP: R$ 30,00 (50% OFF)')
    input('Digite 1 ou 2:\n- ')
    print('\nIngresso reservado. Boa Festa!!!\n')

else:
    if not idade < 18 and py_student == 'sim':
            print('\nEscolha seu ingresso: \n1. Padrão: R$ 35,00 \n2.    VIP: R$ 60,00')
            input('Digite 1 ou 2:\n- ')
            print('\nIngresso reservado. Boa Festa!!!\n')
            

    elif idade < 18:
        ano = 'anos'
        if idade == 1:
            ano = 'ano'
        print(f'\nFaltam {18 - idade} {ano} para você ter acesso ao clube. Estaremos aqui te aguardando!')


