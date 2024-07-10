num = []
x=0
contador = int(input("Quantos números você quer informar? "))
for c in range(contador):
    num2 = int(input(f"Escreva o {c+1}*: "))
    num.append(num2)
    x+=num2
print("Os números ")
for i in num:
    print(f"{i}, ", end="")
print(f"é igual = {x}")
