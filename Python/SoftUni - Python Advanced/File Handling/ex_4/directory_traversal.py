import os

PATH_DIR = './'
files = {}

for el in os.listdir(PATH_DIR):
    file = os.path.join(PATH_DIR, el)
    if os.path.isfile(file):
        extension = '.' + el.split('.')[-1]
        if extension not in files:
            files[extension] = []
        files[extension].append(el)

with open("report.txt", 'w') as report:
    for ext, file_names in sorted(files.items()):
        report.write(f'{ext}\n')
        for file in sorted(file_names):
            report.write(f"- - - {file}\n")