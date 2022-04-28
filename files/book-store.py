file = open("/usercode/files/books.txt", "r")

lines = file.readlines()
for line in lines:
    film = line.replace("\n", "")
    print(film[0] + str(len(film)))
file.close()
