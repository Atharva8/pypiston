from pypiston import Piston, CodeFiles, Runtime

piston = Piston()
codefiles = CodeFiles()
runtime = Runtime(language='python',version='*')
codefiles.add_file(filename='hello.py',content='print("Hello World")')
print(piston.execute(runtime, codefiles))