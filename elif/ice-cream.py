# Let's imagine you want to buy an ice-cream for 10 of your friends.
# Write a program that will take the money you have and the price of one ice-cream,
# and will output the remaining money only if you can buy that ice-cream for your all 10 friends.


money = int(input())
price = int(input())

total = price*10
money_left = money - total

if money_left >= 0:
    print(money_left)
