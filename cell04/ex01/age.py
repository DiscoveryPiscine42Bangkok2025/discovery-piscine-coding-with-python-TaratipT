age = int(input("Please tell me your age: "))
print(f"You are currently {age} years old.")

for i in range(1,4):
    next = 10*i
    age += 10
    print(f"In {next} years, you'll be {age} years old.")
    