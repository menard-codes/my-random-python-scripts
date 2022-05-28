from sys import argv
from file_tasks import get_file_content

def count_words(string: str) -> int:
	return len(' '.join(string.split('\n')).split(' '))

def main():
	try:
		file_path = argv[1]
		file_content = get_file_content(file_path)
		print('Word count:', count_words(file_content))
	except IndexError:
		print('Error: Please enter the file path')
	except FileNotFoundError:
		print('Error: File doesn\'t exist')

if __name__ == "__main__":
	main()

