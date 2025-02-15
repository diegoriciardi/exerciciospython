"""
8. Escreva um programa que leia o nome de um lutador e seu peso. Em seguida, 
informe a categoria a que pertence o lutador, conforme o Quadro 3.9 (note que o quadro 
foi criado para efeito deste exercício e não condiz com qualquer categoria de luta). 
A saída do programa deve exibir na tela uma frase com o padrão descrito a seguir: 
Nome fornecido: Pepe Jordão Peso fornecido: 73.4 Frase a ser exibida: O lutador Pepe 
Jordão pesa 73,4 kg e se enquadra na categoria Ligeiro

Peso                                            Categoria
Menor que 65 kg                                     Pena
Maior ou igual a 65 kg e menor que 72 kg            Leve
Maior ou igual a 72 kg e menor que 79 kg            Ligeiro
Maior ou igual a 79 kg e menor que 86 kg            Meio-médio
Maior ou igual a 86 kg e menor que 93 kg            Médio
Maior ou igual a 93 kg e menor que 100 kg           Meio-pesado
Maior ou igual a 100 kg                             Pesado
"""

try:
    nome = input("digite por favor o nome: ")
    peso = float(input("digite por favor o peso: "))

    if peso < 65:
        categoria = "Pena"
    elif peso >= 65 and peso <= 71:
        categoria = "Leve"
    elif peso >= 72 and peso <= 78:
        categoria = "Ligeiro"
    elif peso >= 79 and peso <= 85:
        categoria = "Meio-médio"
    elif peso >= 86 and peso <= 92:
        categoria = "Médio"
    elif peso >= 93 and peso <= 99:
        categoria = "Meio-pesado"
    else:
        categoria = "Pesado"

    print("Nome fornecido: {}".format(nome))
    print("Peso fornecido: {}".format(peso))
    print("O lutador {} pesa {} kg e se enquadra na categoria {}".format(
        nome, 
        peso,
        categoria
    ))

except Exception as e:
    print("Ocorreu um erro {}".format(e))
