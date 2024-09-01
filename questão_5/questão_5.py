texto = input('Digite um texto: ')

textoInvertido = ""

for i in range(1, len(texto) + 1):
    textoInvertido = textoInvertido + texto[-i]
    
print(textoInvertido)
