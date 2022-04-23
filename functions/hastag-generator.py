s = input()


def hashtagGen(text):
    hashtag = text.replace(' ', '')
    return '#' + hashtag


print(hashtagGen(s))
