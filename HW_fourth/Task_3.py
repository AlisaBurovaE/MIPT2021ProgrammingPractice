import os
import zipfile
with zipfile.ZipFile('C:/Users/MI/Documents/прога/local_repo/MIPT2021ProgrammingPractice/HW_fourth/main.zip') as zip:
    zip.extractall('C:/Users/MI/Documents/прога/local_repo/MIPT2021ProgrammingPractice/HW_fourth')

list = list()

os.chdir("C:/Users/MI/Documents/прога/local_repo/MIPT2021ProgrammingPractice/HW_fourth/main")
for current_dir, dirs, files in os.walk("."):
    for names in files:
        if names[-2:] == 'py':
            list.append(current_dir)
print(sorted(list))
