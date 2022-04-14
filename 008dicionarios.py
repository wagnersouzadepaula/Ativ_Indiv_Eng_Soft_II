vogais = ['a', 'e', 'i', 'o', 'u']
palavra = input("Informe uma palagra ou frase: ").lower()
encontrada = {}
encontrada['a']=0
encontrada['e']=0
encontrada['i']=0
encontrada['o']=0
encontrada['u']=0

for letra in palavra:
    if letra in vogais:
        encontrada[letra] += 1
for chave,valor in sorted(encontrada.items()):
    print(chave, 'foi encontrada', valor, 'vez(es).')
