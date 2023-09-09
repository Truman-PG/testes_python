print("Calculadora de conversão em temperatura")
print("=========================================")

celsius = float(input("Qual a temperatura em graus Celsius:"))

# Variáveis

fahrenheit = celsius*1.8 + 32
kelvin = celsius+273.15

# Comando

print(f"Em Fahrenheit a temperatura será de: {fahrenheit}")
print(f"Em Kelvin será de: {kelvin}")