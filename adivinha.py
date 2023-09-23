from random import randint

numero = randint(0,100)
valor = 0
tentativas = 0

while valor != numero:
    valor = int(input("Insira um numero de 0 a 100: "))
    tentativas += 1
    if valor < numero:
        print(f"O número é maior que {valor}")
    elif valor > numero:
        print(f"O número é menor que {valor}")
    else:
        print(f"Você acertou o número é {numero}")
print(f"Tentativas: {tentativas}")
    