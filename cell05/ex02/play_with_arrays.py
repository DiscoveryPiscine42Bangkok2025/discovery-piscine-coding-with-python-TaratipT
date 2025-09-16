ori = [2, 8, 9, 48, 8, 22, -12, 2]
new = []
for i in ori:
    if i > 5:
        new.append(i+2)

print(f"Original array: {ori}")
print(f"New array: {new}")