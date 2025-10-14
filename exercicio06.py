num1 = float(input("\nDigite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação desejada:\nM para multiplicação\nD para divisão\n\nResposta: ")
#entrada de dados

if operacao == "M" or operacao == "m":
    resultado = num1 * num2
    print(f"\nO resultado da multiplicação é: {resultado}")
elif operacao == "D" or operacao == "d":
    if num2 != 0:
        resultado = num1 / num2
        print(f"\nO resultado da divisão é: {resultado}")
    else:
        print("\nERRO: O número 0 não pode ser usado na divisão.")
#processamento e saída de dados