def get_book_text(path):
    with open(path) as f:
        contents = f.read()
    return contents


text = get_book_text("./books/frankenstein.txt")
num_words = len(text.split())
print(f"Found {num_words} total words")
