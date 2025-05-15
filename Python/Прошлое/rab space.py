glasnii = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"

slovo = input()
tsepoch = list(slovo)
print(tsepoch)

nu = -1

def glasna(letter):
    letter = tsepoch[nu+1]
    return letter in glasnii
otvet = glasna(tsepoch[0])
if otvet == True:
    tsepoch[0], tsepoch[-1] = tsepoch[-1], tsepoch[0]
    print(tsepoch)
else:
    tsepoch[0], tsepoch[1] = tsepoch[1], tsepoch[0]
    print(tsepoch)

text = ""
for element in tsepoch:
    text += f'{element}'
print(text)