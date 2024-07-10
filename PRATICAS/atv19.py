contador = int(input("Informe quantos números você irá digitar: "))
list = []
cont = 0
for c in range(contador):
    X = int(input(f"Digite o {c+1}* número: "))
    list.append(X)
list.sort()
print("A ordem crescente desses números é:")
for i in list:
    print(list[cont])
    cont+=1

