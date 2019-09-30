if __name__ == '__main__':
    import os
    import re
    import shutil


#  задание 1.1

def my_dir(name):
    try:
        os.makedirs(name)
    except FileExistsError:
        print('{} - директория уже существует'.format(name))


def r_dir(name):
    try:
        os.removedirs(name)
    except FileNotFoundError:
        print('{} - папка не найдена'.format(name))


def start():
    answer = ''
    number_dirs = range(1, 10)

    while answer != '3':

        answer = input('Выберите пункт меню:\n'
                       '1. Создать папки dir_1 - dir_9\n'
                       '2. Удалить папки dir_1 - dir_9\n'
                       '3. Выход\n')
        if answer == '3':
            break
        if answer == '1':
            for i in number_dirs:
                i = str(i)
                my_dir('dir_' + i)

        elif answer == '2':
            for i in number_dirs:
                i = str(i)
                r_dir('dir_' + i)


if __name__ == '__main__':
    start()


#  задание 1.2
def list_dir():
    buffer = os.listdir()
    print('Список папок:')
    for index, element in enumerate(buffer, start=1):
        if os.path.isdir(element):
            print('{}. {}'.format(index, element))


if __name__ == '__main__':
    list_dir()

#  задание 1.3

if __name__ == '__main__':
    def file_copy():
        name_file = os.path.realpath(__file__)
        new_file = name_file + '.copy'
        if os.path.isfile(new_file):
            shutil.copy(name_file, new_file)
            return new_file + ' - создан'
        else:
            return 'Файл уже скопирован'

if __name__ == '__main__':
    print(file_copy())
