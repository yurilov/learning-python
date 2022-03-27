age = int(input())
name = input()

if age >= 18:
    print("Welcome " + name)
else:
    print('Sorry')


side1 = int(input())
side2 = int(input())
side3 = int(input())
# your code goes here
sum_of_squares = side1 * side1 + side2 * side2
square_of_hypotenuse = side3 * side3

if sum_of_squares == square_of_hypotenuse:
    print('Right-angled')
else:
    print("Not right-angled")
