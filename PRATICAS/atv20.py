contador = int(input("Informe quantos números você irá digitar: "))
list = []
cont = 0
num = contador-1
for c in range(contador):
    X = int(input(f"Digite o {c+1}* número: "))
    list.append(X)
list.sort()
print("A ordem decrescente desses números é:")
for i in list:
    print(list[num])
    num-=1

