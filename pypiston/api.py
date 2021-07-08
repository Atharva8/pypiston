import requests
from .runtime import Runtime
from .code import CodeFiles


class Piston:
	"""
	The main class which makes api calls to the piston engine
	"""
	def __init__(self, api_url=' https://emkc.org/api/v2/piston'):
		self.base_url = api_url
	
	def execute(self,runtime:Runtime, codefiles:CodeFiles,**kwargs):
		"""
		Executes the files in the CodeFiles class of the given Runtime.
		Pass optional arguments such as stdin, compile_timeout in **kwargs.
		"""
		exec_data={'language':runtime.language,'version':runtime.version}
		exec_data['files'] = codefiles.files
		exec_data.update(kwargs)
		res = requests.post(self.base_url+"/execute",json=exec_data)
		return res.json()

	def get_runtimes(self):
		"""
		Gets all of the runtimes availabe.
		"""
		res = requests.get(self.base_url+'/runtimes')
		if res.status_code != 200:
			raise Exception(message='Failed to get runtimes')
		return res.json()

	def check_runtime(self,runtime:Runtime):
		"""
		Checks if the given runtime exists
		"""
		availabe_runtimes = self.get_runtimes()
		return runtime.runtime in availabe_runtimes