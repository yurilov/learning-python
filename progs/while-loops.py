# magic box (doubles items every day)

items = int(input())
days = int(input())
i = 1

while i <= days:
    items *= 2
    i += 1

print(items)
