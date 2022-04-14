# Há uma coleção de estruturas de dados padrão disponível quando você está escrevendo programas em python. A lista é uma delas e é muito parecida com um array.

# O tipo de uma variável não precisa ser declarado. Quando você atribui um valor a uma variável no python, ele assume dinamicamente o tipo do dado ao qual se refere.

# As decisões com a instrução IF/ELIF/ELSE. As palavras-chave IF, ELIF e ELSE precedem os blocos de código, que sao conhecidos no munto pythom como suítes.

# As suítes e código estao sempre recuados. A tabulação é o mecanismo de agrupamento de código em python.

# A função SLEEP pode ser usada para pausar o programa por um número específico de segundos.

# Para importar uma função específica de um módulo, informe o módulo e a função que deseja importar, por exemplo FROM TIME IMPORT SLEEP.

# Para importar um módulo inteiro informe apenas o módulo a ser importado: IMPORT TIME

# O módulo RANDOM tem uma função útil chamada RANDINT que gera um número inteiro aleatório dentro de um intervalo específico.

import time
import random
from datetime import datetime

impares = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]


for x in range(5):
    minutoAtual = datetime.today().minute
    #A variável "minutoAtual" é criada de forma dinâmica, não é necessário declarar a variável no início do código atribuindo-lhe um tipo.

    if minutoAtual in impares: #o operador "in" verifica se algo está dentro de uma coisa, retornando true ou false.
        print("O minuto atual parece ser ÍMPAR")
    else:
        print("O minuto atual NÃO É ÍMPAR")
    esperar = random.randint(1,10)
    time.sleep(esperar)
