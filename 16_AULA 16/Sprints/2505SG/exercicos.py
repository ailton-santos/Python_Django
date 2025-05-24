#Exercicio 4

a1 = float(input('Digite o primeiro numero: '))
a2 = float(input('Digite o segundo numero: '))

result_soma = a1 + a2
result_mult = a1 * a2
result_sub  = a1 - a2
result_div = a1 + a2

print(f'O resultado da soma da primeira operaçao é igual a {result_soma}')
print(f'O resultado da multiplacacao da primeira operaçao é igual a {result_mult}')
print(f'O resultado da subtracao da primeira operaçao é igual a {result_sub}')
print(f'O resultado da divisao da primeira operaçao é igual a {result_div}')



#exercico 1
#resultado do jogo de futebel
placar_timevita = int(10)
placar_timevivo = int(8)
print(f"O placar do time vita é igual a {placar_timevita}")
print(f"O placar do time vivo é igual a {placar_timevivo}")
print(placar_timevivo)

if placar_timevivo >=8:
    print(f"Parabéns o time vivo ganhou")
elif placar_timevita <=10:
    print(f"Parabéns o time vita ganhou!")


#exercicos 03

#total da compra
# Lista de frutas disponíveis e seus preços (por kg)
frutas = {
    "Maçã": 5.00,
    "Banana": 3.00,
    "Laranja": 4.50,
    "Morango": 8.00,
    "Manga": 6.50
}

# Exibe as frutas disponieis 
print("Frutas disponíveis:")
for fruta, preco in frutas.items():
    print(f"{fruta}: R$ {preco:.2f}/kg")

# Usuário escolhe a fruta
escolha = input("\nQual fruta você deseja comprar? ").title()
if escolha not in frutas:
    print("Fruta não disponível.")
else:
    # Pergunta a quantidade
    quantidade = float(input(f"Quantos kg de {escolha} você quer? "))
    valor_total = frutas[escolha] * quantidade

    # Parcelamento
    parcelas = int(input("Em quantas vezes deseja parcelar a compra? "))
    valor_parcela = valor_total / parcelas

    # Resultado
    print(f"\nVocê comprou {quantidade:.2f} kg de {escolha} por R$ {valor_total:.2f}.")
    print(f"Será parcelado em {quantidade:.2f}x de R$ {parcelas:.2f}.")















