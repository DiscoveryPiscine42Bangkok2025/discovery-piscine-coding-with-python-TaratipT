import sys

if len(sys.argv) == 3:
    key = sys.argv[1]
    value = sys.argv[2]
    value = value.count(key)
    if value != 0:
        print(value)
    else:
        print("none")
else:
    print("none")