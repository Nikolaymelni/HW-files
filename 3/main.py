import os
list_ = []
list_name = os.listdir('sorted')
for i in list_name:
    with open(f'sorted/{i}', encoding='utf-8') as file:
        lines = file.readlines()
        lines = [i + '\n'] + [str(len(lines)) + '\n'] + lines
        list_.append(lines)

text = ''.join(sum((sorted(list_, key=len)), []))


with open('complete.txt', 'w', encoding='utf-8') as result:
    result.write(text)
