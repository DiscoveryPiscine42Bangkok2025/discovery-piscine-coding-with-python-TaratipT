print("Enter the first number: ")
num1 = int(input())
print("Enter the second number: ")
num2 = int(input())

result = num1 * num2
print(f"{num1} x {num2} = {result}")

if result < 0:
    print("This result is negative.")
elif result == 0:
    print("This result is positive and negative.")
else:
    print("This result is positive.")