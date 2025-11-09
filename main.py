from stats import get_num_words, get_char_counts, get_chars_sorted
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]
text = get_num_words(book_path)
num_words = len(text.split())
char_counts = get_char_counts(text)
print("============ BOOKBOT ============")
print(f"Analyzing book found at {num_words}...")
print("----------- Word Count ----------")
print(f"Found {num_words} total words")
print("--------- Character Count -------")
for char in get_chars_sorted(char_counts):
    print(f"{char["char"]}: {char["num"]}")
