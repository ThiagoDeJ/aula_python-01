#CRIAÇÃO DO ESTOQUE
estoque = {
    "Camisa":50,
    "Calça":15,
    "Boné":25,
    "Tenis naique":35,
}
#mostrar estoque atual
print("Estoque atual: ")
for produto, quantidade in estoque.items():
    print(f"{produto} : {quantidade}")
#pedindo dados para o usuario do sistema
nome_produto = input("\nInforme o nome do produto vendido: ")
quantidade_vendida = int(input("Informe a quantidade vendida: "))
#atualizar o estoque
if nome_produto in estoque:
    if quantidade_vendida <= estoque[nome_produto] :
        estoque[nome_produto] = estoque[nome_produto] - quantidade_vendida
        print("Venda realizada com sucesso")
else:
    print("Produto não encontrado")
#mostrar estoque atualizado
for produto, quantidade, in estoque.items():
    print(f"{produto} | {quantidade}")
