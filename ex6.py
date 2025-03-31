tempFahrenheit = float(input("Digite a temperatura em fahrenheit que você quer transformar: "))

tempCelsius = (tempFahrenheit * 9/5) + 32
tempKelvin = (tempFahrenheit - 32) * 5/9 + 273,15

print("A temperatura em celsius é de: ", tempCelsius)
print("Aemperatura em kelvin é de: ", tempKelvin)