livro = "Guia do mochileiro das galaxias"
livroEmLista = list(livro)
print(livroEmLista)
print(livroEmLista[0:3]) #imprime da posição 0, até a posição 3 (não incluindo-a), com um step de 1 (uma vez que nao foi informado nenhum passo)
print(livroEmLista[3:]) #imprime da posição 3 até o fim (uma vez que nao foi informado o stop), com step 1 (uma vez que nao foi informado o passo)
print(livroEmLista[:10]) #imprime da posição inicial até a posição 10 (nao incluindo-a),com step 1 (uma vez que nao foi informado o passo)
print(livroEmLista[::2]) #imprime da posição inicial até a final, com step 2
print(livroEmLista[::-1]) #imprime da posicao final até a posição inicial, uma vez que o step informado é -1
print(livroEmLista[-8:]) #imprime da posição -8 até o final
