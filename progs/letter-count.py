def letter_count(text, letter):
    count = 0
    for l in text:
        if l == letter:
            count +=1
    return count

text = input()
letter = input()

print(letter_count(text, letter))
