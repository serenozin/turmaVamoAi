def media (alunos):
    """Função que retorna a média dos números de uma lista"""
    
    media = sum(alunos) / len(alunos) 
    # 'sum()'vai retornar a soma de todos os números da lista 
    # 'len()' vai retornar a quantidade de elementos da lista
    return print(f'\nA média da turma é {media}\n')

alune1 = 5
alune2 = 6
alune3 = 8
alune4 = 3
alune5 = 9

media([alune1, alune2, alune3, alune4, alune5])