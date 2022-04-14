# O loop FOR pode ser usado para iterar um número fixo de vezes. Se você souber de antemão quantas vezes precisará fazer um loop, use FOR.

# Quando não souber quantas vezes o loop deverá ser realizado, use o WHILE.

# O loop FOR pode iterar qualquer sequência como lista ou strings. Bem como executar um número fixo de vezes (graças à funcão RANGE).

# a função range pode ter mais d eum argumento quando for chamada. Esses argumentos permitem controlar os valores (START, STOP, STEP).

# O STEP quando informado como um número negativo, mudará a direção da contagem.

palavra = "bottles"
for num_cerveja in range (99, 0, -1):
    print(num_cerveja, palavra, "of beer on the wall.")
    print(num_cerveja, palavra, "of beer.")
    print("Take one down.")
    print("Pass it around.")
    if num_cerveja == 1:
        print("No more bottles of beer on the wall.")
    else:
        novo_num_cerveja = num_cerveja - 1
        if novo_num_cerveja == 1:
            palavra = "bottle"
        print(novo_num_cerveja, palavra, "of beer on the wall.")
    print()
