# Resolução algoritmo 1

input = 'teste'

# for no input

count = 0
for str in input:

    # se a string for vogal, aumente o contador em 1
    if str in ['a','e','i','o','u']:
        count += 1

# print contagem

print(count)
