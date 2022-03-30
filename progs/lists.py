# vending machine
fruits = ["apple", "cherry", "banana", "kiwi",
          "lemon", "pear", "peach", "avocado"]
num = int(input())

if num < 0 or num > 7:
    print("Wrong number")
else:
    print(fruits[num])

# strings can be indexed like lists
text = input()

print(text[2])
