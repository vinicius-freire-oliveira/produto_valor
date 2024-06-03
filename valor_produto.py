# Função para obter o peso do produto do usuário, com manipulação de exceção para garantir entrada válida
def obter_peso_produto():
    while True:
        try:
            peso = float(input("Informe o peso em Kg do produto: "))
            if peso <= 0:  # Verifica se o peso é válido
                print("O peso do produto deve ser maior que zero.")
            else:
                return peso  # Retorna o peso se for válido
        except ValueError:  # Captura erros se o usuário fornecer entrada não numérica
            print("Por favor, insira um valor numérico válido.")

# Função para obter o preço do produto do usuário, com manipulação de exceção para garantir entrada válida
def obter_preco_produto():
    while True:
        try:
            preco = float(input("Valor do produto: "))
            if preco < 0:  # Verifica se o preço é válido
                print("O valor do produto não pode ser negativo.")
            else:
                return preco  # Retorna o preço se for válido
        except ValueError:  # Captura erros se o usuário fornecer entrada não numérica
            print("Por favor, insira um valor numérico válido.")

# Função para calcular o valor por Kg do produto
def calcular_valor_por_kg(peso, preco):
    return preco / peso if peso != 0 else None  # Retorna None se o peso for zero para evitar divisão por zero

# Função principal do programa
def main():
    # Chama as funções para obter o peso do produto e o preço do produto
    peso_produto = obter_peso_produto()
    preco_produto = obter_preco_produto()

    # Calcula o valor por Kg do produto
    valor_por_kg = calcular_valor_por_kg(peso_produto, preco_produto)

    # Verifica se o valor por Kg é válido e imprime o resultado formatado
    if valor_por_kg is not None:
        print(f"Valor do Kg vale: R${valor_por_kg:.2f}")
    else:
        print("O peso do produto não pode ser zero.")

# Executa a função main quando o script é executado diretamente
if __name__ == "__main__":
    main()
