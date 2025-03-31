tempKelvin = float(input("Digite a temperatura em fahrenheit que você quer transformar: "))

tempFahrenheit = (tempKelvin - 273,15) * 9/5 + 32
tempCelsius = tempKelvin - 273,15

print("A temperatura em fahrenheit é de: ", tempFahrenheit)
print("Aemperatura em celsius é de: ", tempCelsius)