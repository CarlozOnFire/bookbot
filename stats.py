def num_words(book_text):
    words = book_text.split()
    return len(words)


def character_count(book_text):
    characters = book_text.lower()
    count_chars ={}
    for letter in characters:
        if letter not in count_chars:
            count_chars[letter] = 1
        else:
            count_chars[letter] += 1
    return count_chars
            

def sort_on(item):
    return item["num"]

def build_char_list(char_counts):
    chars = []
    for char, count in char_counts.items():
        chars.append({"letter": char, "num": count})
    return chars





