contador = int(input("Informe quantos números você quer digitar: "))
list = []
cont = 0
Z = 0
for c in range(contador):
    X = int(input(f"Digite o {c+1}* número: "))
    list.append(X)
for i in list:
    if list[cont]%2==0:
        Z+=list[cont]
    cont+=1
print(f"A soma de todos os números pares que você escreveu é: {Z}.")