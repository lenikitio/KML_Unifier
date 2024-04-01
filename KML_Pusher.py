import os

project_name = input("Введите шифр проекта: ")

if os.path.isdir('.git') != True:
    os.system('git init')
    os.system(f'git remote add origin https://github.com/lenikitio/{project_name}.git')
    os.system('git branch -M main')
    os.system('git push -u origin main')
file = "field_data.kml"
os.system(f'git add {file}')
os.system(f'git commit -m "flight"')
os.system('git push')