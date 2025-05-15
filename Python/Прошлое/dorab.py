word = input()
reword = ''
num = -1
# print('Расшифровать или зашифровать?')
# pac_il_shif = input().upper
# if pac_il_shif == 'Расшифровать':
for i in range(len(word)):
        num += 1
        if num >= 0:
            reword += word[num * 2]
        else:
              reword += word[num * -1 + (num * -1 - 1)]

# s = input()
# s = s.split(' ')
# A = []
# for i in range(len(s)):
#   if i % 2 != 1:
#     A += s[i]
# print(A)