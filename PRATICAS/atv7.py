contador = int(input("Quantas palavras voce vai escrever? "))
list = []
cont = 0

for c in range(contador): 
    A = input(f"Escreva a {c+1}* palavra: ")
    list.append(A) 

for i in list:
    if  cont== 0:
        maior=len(i)
        indice=cont
    elif len(i)>maior:
        maior=len(i)
        indice=cont
    cont+=1

print(f"A maior palavra é: {list[indice]}")    
