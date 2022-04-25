file = open("/pull_ups.txt")
n = int(input())

p = file.readlines()

print(p[n])
file.close()
