data = [7, 5, 6.9, 1, 8, 42, 33, 128, 1024, 2, 8, 11, 0.4, 1024, 66, 809, 11, 8.9, 1.1, 3.42, 9, 100, 444, 78]

data.remove(min(data))
data.remove(max(data))

sum = 0

for n in data:
    sum += n
    
print(sum)
