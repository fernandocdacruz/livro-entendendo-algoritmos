def somar(lista):
    soma = 0
    for i in range(len(lista)):
        soma += lista[i]
    return soma

lista = [3,5,7,9,10]

def somar2(lista):
    if lista == []:
        return 0
    return lista[0] + somar2(lista[1:])

def contar_elementos(lista):
    if lista == []: 
        return 0
    else:
        return 1 + contar_elementos(lista[1:])



print(somar(lista))
print(somar2(lista))
print(contar_elementos(lista))