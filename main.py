import sys
from stats import text_number
from stats import character_count
from stats import sorted_char

def get_book_text(file_path):
    with open(file_path, "r", encoding ="utf-8") as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    file_path = sys.argv[1]
   
    text = get_book_text(file_path)

    print(f"Found {text_number(text)} total words")

    char_count = character_count(text)
    print(char_count)

    sorted_count = sorted_char(char_count)
    for char, count in sorted_count.items():
       print(f"{char}: {count}")


main()