
def get_file_content(file_path: str) -> str:
	with open(file_path, 'r') as file:
		content = file.read()
	return content

