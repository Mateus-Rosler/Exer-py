salario = float(input("Qual seu salário: "))
aumento = float(input("Qual o percentual de aumento aumento: "))

salarioAjustado = salario * (aumento/100) + salario

print("O valor do aumento é: ", salario * (aumento/100))
print("O novo salário é de: ", salarioAjustado)