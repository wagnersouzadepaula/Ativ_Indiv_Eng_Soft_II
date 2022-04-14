# 1- Funções são partes nomeadas do código.
# 2- DEF é usada para nomear uma função. O código da função fica recuado em relação ao DEF.
# 3- RETURN permite que as funções retornem qualquer quantidade de valor (inclusive nenhum valor).

def procura_vogais(frase: str) -> set:
    """Retorna todas as vogais encontradas na palavra passada como parâmetro."""
    vogais = set('aeiou')
    return vogais.intersection(set(frase))


def procura_letras(frase: str, letras: str = 'aeiou') -> set:
    """Retorna todas as 'letras' passadas como parâmetro e encontradas na 'frase'."""
    return set(letras).intersection(set(frase))
