# Classe Produto
class Produto:
    # Construtor da classe Produto, inicializa com nome, quantidade, preço e unidade
    def __init__(self, nome, quantidade, preco, unidade):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco
        self.unidade = unidade

    # Método para calcular o preço por 100 unidades
    def calcular_preco_por_100_unidades(self):
        return (self.preco / self.quantidade) * 100

# Classe ComparadorDeProdutos
class ComparadorDeProdutos:
    # Construtor da classe ComparadorDeProdutos, inicializa com uma lista vazia de produtos
    def __init__(self):
        self.produtos = []

    # Método para adicionar um produto à lista de produtos
    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    # Método para comparar os produtos
    def comparar(self):
        resultados = []
        for produto in self.produtos:
            preco_por_100 = produto.calcular_preco_por_100_unidades()
            resultados.append((produto.nome, preco_por_100, produto.unidade))

        # Ordena os resultados pelo preço por 100 unidades, em ordem crescente
        resultados.sort(key=lambda x: x[1])

        return resultados

# Função para obter informações dos produtos do usuário
def obter_informacoes_produto():
    nome = input("Digite o nome da marca: ")

    # Loop para obter e validar a quantidade do produto
    while True:
        try:
            quantidade = float(input("Digite a quantidade do produto: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número para a quantidade.")
    
    # Loop para obter e validar a unidade do produto (deve ser 'ml' ou 'g')
    unidade = input("Digite a unidade do produto (ml ou g): ").strip().lower()
    while unidade not in ['ml', 'g']:
        print("Unidade inválida. Por favor, digite 'ml' ou 'g'.")
        unidade = input("Digite a unidade do produto (ml ou g): ").strip().lower()

    # Loop para obter e validar o preço do produto
    while True:
        try:
            preco = float(input("Digite o preço do produto em R$: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número para o preço.")
    
    # Retorna uma instância da classe Produto com as informações fornecidas
    return Produto(nome, quantidade, preco, unidade)

# Exemplo de uso
comparador = ComparadorDeProdutos()

# Obter informações para três produtos
for i in range(3):
    print(f"\nProduto {i + 1}:")
    produto = obter_informacoes_produto()
    comparador.adicionar_produto(produto)

# Comparar os produtos e mostrar os resultados
resultados = comparador.comparar()

# Exibir os resultados da comparação
print("\nComparação de Preços por 100 unidades:\n")
for nome, preco, unidade in resultados:
    print(f"{nome}: R$ {preco:.2f} por 100 {unidade}")

