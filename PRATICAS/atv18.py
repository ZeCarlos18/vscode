contador = int(input("Informe quantos números você irá digitar: "))
list = []
cont = 0
for c in range(contador):
    X = int(input(f"Digite o {c+1}* número: "))
    list.append(X)
V = 1
for i in list:
    V = list[cont]*V
    cont+=1
print(f"A multiplicação de todos os númeors que você informou é: {V}.")
