# list operations
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num = int(input())

items[num] = 'x'
print(items)

# find 'a' in string
s = input()

if 'a' in s:
    print('Match')
if not 'a' in s:
    print('No match')
