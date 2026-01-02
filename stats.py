chars = {}

def count_words(text):
    words = text.split()
    return(len(words))

def count_char(text):
    for letter in text:
        c = letter.lower()
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return(chars)

def sort_on(items):
    return items["num"]

def sort_char(d):
    sorted_list = []
    for i in d:
        sorted_list.append({"char": i, "num": d[i]})
    sorted_list.sort(reverse=True, key=sort_on)

    return(sorted_list)

