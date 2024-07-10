contador = int(input("Informe quantos números você quer digitar: "))
list = []
cont = 0
for c in range(contador):
    X = int(input(f"Digite o {c+1}* número: "))
    list.append(X)

list.sort()
print(f"O maior numero que você escreveu foi {list[0]}")
