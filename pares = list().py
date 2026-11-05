pares = list()
impares = list()
for i in range(10):
    numero = int(input("digite um número inteiro: "))
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
print("numeros pares:", pares)
print("numeros impares:", impares)