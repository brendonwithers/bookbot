def text_number(text):
    words = text.split()
    count = len(words)
    return count

def character_count(text):
    char_count ={}
    text = text.lower()
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sorted_char(char_count):
    sorted_count = dict(sorted(char_count.items(), key = lambda item: item[1], reverse=True))
    return sorted_count