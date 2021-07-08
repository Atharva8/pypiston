# pypiston
An API wraper for Piston implemented in Python

## Examples
Basic Hello World

```py
from pypiston import Piston, CodeFiles, Runtime

piston = Piston()
codefiles = CodeFiles()
runtime = Runtime(language='python',version='*')
codefiles.add_file(name='hello.py',content='print("Hello World")')
output = piston.execute(runtime, codefiles)
print(output)
```
Output:
```json
{'language': 'python', 'version': '3.9.4', 'run': {'stdout': 'Hello World\n', 'stderr': '', 'code': 0, 'signal': None, 'output': 'Hello World\n'}}
```

### Add files from system
```py
from pypiston import Piston, CodeFiles, Runtime

piston = Piston()
codefiles = CodeFiles()
runtime = Runtime(language='python',version='*')
codefiles.add_file_by_path('/example/path/hello.py')
output = piston.execute(runtime, codefiles)
print(output)

```