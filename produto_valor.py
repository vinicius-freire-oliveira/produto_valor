def calcular_custo_do_queijo(peso_em_kg, preco_por_kg):
    return peso_em_kg * preco_por_kg

# Preço do queijo por quilograma (em reais)
preco_por_kg_queijo = 32.90

# Peso do queijo que você deseja comprar (em quilogramas)
peso_desejado_kg = 4.25

# Calcula o custo total do queijo
custo_total = calcular_custo_do_queijo(peso_desejado_kg, preco_por_kg_queijo)

# Exibe apresentação
print("\nCálculo custo do produto em relação ao peso")
# Exibe o resultado
print(f"O valor do peso do queijo é: R${preco_por_kg_queijo:.2f}")
print(f"Você comprou {peso_desejado_kg} kg de queijo.")
print(f"Total a pagar: R${custo_total:.2f}")
