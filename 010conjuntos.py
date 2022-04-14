# 01- Conjuntos no python não permitem dados duplicados.
# 02- Como nos dicionários, os conjuntos ficam entre chaves, mas estes não possuem chaves/valor. Cada objeto único no conjunto é separado por vírgulas
# 03- Como nos dicionários, os conjuntos são desordenados (não mantem a ordem de inserção), mas podem ser ordenados pela função SORTED
# 04- É possível passar qualquer sequência para a função SET criar um conjunto de elementos a partir dos objetos na sequência.
# 05- Os conjuntos tem funcionalidades como união (UNION), diferença (DIFFERENCE), interseção (INTERSECTION)

vogais = set('aeiou')
palavra = input("Informe uma palavra ou frase: ").lower()
intersectionVogais = vogais.intersection(set(palavra))
print(sorted(intersectionVogais))
