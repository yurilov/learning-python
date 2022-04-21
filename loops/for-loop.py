cart = [15, 42, 120, 9, 5, 380]

discount = int(input())
total = 0

for item in cart:
    total += item

total = total - total*discount/100

print(total)
