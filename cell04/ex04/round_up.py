roundup = float(input("Enter a decimal number: "))
if roundup.is_integer():
    print(int(roundup))
else:
    print(int(roundup) + 1)