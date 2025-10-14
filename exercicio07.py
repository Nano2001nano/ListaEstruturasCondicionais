dia = int(input("\nDigite o dia do mês: "))
mes = int(input("Digite o mês (número): "))
ano = int(input("Digite o ano: "))
#entrada de dados

if ano < 0:
    print("\nData inválida.")

elif (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12) and (dia > 0 and dia < 32):
    print(f"\n{dia}/{mes}/{ano} é uma data válida.")

elif (mes == 4 or mes == 6 or mes == 9 or mes == 11) and (dia > 0 and dia < 31):
    print(f"\n{dia}/{mes}/{ano} é uma data válida.")

elif mes == 2 and (dia > 0 and dia < 29):
    print(f"\n{dia}/{mes}/{ano} é uma data válida.")

else:
    print("\nData inválida.")
#processamento e saída de dados