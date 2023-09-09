numero1 = float(input("Insira um número:"))
numero2 = float(input("Insira um número:"))
operacao = input("Insira a operação para calcular os números (+ - * /):")

if operacao == "+" :
    resultado = numero1+numero2
    print(f"O resultado é de:{resultado}")

elif operacao == "-" :
    resultado = numero1-numero2
    print(f"O resultado é de:{resultado}")

elif operacao == "*" :
    resultado = numero1*numero2
    print(f"O resultado é de:{resultado}")

elif operacao == "/" :
    resultado = numero1/numero2
    print(f"O resultado é de:{resultado}")

else:
    print("Não é possivel ser executado")