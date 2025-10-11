num1 = int(input("\nDigite o primeiro número: "))
num2 = int(input("\nDigite o segundo número: "))
num3 = int(input("\nDigite o terceiro número: "))
#entrada

if num1 >= num2 and num1 >= num3 and num2 >= num3:
    print(f"\n A ordem crescente é: {num3}, {num2}, {num1}\n")
elif num1 >= num2 and num1 >= num3 and num3 >= num2:
    print(f"\n A ordem crescente é: {num2}, {num3}, {num1}\n")
elif num2 >= num1 and num2 >= num3 and num1 >= num3:
    print(f"\n A ordem crescente é: {num3}, {num1}, {num2}\n")
elif num2 >= num1 and num2 >= num3 and num3 >= num1:
    print(f"\n A ordem crescente é: {num1}, {num3}, {num2}\n")
elif num3 >= num1 and num3 >= num2 and num1 >= num2:
    print(f"\n A ordem crescente é: {num2}, {num1}, {num3}\n")
else:
    print(f"\n A ordem crescente é: {num1}, {num2}, {num3}\n")
#processamento e saída