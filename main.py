import sys

def main():
    print("============ BOOKBOT ============")

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]

    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    book_text = get_book_text(book_path)

    word_count = num_words(book_text)
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")

    char_counts = character_count(book_text)

    chars = build_char_list(char_counts)
    chars.sort(reverse=True, key=sort_on)
    filtered_chars = [char for char in chars if char["letter"].isalpha()]
    for char in filtered_chars:
        print(f"{char['letter']}: {char['num']}")


    




from stats import num_words, character_count, sort_on, build_char_list




def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents



main()
