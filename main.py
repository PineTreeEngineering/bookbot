from stats import count_words
from stats import count_char
from stats import sort_char
import sys

arg = sys.argv
if len(arg) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book = sys.argv[1]

def get_book_text(filepath):
    with open(filepath) as f:
        book = f.read()
    return book


def main():
    text = get_book_text(book)
    words = count_words(text)
    count = count_char(text)

    print(
        "============ BOOKBOT ============\n"
        f"Analyzing book found at {book}...\n"
        "----------- Word Count ----------\n"
        f"Found {words} total words\n"
        "--------- Character Count -------"
    )

    sorted = sort_char(count)

    for i in sorted:
        if i["char"].isalpha():
            print(f'{i["char"]}: {i["num"]}')
        else:
            continue

    print("============= END ===============")


main()
