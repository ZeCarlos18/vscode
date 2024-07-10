contador = int(input("Informe quatas palavras você quer digitar: "))
list = []
c = 0
z = 0
for c in range(contador):
    X = input(f"Informe a {c+1}* palavra: ")
    list.append(X)
for i in list:
    if i[0]=='a':
        print(f"A palavra: {list[z]} começa com: a")
    elif i[0]=='A':
        print(f"A palavra: {list[z]} começa com: A")
    z+=1
