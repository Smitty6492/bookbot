#print("greetings boots")
def get_books_text(filepath):
    with open(filepath) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_books_text(book_path)
    #print(book_text)
    num_words = count_words(book_text)
    print(f"{num_words} words found in the document")

main()


