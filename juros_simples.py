print("Calculadora de juros simples")
print("=============================")

# Varíaveis

principal = float(input("Qual o valor principal?: "))
juros = float(input("Qual a taxa de juros em porcentagem?: "))
tempo = float(input("Qual o periodo de tempo em anos?: "))
montante = principal + (principal*juros/100*tempo)

# Comando

print(f"O valor no total será de: {montante}")