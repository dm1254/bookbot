def main():
	get_path = "books/frankenstein.txt"
	text = get_book(get_path)
	print(text)
	word_count = number_of_words(text)
	print(f"Beginning of {get_path} book report\n") 
	print(f"Word Count:{word_count} \n")
	Character_count = character_count(text)
	sorted_char = sort(Character_count)
	for char, count in sorted_char:
		if char.isalpha():
			print(f"The '{char}' character was found {count} times")
	print(f"End of {get_path} report")
def get_book(path):
	with open (path) as f:
		return f.read()

def number_of_words(book):
	return len(book.split())

def character_count(Text):
	lowered_char = Text.lower()
	character_dict = {}
	for i in range(0,len(lowered_char)):
		character = lowered_char[i]
		if character in character_dict:
			character_dict[character] += 1
		else:
			character_dict[character] = 1
	return character_dict

def sort(dict):
	
	sorted_items = sorted(dict.items(), key=lambda x: x[1], reverse=True)
	return sorted_items

main()  
