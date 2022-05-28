from pyperclip import copy
from sys import argv
from file_tasks import get_file_content

def main():
	file_path = argv[1]
	file_content = get_file_content(file_path)
	copy(file_content)
	print('File content copied to clipboard!')
	pass

if __name__ == "__main__":
	main()

