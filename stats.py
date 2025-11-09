def get_num_words(path):
    with open(path) as f:
        contents = f.read()
    return contents


def get_char_counts(text):
    char_count = {}

    for char in text:
        char = char.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count


def get_chars_sorted(dict):
    char_list = []

    for char in dict:
        if char.isalpha():
            char_list.append({"char": char, "num": dict[char]})

    char_list.sort(key=lambda x: x["num"], reverse=True)
    return char_list
