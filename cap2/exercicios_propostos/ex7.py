"""
7. Escreva a sequência de comandos para calcular o salário 
bruto de um pro-fissional que ganha por hora, 
sabendo que ele ganha R$ 14,25/h e trabalhou 163 horas 
normais e 20 horas extras (pagam o dobro).
"""

salario_por_hora = 14.25
horas_normais_trabalhadas = 163
horas_extras_trabalhadas = 20

salario_bruto = (salario_por_hora * horas_normais_trabalhadas) + (salario_por_hora * horas_extras_trabalhadas * 2)

print("O salario bruto = {}".format(salario_bruto))




