string1 = input("Entre com uma string: ")
string2 = ''
temp = []

for letra in string1:
    temp.append(letra)

index = len(temp) - 1

for letra in range(index, -1, -1):
    string2 += temp[letra]

print(string2)

