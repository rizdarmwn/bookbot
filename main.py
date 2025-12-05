import sys

from stats import get_char_count, get_words_count, sorted_dict


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    try:
        text = get_book_text(book_path)
        num_words = get_words_count(text)
        chars = get_char_count(text)
        sorted_chars = sorted_dict(chars)

        print("============ BOOKBOT ============")
        print(f"Analyzing boot found at {book_path}")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for c in sorted_chars:
            if c["char"].isalpha():
                print(f"{c['char']}: {c['num']}")
        print("============= END ===============")
    except FileNotFoundError:
        print("book not found, most likely path is incorrect")
    except Exception as e:
        print(e)


main()
