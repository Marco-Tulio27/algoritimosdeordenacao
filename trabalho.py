from time import sleep
sizelista=6
def insercao():
    lista = []
    for k in range(sizelista):
        numero = int(input('Digite um número: '))
        lista.append(numero)
        j = len(lista) - 1
        while j > 0 and lista[j] < lista[j - 1]:
            lista[j], lista[j - 1] = lista[j - 1], lista[j]
            j -= 1
    print('lista ordenada por inserção',lista)
#nsercao()

def selecao():
    lista = []
    
    for k in range(sizelista):
        numero = int(input('Digite um número: '))
        lista.append(numero) 

    for i in range(len(lista)):
        menor = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[menor]:
                menor = j
        lista[i], lista[menor] = lista[menor], lista[i]
    
    print('Lista ordenada por seleção:', lista)

#selecao()
def quicksort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivo = lista[0]
        less = [x for x in lista[1:] if x <= pivo]
        greater = [x for x in lista[1:] if x > pivo]
        return quicksort(less) + [pivo] + quicksort(greater)
def chamar_quick():
    lista = []
    for k in range(sizelista):
        numero = int(input('Digite um número: '))
        lista.append(numero)

    lista_ordenada = quicksort(lista)
    print('lista ordenada por quicksort',lista_ordenada)
            
def shell_sort(lista):
    n = len(lista)
    dividir = n // 2

    while dividir > 0:
        for i in range(dividir, n):
            temp = lista[i]
            j = i
            while j >= dividir and lista[j - dividir] > temp:
                lista[j] = lista[j - dividir]
                j -= dividir
            lista[j] = temp
        dividir //= 2

def chamar_shel():
    lista = []
    for i in range(sizelista):
        numero = int(input('Digite um número: '))
        lista.append(numero)
    shell_sort(lista)
    print('lista ordenada por shellsort',lista)


        