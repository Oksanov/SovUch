# a = list(input())
# length = len(a)//2
# chislo = 0

# while length != chislo // 2():
#     itog =+ (a[chislo]*int(a[chislo+1]))
# print(itog)

a = list(input())
n = len(a) // 2
print(n)

itog = 0
chislo = 0

while chislo < n * 2:
    itog += int(a[chislo]) * int(a[chislo + 1])
    chislo += 2

print(itog)