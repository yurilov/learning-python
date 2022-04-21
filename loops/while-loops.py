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

# an infinite loop to continuously take user input
items = []

while True:
    n = int(input())
    if n == 0:
        break
    items.append(n)

print(items)

# get item for free if price is odd

items = [23, 555, 666, 123, 128, 4242, 990]

sum = 0
n = 0

while n < len(items):

    num = items[n]
    n += 1

    if num % 2 == 1:
        continue

    sum += num

print(sum)
