escolha = input("Quantos títulos o piloto de fórmula 1 Lews Hamilton tem?\nDigite 1 para 5 títulos\nDigite 2 para 8 títulos\nDigite 3 para 7 títulos\nResposta: ")
#entrada de dados

if escolha == "3":
    print("\nResposta correta! Lewis Hamilton tem 7 títulos na Fórmula 1.")

elif escolha != "1" and escolha != "2":
    print("\nOpção inválida! Por favor, escolha 1, 2 ou 3.")
else:
    print("\nResposta incorreta! Lewis Hamilton tem 7 títulos na Fórmula 1.")
#estrutura condicional