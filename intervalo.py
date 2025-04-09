contagem = 0
cont2 = 0
for i in range(0, 10, 1):
    num = int(input("digite um nuemro"))
    if num >= 10 and num <= 20:
        contagem += 1

    else:
        cont2 = cont = 1

print(f"dentro do intervalo tem {contagem} numeros e fora tem {cont2}")
