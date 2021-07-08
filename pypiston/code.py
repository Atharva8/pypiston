import os

class CodeFiles:
	"""
	Class to add files so as to be run by the Piston execute call
	"""
	def __init__(self):
		self.files = []

	def add_file(self, filename="",content=""):
		"""
		Add file without specifying a system file path.
		"""
		self.files.append({"name":filename,"content":content})

	def add_file_by_path(self, path:str):
		"""
		Add file from system's path.
		"""
		if not os.path.exists(path):
			raise Exception(message='Path does not exist')
		
		with open(path,'r') as file:
			content = file.read()

		filename = os.path.split(path)[1]

		self.files.append({"name":filename, "content":content}) 

