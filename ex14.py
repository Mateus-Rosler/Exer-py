numero1 = float(input("Diga o primero número: "))
numero2 = float(input("Diga o segundo número: "))
numero3 = float(input("Diga o terceiro número: "))

if numero1 > numero2 and numero1 > numero3:
    print("O maior número é o primeiro")
elif numero2 > numero1 and numero2 > numero3:
    print("O maior número é o segundo")
elif numero3 > numero1 and numero3 > numero2:
    print("O maior número é o terceiro")
else:
    print("São iguais")