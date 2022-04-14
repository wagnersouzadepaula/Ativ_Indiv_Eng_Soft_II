frase = "don't panic!"
flista = list(frase) #criar a lista com as letras de frase
print(frase)
print(flista)
novaFrase = ''.join(flista[1:3]) #seleciona a primeira parte 'on'
novaFrase = novaFrase + ''.join([flista[5],flista[4],flista[7],flista[6]]) #seleciona a segunda parte reorganizando os caracteres
print(flista)
print(novaFrase)
#observação importante: O uso do 'fatiamento' (uso dos colchetes[6]) não altera o conteúdo da varíavel, ao contrário do append, insert, extends, pop, remove que alteram o conteúdo da varíavel.
