def cozinhar(ingrediente, tempo):
    return print(f'\n- {ingrediente} foi cozido por {tempo} minutos.')

def temperar(temperos, ingrediente):
    return print(f'\n- {temperos} foi adicionado à {ingrediente}.')

def camada(ingrediente):
    return print(f'\n- Camada de {ingrediente} adicionada.')

def aquecer_forno(temperatura, tempo):
    return print(f'\n- Forno aquecido a {temperatura}ºC durante {tempo} minutos')

def botar_forno(alimento, tempo):
    return print(f'\n- {alimento} foi colocada no forno por {tempo} minutos')

cozinhar('massa da lasanha', 5)
cozinhar('carne moída', 20)

temperar('molho de tomate', 'carne moída') 
temperar('sal', 'carne moída') 
temperar('pimenta do reino', 'carne moída') 
temperar('orégano', 'carne moída') 

camada('molho')
camada('massa da lasanha')
camada('presunto')
camada('queijo')

camada('molho')
camada('massa da lasanha')
camada('presunto')
camada('queijo')

aquecer_forno(temperatura= 180, tempo=5)

botar_forno(alimento='lasanha', tempo= 25)