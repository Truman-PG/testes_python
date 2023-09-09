nome = input("Qual o seu nome:")
idade = int(input("Qual é a sua idade:"))
peso = float(input("Qual o seu peso em Kg:"))
altura = float(input("Qual a sua altura em cm:"))
imc = peso/(altura**2)

print(f"Olá {nome}")
print(f"Sua idade é de {idade}", "anos")
print(f"Seu IMC é de {imc}")