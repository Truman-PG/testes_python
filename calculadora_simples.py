numero1 = float(input("Insira um número:"))
numero2 = float(input("Insira um número:"))
operacao = input("Insira a operação para calcular os números (+ - * /):")
resultado = ''

if operacao == '+':
    resultado = numero1 + numero2
elif operacao == '-':
    resultado = numero1 - numero2
elif operacao == '*':
    resultado = numero1 * numero2
elif operacao == '/':
    if numero2 == 0:
        print("Não é possível dividir por zero")
    else:
        resultado = numero1 / numero2
else:
    print("Operação não reconhecida.")
if resultado != '':
    print(f"O resultado é{resultado}")