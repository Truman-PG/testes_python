#Peça ao usuário para inserir seu salário e o tempo de serviço.
#Se o tempo de serviço for superior a 5 anos, conceda um bônus de 5% ao salário.

print("==========Cálculos de bônus salarial==========")

salario = float(input("Insira seu salário: "))
tempo = float(input("Insira seu tempo de serviço em anos: "))

if tempo > 5:
    resultado = (salario*5/100) + salario
    print(f"Com bônus de 5% será de: {resultado}")
else:
    print("Você nao tem bônus salarial.")