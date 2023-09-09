print("Calculadora de juros simples")
print("=============================")

# Varíaveis

principal = float(input("Qual o valor principal?: "))
juros = float(input("Qual a taxa de juros anual?: "))
tempo = float(input("Qual o periodo de tempo em anos?: "))
montante = principal + (principal*juros*tempo)

# Comando

print(f"O valor no total será de: {montante}")