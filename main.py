#print("greetings boots")
import sys
from stats import get_num_words
from stats import get_char_counts
from stats import sort_char_counts


def get_books_text(filepath):
    with open(filepath) as f:
        return f.read()



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    """
    book_path = "books/frankenstein.txt"
    book_text = get_books_text(book_path)
    
    #print(book_text)
    
    num_words = get_num_words(book_text)
    print(f"{num_words} words found in the document")
    
    char_counts = get_char_counts(book_text)
    print(char_counts)
    """
    book_path = sys.argv[1]
    book_text = get_books_text(book_path)

    num_words = get_num_words(book_text)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    char_counts = get_char_counts(book_text)
    sorted_chars = sort_char_counts(char_counts)

    print("--------- Character Count -------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")
    
    
main()


