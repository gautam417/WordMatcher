import sys
import re
from collections import defaultdict

def read_file(filepath):
    """ Read a file and return its content as a list of lines. """
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.readlines()

def count_matches(text_lines, predefined_words):
    """ Count matches of predefined words in the given text lines. """
    word_count = defaultdict(int)
    word_pattern = re.compile(r'\b\w+\b')  # Regular expression to match words
    
    for line in text_lines:
        words = re.findall(word_pattern, line.lower())  # Find all words in lowercase
        for word in words:
            if word in predefined_words:
                word_count[word] += 1
    
    return word_count

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <path_to_input_file> <path_to_predefined_words_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    predefined_words_file = sys.argv[2]
    
    try:
        # Read input file
        text_lines = read_file(input_file)
        
        # Read predefined words with original capitalization
        predefined_words = {}
        with open(predefined_words_file, 'r', encoding='utf-8') as f:
            for line in f:
                word = line.strip()
                predefined_words[word.lower()] = word
        
        # Count matches
        word_count = count_matches(text_lines, predefined_words)
        
        # Print output
        print("Predefined word     Match count")
        for word in predefined_words.values():
            if word.lower() in word_count:
                print(f"{word.ljust(20)} {word_count[word.lower()]}")
            else:
                print(f"{word.ljust(20)} 0")  # Print 0 if the word has no matches
    
    except FileNotFoundError:
        print("File not found. Please check the file paths and try again.")
        sys.exit(1)

if __name__ == "__main__":
    main()
