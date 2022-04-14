frase = "don't panic!"
flista = list(frase)
print(frase)
print(flista)
for letra in range (4): #remove os 4 últimos caracteres
    flista.pop()
print(flista)
flista.remove("d") #remove a letra d
print(flista)
flista.extend([flista.pop(),flista.pop()]) #inverte "a" e "p"
print(flista)
flista.remove("'") #remove '
print(flista)
flista.insert(2,flista.pop(3)) #retira o espaço
# flista.extend([flista.pop(2),flista.pop(3)])
novaFrase = ''.join(flista) #unifica a lista em uma única string
print((novaFrase))

