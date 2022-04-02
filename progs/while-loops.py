# magic box (doubles items every day)

items = int(input())
days = int(input())
i = 1

while i <= days:
    items *= 2
    i += 1

print(items)

# even numbers
x = 0
while x <= 10:
    if x % 2 == 0:
        print(x)

    x += 1
