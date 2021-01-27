# file = open('001.txt')

# text = file.read()
# file.close()
# print(text)

# lines = file.readlines()
# print(lines)

# for line in lines:
#     print(line, end='')
    # print(line.strip())

# for line in file:
#     print(line.strip())

# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())

# file = open('001.txt', 'w')
# lines = ['qwe\n', 'asd\n', 'zxc\n']
# file.write('qwe')
# file.writelines(lines)
# file.close()

# file = open('001.txt')

# with open('001.txt') as file:
#     # with open('') as file_2:
#     print(file.read())
#     print(file.closed)
# print(file.closed)

with open('001.txt', 'r+', encoding='utf-8') as f:
    print(f)
    # print(f.closed)
    # print(f.mode)
    # print(f.name)
    # f.write('\n\n\asdasdasdasd\n\ansd\ansd\ansda\snda\nsdz')
    # f.seek(0)
    # print(f.read())


# with open("python.txt", "w") as f_obj:
#     print("Необычная работа функции print", file=f_obj)


import os
# print(os.getcwd())
# print(os.listdir())
# print(os.path.isdir('0610'))
# print(os.path.isfile('0610'))
# print(os.path.basename(r'C:\Users\ivan_\Desktop\gb_python_new\les_08\envs\pepsi\Scripts\python.exe'))
# print(os.path.splitext('python.exe'))
# main_folder = r'C:\Users\ivan_\Desktop\gb_python_new\les_08\envs'
# folder = 'Desktop'
# file_name = 'python.exe'
# print(os.path.join(main_folder, folder, folder, file_name))

import json
data = {'income': {'salary': 5000, 'bonus': 1000}}
# print(json.dumps(data))
# data = '{"income": {"salary": 5000, "bonus": 1000}}'
# print(json.loads(data)['income'])

with open('Vova.json', 'w', encoding='utf-8') as f_json:
    json.dump(data, f_json, ensure_ascii=False)


# with open('Vova.json') as f_json:
#     data_1 = json.load(f_json)
#     print(data_1)
#     print(type(data_1))

# import shutil
#
# shutil.copy('', '')

# import sys
# sys.argv
# sys.path
# sys.exit()
# print('qwe')