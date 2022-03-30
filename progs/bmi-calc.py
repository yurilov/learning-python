weight = int(input())
height = float(input())

bmi = weight / (height * height)

if bmi < 18.5:
    print('Underweight')
elif bmi < 25:
    print('Normal')
elif bmi < 30:
    print('Overweight')
else:
    print('Obesity')

# card type
type = input()
if type == 'Visa' or type == 'Amex':
    print('accepted')

# discount level

score1 = int(input())
score2 = int(input())
average = (score1 + score2) / 2

if average <= 100 and average >= 90:
    print(50)
elif average <= 89 and average >= 80:
    print(30)
elif average <= 79 and average >= 70:
    print(10)
else:
    print(0)
