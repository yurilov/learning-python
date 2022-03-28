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
