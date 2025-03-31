valorProduto = float(input("Digite o valor do produto: "))

if valorProduto < 20:
    print("O valor do produto é de: ", (valorProduto * 0.45) + valorProduto)
else:
    print("O valor do produto é de: ", (valorProduto * 0.30) + valorProduto)