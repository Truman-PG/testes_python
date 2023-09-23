lista =int((input("Solicite um número maximo para a lista: ")))
ordem = input("Qual a ordem que deseja imprimir os números (C/D): ")

if ordem == 'C':
    for resultado in range (1 , lista + 1):
        print(resultado)
elif ordem == 'D':
    for resultado in range (lista, 0 , - 1):
        print(resultado)
else:
    print("Ordem inválida.")