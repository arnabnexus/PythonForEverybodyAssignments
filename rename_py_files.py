import os

root = r'c:/GitRepo/PromptDevelopment/PythonForEverybody'

for dirpath, _, filenames in os.walk(root):
    for name in filenames:
        if not name.endswith('.py'):
            continue
        lower_name = name.lower()
        if lower_name == name:
            continue
        old_path = os.path.join(dirpath, name)
        new_path = os.path.join(dirpath, lower_name)
       
        os.rename(old_path, new_path)
        print(f'Renamed: {name} -> {lower_name}')
