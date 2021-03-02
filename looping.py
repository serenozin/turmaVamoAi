# print("\nContando de um 1 à 5:")
# for i in range(1, 6):
#     print(i)

# print("\nPrintando somente as sílabas da palavra inputada")
# palavra = input("Insira uma palavra:\n- ").upper()
# for i in palavra:
#     if  i == "A" or i == "E" or i =="I" or i == "O" or i == "U":
#         print(" ")
#     else:
#         print(i)
    
# WHILE com FUNÇÃO
def par_ou_impar(numero):
    numero = float(numero)
    if numero % 2 == 0: 
        print(f"{numero} é um número par.")
    elif numero % 2 == 1:
        print(f"{numero} é um número ímmpar.")
    else: 
        print('Inserção inválida.')
    
resposta = input(
    "\nInsira um número para saber se é par ou ímpar; ou 'sair!' para sair:\n- "
    )

while resposta != "sair!":
    par_ou_impar(resposta)
    resposta = input(
        "\nInsira outro número para saber se é par ou ímpar; ou 'sair!' para sair:\n- "
        )


# WHILE
adivinha = input("\nChute até descobrir meu sabor de sorvete preferido:\n- ").lower()

while adivinha != "feijao":
    adivinha = input("Tente novamente:\n- ").lower()

print("\nVocê acertou!")




    
