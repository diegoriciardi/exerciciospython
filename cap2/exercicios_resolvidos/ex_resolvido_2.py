"""
. Reescreva o programa anterior alterando-o de modo que as vendas 
do mês sejam lidas do teclado
"""

fixo = 500.00
vendas = float(input("Digite por favor o valor das vendas: "))
porcentagem_comissao = 0.06
comissao = vendas * porcentagem_comissao

resultado = fixo + comissao

print("Faturamento do representante: {:.2f}".format(resultado))
