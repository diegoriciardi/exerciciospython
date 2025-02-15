"""
9. Escreva um programa que leia o valor hora que um profissional ganha na empresa onde trabalha. 
Leia também as quantidades de horas normais e horas extras trabalhadas em um mês. 
Calcule o valor a ser recebido pelo profissional nesse mês, sabendo que nas horas extras o pagamento é dobrado.
"""

try:
    valor_por_hora = float(input("digite por favor o valor do salario por hora: "))
    qtde_horas_normais = int(input("digite por favor a quantidade de horas trabalhadas (normais): "))
    qtde_horas_extras = int(input("digite por favor a quantidade de horas trabalhadas (extras): "))
    print("\n\n")

    salario = (valor_por_hora * qtde_horas_normais) + ((valor_por_hora * qtde_horas_extras) *2)

    print("Valor por hora: {}".format(valor_por_hora))
    print("Horas trabalhadas (normal): {}".format(qtde_horas_normais))
    print("Horas trabalhadas (extra x2): {}".format(qtde_horas_extras))

    print("Salario: R$ {:.2f}".format(salario))

except Exception as e:
    print("Ocorreu um erro. {}".format(e))