total = 0
passengers = 5
while passengers > 0:
    age = int(input())
    if age <= 3:
        passengers -= 1
        continue
    else:
        passengers -= 1
        total += 100
print(total)
