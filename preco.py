# Definindo a função 'Compra'
def Compra():
    # Solicitando ao usuário o preço por quilograma (kg) do produto
    preco = float(input("Valor do Kg: "))

    # Solicitando ao usuário a quantidade do produto em gramas (g)
    qnt = float(input("Peso em gramas: "))

    # Calculando o valor a pagar, convertendo a quantidade de gramas para quilogramas
    valorPagar = (preco * qnt) / 1000

    # Retornando o valor a ser pago
    return valorPagar

# Chamando a função 'Compra' e armazenando o valor retornado na variável 'valor_total'
valor_total = Compra()

# Imprimindo o valor a ser pago na tela, formatado com duas casas decimais
print("Valor a pagar: R${:.2f}".format(valor_total))

