from stats import get_num_words, create_dictionary, sort_on

def main():
    import sys
    import os

    if len(sys.argv) != 2:
         print("Usage: python3 main.py <path_to_book>")
         sys.exit(1)

    book = sys.argv[1]
    if os.path.exists(book):
        
        text = get_book_text(book)
        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        num_words = get_num_words(text)
        print(f"Found {num_words} total words")
        print("----------- Word Count ----------")
        character_count = create_dictionary(text)
        character_list = [{"char": char, "num": count} for char, count in character_count.items()]
        character_list.sort(reverse=True, key=sort_on)
        for item in character_list:
                if not item["char"].isalpha():
                    continue
                print(f"{item['char']}: {item['num']}")
        print("============= END ===============")
    else:
        print(f"{book} does not exist")
        sys.exit(1)

def get_book_text(book_name):
    """Return the text of the named book."""
    if book_name == "":
        return
    with open(f"{book_name}") as f:
        file_contents = f.read()
    return file_contents

main()
