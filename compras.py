print('\nVamos às compras!')
print('Insira o nome de três produtos de \nmercado e seus respectivos preços')
item1 = input('\n1º Produto: ')
item1_preco = float(input('     Preço: '))

item2 = input('\n2º Produto: ')
item2_preco = float(input('     Preço: '))

item3 = input('\n3º Produto: ')
item3_preco = float(input('     Preço: '))

if item1_preco < item2_preco and item2_preco < item3_preco:
    print(f'{item1} é o produto mais barato.')

elif item2_preco < item1_preco and item1_preco < item3_preco:
    print(f'{item2} é o produto mais barato.')

elif item3_preco < item1_preco and item1_preco < item2_preco:
    print(f'\n{item3} é o produto mais barato.\n')