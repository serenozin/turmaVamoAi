def saude(exame):
    if exame >= 7:
        print('\nSua saúde está boa, continue assim!')
    
    elif exame < 7 and exame >= 4:
        print('\nSua saúde está mediana, busque se cuidar mais e fazer acompanhamento médico.')
    
    elif exame < 4:
        print('\nSua saúde não está boa, procure a equipe médica.\n')


paciente1 = 7
paciente2 = 5
paciente3 = 2

saude(paciente1)

saude(paciente2)

saude(paciente3)
