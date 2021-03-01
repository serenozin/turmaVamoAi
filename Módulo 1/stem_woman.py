print('\nVamos ver se você conhece a Marie Curie!\nDigite a letra de uma resposta certa')

print('\n1. Quantos prêmios Nobel ela recebeu?\na - Dois ')
print('b - Um de química e um de física \nc - Um de química')
questao1 = input('Resposta:\n- ')

print('\n2. De onde ela era?\na - Polônia, e naturalizada na França')
print('b - França \nc - Polônia')
questao2 = input('Resposta:\n- ')

print('\n3. Qual foi a causa de sua morte?\na - Exposição à radiação na 1ª Guerra')
print('b - Exposição à radiação num experimento \nc - Tuberculose')
questao3 = input('Resposta:\n- ')

acertos = 0
plural = 'questões'

if questao1 == 'b' or questao1 == 'a':
    acertos += 1
if questao2 == 'c' or questao2 == 'a':
    acertos += 1
if questao3 == 'b' or questao3 == 'a':
    acertos += 1

if acertos == 1:
    plural = 'questão'

if acertos == 0:
    print('\nVocê não acertou nenhuma questão')
else:
    print(f'\nVocê acertou {acertos} {plural}.')

print('''\nMarie Skłodowska Curie foi uma cientista e física polonesa 
naturalizada francesa, que conduziu pesquisas pioneiras em 
todo o mundo no ramo da radioatividade. Foi a primeira mulher a 
ser laureada com um Prêmio Nobel[2], a primeira pessoa e única 
mulher a ganhar o prêmio duas vezes e até hoje é a única pessoa 
a ganhar o Nobel em duas áreas do conhecimento distintas. 
A família Curie ganhou um total de cinco prêmios Nobel. Marie Curie 
foi a primeira mulher a ser admitida como professora na Universidade 
de Paris. Em 1995, a cientista se tornou a primeira mulher a ser 
enterrada por méritos próprios no Panteão de Paris.\n''')
