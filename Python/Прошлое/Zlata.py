a = 1023456789876543201
forcount = list(str(a))
while not (a % 9 == 0 and forcount == forcount[::-1] and forcount.count("0") >= 1 and forcount.count("1") >= 1 and forcount.count("2") >= 1 and forcount.count("3") >= 1 and forcount.count("4") >= 1 and forcount.count("5") >= 1 and forcount.count("6") >= 1 and forcount.count("7") >= 1 and forcount.count("8") >= 1 and forcount.count("9") >= 1):
    a += 1
    print(a)
    forcount = list(str(a))
print(a)
