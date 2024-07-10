contador = int(input("Informe quantos números você quer digitar: "))
list = []
cont = 0
for c in range(contador):
    X = int(input(f"Digite o {c+1}* número: "))
    list.append(X)
for i in list:
    if list[cont]%2!=0:
        print(f"Esse número é impar {list[cont]}.")
    else:
        print(f"Esse número não é impar {list[cont]}.")
    cont+=1