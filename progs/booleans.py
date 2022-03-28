# humidity checker

humidity = int(input())
if humidity >= 40 and humidity <= 60:
    print('norm')

# is store open?
hour = int(input())
day = int(input())

if day >= 1 and day < 6 and hour >= 10 and hour <= 21:
    print('Open')
else:
    print('Closed')

# age groups
age = int(input())

if age >= 0 and age <= 11:
    print('Child')
elif age >= 12 and age <= 17:
    print('Teen')
elif age >= 18 and age <= 64:
    print('Adult')
else:
    print('Senior')
