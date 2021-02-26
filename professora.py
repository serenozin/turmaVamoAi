def situacao_alune(media):
    situacao = ''
    if not media < 7:
        situacao = 'Você está aprovada!\n'
    elif media < 7 and media > 3: 
        situacao = 'Você está de recuperação.\n'
    elif media <= 3:
        situacao = 'Você está reprovada.\n'    
    return  situacao

def media_alune(notas):
    media = sum(notas) / len(notas)
    return media


nome = input('Insira seu nome:\n- ')
print(f'\nOlá, {nome.capitalize()}!\n')
nota1 = input('Insira sua nota de Python:\n- ')
nota2 = input('Insira sua nota de R:\n- ')
nota3 = input('Insira sua nota de Estatística:\n- ')
print('='*35)

notas = [float(nota1), float(nota2), float(nota3)]
print(f'\nEstudante: {nome.capitalize()}')
print(f'\nPython = {nota1}')
print(f'R = {nota2}')
print(f'Estatística = {nota3}')
        
media = media_alune(notas = notas)
print('\nMÉDIA = {:.2f}\n'.format(media))
situacao = situacao_alune(media= media)
print(situacao)
