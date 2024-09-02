def pertenceFibonacci(numero): #verifica se um numero faz parte da sequencia de numeros fibonacci
    if numero < 0:
        return False

    a, b = 0, 1

    while a <= numero: #o loop continua até que A seja igual ao numero  pesquisado caso ele esteja na sequencia fibonacci ou maior que o numero pesquisado caso ele não esteja.
        if a == numero: #caso seja o numero, o loop será cancelado.
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
    print('Digite um numero inteiro!') #caso o numero digitado no input for diferente de inteiro haverá uma mensagem de erro.

