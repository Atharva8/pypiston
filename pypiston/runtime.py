
class Runtime:
	def __init__(self,language:str, version:str):
		"""
		Creates a Runtime Class of the given language and version.
		"""
		self.language = language
		self.version = version
		self.runtime = {'language':language,'version':version}
	