def get_num_words(path):
    with open(path) as f:
        contents = f.read()
    return contents


def get_char_counts(text):
    char_count = {}

    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count
