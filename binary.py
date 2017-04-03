number = int(input("Please enter a decimal number to transform into binary number: "))
number1 = number
b = ""
for i in range(15, -1, -1):
    c = number // (2**i)
    r = number % (2**i)
    if c != 0:
        b += "1"
        number = r
        if b == ("0" * (15-i)) + "1":
            b = "1"
    else:
        b += "0"
        if b == ("0" * 16):
            b = 0
print("Number {} is in binary represented like {}". format(number1, b))

number = int(input("Please enter a decimal number to transform into octal number: "))
d = ""
number1 = number
for i in range(9, -1, -1):
    c = int(number // (8**i))
    r = int(number % (8**i))
    if c != 0:
        d += str(c)
        number = r
        if d == ("0" * (9-i)) + str(c):
            d = str(c)
    else:
        d += "0"
        if d == ("0" * 9):
            d = "0"
print("Number {} is in octal represented like {}". format(number1, d))
