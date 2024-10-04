def main():
	get_path = "books/frankenstein.txt"
	text = get_book(get_path)
	print(text)

def get_book(path):
	with open (path) as f:
		return f.read()

main()   
