def pertenceFibonacci(numero):
    if numero < 0:
        return False

    a, b = 0, 1

    while a <= numero:
        if a == numero:
            return True
        a, b = b, a + b

    return False

try:
    numero = int(input('Digite um numero: '))

    if pertenceFibonacci(numero):
        print(f"O numero {numero} pertence a fibonacci")
    else:
        print(f"O numero {numero} não pertence a fibonacci")
        
except ValueError:
    print('Digite um numero inteiro!')

