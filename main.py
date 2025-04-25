import sys
from stats import get_num_words
from stats import get_num_characters
from stats import sorted_char_dict

def main():
	if len(sys.argv) == 2:
		print("========== BOOKBOT ============")
		print(f"Analyzing book found at {sys.argv[1]}") 
		print("----------- Word Count ----------") 
		print(f"Found {get_num_words(sys.argv[1])} total words")
		print("--------- Character Count -------") 
		chars = sorted_char_dict(sys.argv[1])
		for char_dict in chars:
    			if char_dict["char"].isalpha():
        			print(f"{char_dict['char']}: {char_dict['num']}")
		print("============= END ===============")
	else:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
main()
