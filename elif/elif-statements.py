# age checker

age = int(input())
name = input()

if age >= 18:
    print("Welcome " + name)
else:
    print('Sorry')

# right-angled triangle checker

side1 = int(input())
side2 = int(input())
side3 = int(input())

sum_of_squares = side1 * side1 + side2 * side2
square_of_hypotenuse = side3 * side3

if sum_of_squares == square_of_hypotenuse:
    print('Right-angled')
else:
    print("Not right-angled")

# color categorizer

color = input()

if color == 'red':
    print(1)
elif color == 'green':
    print(2)
elif color == 'black':
    print(3)

# number checker
number = int(input())

if number % 2 == 0:
    print(number * 2)
elif number % 2 == 1:
    print(number * 3)
else:
    print(0)
