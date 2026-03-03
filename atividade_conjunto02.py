pessoa1 = {"Café", "Açúcar", "Farinha", "Refrigerante", "Trigo"}
pessoa2 = {"Maçã", "Melão", "Melancia", "Banana", "Açúcar", "Farinha"}
pessoa3 = {"Refrigerante", "Farinha", "Vinho", "Copos", "Limão", "Açúcar"}
pessoa4 = {"Vassoura", "Açúcar", "Arroz", "Feijão", "Farinha", "Espanador"}

cliente1 = set(pessoa1)
cliente2 = set(pessoa2)
cliente3 = set(pessoa3)
cliente4 = set(pessoa4)

print(f"A lista de compras do primeiro cliente é: {pessoa1}")
print(f"A lista de compras do segundo cliente é: {pessoa2}")
print(f"A lista de compras do terceiro cliente é: {pessoa3}")
print(f"A lista de compras do quarto cliente é: {pessoa4}")

rep_itens = cliente1.intersection(cliente2|cliente3|cliente4)
print(f"Os itens repitidos nas quatro listas são: {rep_itens}")

todos_itens = cliente1.union(cliente2|cliente3|cliente4)
print(f"Os itens dos clientes são: {todos_itens} e o total de itens é:")
print(len(todos_itens))
