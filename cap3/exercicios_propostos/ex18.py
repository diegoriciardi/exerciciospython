"""
18. Elabore um programa que efetue a leitura de valores positivos inteiros até que 
zero ou um valor negativo seja informado. Ao final, devem ser apresentados o maior e 
menor valores informados pelo usuário, a quantidade de valores, a soma e a média de todos.
"""

try:
    
    mensagem_prompt = "digite por favor um valor inteiro positivo: "
    mensagem_maior_menor = "maior {} e menor {}"

    x = int(input(mensagem_prompt))
    if x != 0:
        quantidade_valores = 1
        soma = 0
        maior = menor = x
        while True:
            x = int(input(mensagem_prompt))
            if x != 0:
                if x >= maior:
                    maior = x
                elif x <= menor:
                    menor = x
                soma += x
                quantidade_valores += 1
            else:
                break
        
        print("\n\n")
        print("Quantidade valores informados: {}".format(quantidade_valores))
        print("Maior valor: {}".format(maior))
        print("Menor valor: {}".format(menor))
        print("Media dos valores informados: {:.2f}".format(
            soma / quantidade_valores
        ))

            

except Exception as e:
    print("Ocorreu um erro: {}".format(e))