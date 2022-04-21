shots = 4
score = 100

while shots > 0:
    result = input()
    if result == "hit":
        score += 10
        shots -= 1
    elif result == "miss":
        score -= 20
        shots -= 1
print(score)
