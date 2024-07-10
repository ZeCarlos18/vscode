contador = int(input("Informe quantos números você quer digitar: "))
list = []
cont = 0
Z = 0
for c in range(contador):
    X = int(input(f"Digite o {c+1}* número: "))
    list.append(X)
for i in list:
    X=list[cont]
    Z+=X
    cont+=1
media = Z/contador
print(f"A media dos números que você me informou é {media}.")