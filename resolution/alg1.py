# Resolução algoritmo 1

input = '4aAAa 5CcCcC #$@'

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

# print contagem

print('o número de vogais é:', count_v)
print('o número de consoantes é:', count_c)
