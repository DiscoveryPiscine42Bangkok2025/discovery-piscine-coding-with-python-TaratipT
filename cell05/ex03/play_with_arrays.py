ori = [2, 8, 9, 48, 8, 22, -12, 2]

new = []
for i in ori:
    if i > 5:
        num = i+2
        if num not in new:
            new.append(i+2)

new = set(new)

print(ori)
print(new)