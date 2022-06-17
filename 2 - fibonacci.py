termo1 = 0
termo2 = 1

final = int(input("Entre com um número: "))

while termo2 < final:
    temp = termo1
    termo1 = termo2
    termo2 += temp

if termo2 != final:
    print(f"O número {final} não se encontra na sequêcia de fibonacci.")
else:
    print(f"O número {final} se encontra na sequência de fibonacci !!")