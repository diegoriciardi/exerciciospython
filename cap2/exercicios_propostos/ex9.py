"""
10. Um vendedor ambulante vendeu os produtos indicados na tabela a seguir. 
Informe quanto ele faturou com cada produto e quanto ele faturou no total.
Produto				Quantidade vendida	Valor unitário
Boneco Malandrinho		17					18,50
Spinner Pequeno			36					12,00
Cubo Mágico				7					5,90

Todos os dados devem ser lidos do teclado, sendo que o nome do produto é string, 
a quantidade vendida é um número inteiro e o valor unitário é um número real.
"""

nome_produto_1 = input("digite por favor o nome do produto 1: ")
valor_unitario_produto_1 = float(input("digite por favor o valor unitario do produto {}: ".format(nome_produto_1)))
quantidade_produto_1 = int(input("digite por favor a quantidade vendida do produto {}: ".format(nome_produto_1)))

nome_produto_2 = input("digite por favor o nome do produto 2: ")
valor_unitario_produto_2 = float(input("digite por favor o valor unitario do produto {}: ".format(nome_produto_2)))
quantidade_produto_2 = int(input("digite por favor a quantidade vendida do produto {}: ".format(nome_produto_2)))

nome_produto_3 = input("digite por favor o nome do produto 3: ")
valor_unitario_produto_3 = float(input("digite por favor o valor unitario do produto {}: ".format(nome_produto_3)))
quantidade_produto_3 = int(input("digite por favor a quantidade vendida do produto {}: ".format(nome_produto_3)))

faturamento_produto_1 = valor_unitario_produto_1 * quantidade_produto_1
faturamento_produto_2 = valor_unitario_produto_2 * quantidade_produto_2
faturamento_produto_3 = valor_unitario_produto_2 * quantidade_produto_3
faturamento_total = faturamento_produto_1 + faturamento_produto_2 + faturamento_produto_3

print("Faturamento {} = {:.2f}".format(nome_produto_1, faturamento_produto_1))
print("Faturamento {} = {:.2f}".format(nome_produto_2, faturamento_produto_2))
print("Faturamento {} = {:.2f}".format(nome_produto_3, faturamento_produto_3))
print("Faturamento total = {:.2f}".format(faturamento_total))