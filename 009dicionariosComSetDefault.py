vogais = ['a', 'e', 'i', 'o', 'u']
palavra = input("Informe uma palavra ou frase: ").lower()
encontrada = {}

for letra in palavra:
    if letra in vogais:
        encontrada.setdefault(letra,0)
        encontrada[letra] += 1
for chave,valor in sorted(encontrada.items()):
    print(chave, 'foi encontrada', valor, 'vez(es).')
