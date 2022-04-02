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

# sum of digits in number
n = int(input())

length = 0
sum = 0

while n > 0:
    sum += n % 10
    n //= 10
    length += 1

# print(length)

print(sum)
