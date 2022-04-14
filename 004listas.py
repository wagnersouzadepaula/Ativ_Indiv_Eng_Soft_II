# Listas são ótimas para armazenar uma coleção de objetos afins. Se tiver informações parecidas, a lista é um ótimo lugar para armazená-las.

# Lista é parecida com arrays em outras linguagens, entretanto, diferente das outras linguagens, o tamanho da lista em python é dinâmico.

# Nas listas, os objetos ficam entre colchetes [], e são separados por vírgulas.

# Isso é uma lista vazia LISTA = []

# O modo mais rápido para verificar se um objeto está armazenado numa lista é usando o operador IN.

# Para adicionar um objeto a uma lista, utilise APPEND, EXTEND ou INSERT.

# Para diminuir uma lista retirando um objeto dela utilize REMOVE ou POP.


vogais = ['a', 'e', 'i', 'o', 'u']
palavra = input("Informe uma palavra ou frase: ").lower()
encontrada = []
for letra in palavra:
    if letra in vogais:
        if letra not in encontrada:
            encontrada.append(letra)
for vogal in encontrada:
    print(vogal)

