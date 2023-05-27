import trabalho
from time import sleep
while True:
    print('VAMOS ORDERNAR A SUA LISTA')
    print('ESCOLHA A OPÇÃO E DIGITE SUA LISTA')
    print('')
    print('1 - Algoritmo de Inserção')
    print('2 - Algoritmo de Seleção')
    print('3 - Algoritmo de Shellsort')
    print('4 - Algoritmo de Quicksort')
    print('0 - Sair')

    opcao = int(input('Escreva o número para ordenar sua lista: '))

    if opcao == 1:
        trabalho.insercao(),sleep(2)
    elif opcao == 2:
        trabalho.selecao(),sleep(2)
    elif opcao == 3:
        trabalho.chamar_shel(),sleep(2)
    elif opcao == 4:
        trabalho.chamar_quick(),sleep(2)
    elif opcao == 0:
        break
    else:
        print('Opção inválida! Tente novamente.')