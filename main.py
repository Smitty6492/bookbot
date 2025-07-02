#print("greetings boots")
from stats import get_num_words
from stats import get_char_counts
from stats import sort_char_counts

def get_books_text(filepath):
    with open(filepath) as f:
        return f.read()



def main():
    """
    book_path = "books/frankenstein.txt"
    book_text = get_books_text(book_path)
    
    #print(book_text)
    
    num_words = get_num_words(book_text)
    print(f"{num_words} words found in the document")
    
    char_counts = get_char_counts(book_text)
    print(char_counts)
    """
    book_path = "books/frankenstein.txt"
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


