# Resolução algoritmo 1

def count_vog_con(input):

    # Definições

    count_v = 0
    count_c = 0
    vogais = ['a','e','i','o','u']

    # Tratamento

    input = input.lower()

    for str in input:

        # Verifica se a string é uma letra
        if str.isalpha():
            # se a string for vogal, aumente o contador de vogais em 1
            if str in vogais:
                count_v += 1
            # se a string não for vogal, aumente contador de consoantes em 1
            elif str not in vogais:
                count_c += 1

    output_1 = count_v
    output_2 = count_c
    
    return output_1, output_2
