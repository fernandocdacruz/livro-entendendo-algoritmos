tamanho = int(input("Digite o tamanho da lista: "))

contador = 1
log = 2

while log != tamanho:
    log = log * 2
    contador = contador + 1

print(contador)