idade = int(input("\nDigite sua idade: "))
#entrada

if idade < 16:
    print("\nVocê não pode votar.")

elif idade >= 16 and idade < 18 or idade >= 65:
    print("\nO voto é opcional para você.")

else:
    print("\nO voto é obrigatório para você.")
    #processamento e saída