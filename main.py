from stats import get_num_words, get_char_counts

text = get_num_words("./books/frankenstein.txt")
num_words = len(text.split())
print(f"Found {num_words} total words")
print(get_char_counts(text))
