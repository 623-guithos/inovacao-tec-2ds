# Programa para calcular a média de 4 números

# 1. Solicitar os 4 números via input
print("Digite 4 números para calcular a média:")
num1 = input("Número 1: ")
num2 = input("Número 2: ")
num3 = input("Número 3: ")
num4 = input("Número 4: ")

# 2. Converter os valores para float
# A conversão é necessária para realizar operações matemáticas
num1 = float(num1)
num2 = float(num2)
num3 = float(num3)
num4 = float(num4)

# 3. Calcular a média
# Soma todos os números e divide pela quantidade (4)
media = (num1 + num2 + num3 + num4) / 4

# 4. Exibir o resultado com duas casas decimais
# Usamos f-string com :.2f para formatar com 2 casas decimais
print(f"A média dos números é: {media:.2f}")
