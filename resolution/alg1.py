# Resolução algoritmo 1

input = 'teste'

# for no input

count_v = 0
count_c = 0

for str in input:

    # se a string for vogal, aumente o contador em 1
    if str in ['a','e','i','o','u']:
        count_v += 1
    
    elif str not in ['a','e','i','o','u']:
        count_c += 1

# print contagem

print('o número de vogais é:', count_v)
print('o número de consoantes é:', count_c)
