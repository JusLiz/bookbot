def get_num_words(path_to_file):
        with open(path_to_file) as f:
                file_contents = f.read()
                word_count = len(file_contents.split())
        return word_count
def get_num_characters(path_to_file):
	with open(path_to_file) as f:
		file_contents = f.read()
	char_dict = {}
	for char in file_contents.lower():
		if char in char_dict:
			char_dict[char] += 1
		else:
			char_dict[char] = 1
	return char_dict

def sorted_char_dict(path_to_file):
	dict = get_num_characters(path_to_file)
	char_num_list = []
	for key, value in dict.items():
		char_num_dict = {"char": key, "num": value}
		char_num_list.append(char_num_dict)
	def sort_on(dict):
		return dict["num"]
	char_num_list.sort(reverse=True, key=sort_on)
	return char_num_list

