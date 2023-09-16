# 1 – A vista – 10% de desconto, caso o valor da venda seja maior que 500 15%, caso seja maior que 1000, 20% de desconto;
# 2 – A prazo – A venda pode ser parcelada em até 18x. Caso seja parcelado em mais do que 10x possui juros:
# Apenas compras com mais de 800 reais podem ser parceladas acima de 5x;
# Juros:
# 1 – 11 vezes: 5% de juros ao mês.
# 2 – 12 vezes: 6.5% de juros ao mês.
# 3 – 13 vezes: 7% de juros ao mês.
# 4 – 14 vezes: 9% de juros ao mês.
# 5 – 15 vezes: 9.5% de juros ao mês.
# 6 – 16 vezes: 10% de juros ao mês.
# 7 – 17 vezes: 11.3% de juros ao mês.
# 8 – 18 vezes: 12% de juros ao mês. 

# Primeiro passo: Pagar a vista ou a prazo:
# Segundo passo: Perguntar o valor:
# Terceiro passo: Valor a vista > 500, 15% desconto.
# Quarto passo: Valor a vista > 1000, 20% desconto.

preferencia = input("Vai pagar a vista ou a prazo?")
valor = float(input("Isnira o valor:  "))
if preferencia == "vista" and valor > 500 and valor <= 1000:
    resultado = valor - (valor*15/100)
    print(f"Com desconto de 15% o valor será de {resultado}")
elif preferencia == "vista" and valor > 1000:
    resultado = valor - (valor*20/100)
    print(f"Com desconto de 20% o valor será de: {resultado}")
elif preferencia == "prazo":
    print("Você pode parcelar até 18x")
    parcela = int(input("Em quantas vezes você irá parcelar?: "))
