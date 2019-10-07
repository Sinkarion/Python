if __name__ == '__main__':
    import os
    import Easy_lesson_5


    def change_dir(path):
        try:
            os.chdir(path)
            return 'Успешно перешли в папку: {}'.format(path)
        except FileNotFoundError:
            return 'dir_{} - папки не существует'.format(path)


    def start():
        answer = ''
        while answer != '5':
            print('Текущая директория: ' + os.getcwd())
            answer = input('Выберите пункт меню:\n'
                           '1. Перейти в папку\n'
                           '2. Помотреть содержимое текущей папки\n'
                           '3. Удалить папку\n'
                           '4. Создать папку\n'
                           '5. Выход\n')
            if answer == '5':
                break
            if answer == '1':
                path_name = input('Укажите папку для перехода: ')
                print(change_dir(path_name))
            elif answer == '2':
                Easy_lesson_5.list_dir()
            elif answer == '3':
                name = input('Введите имя удаляемой папки: ')
                Easy_lesson_5.r_dir(name)
            elif answer == '4':
                name = input('Введите имя новой папки: ')
                Easy_lesson_5.my_dir(name)

if __name__ == '__main__':
    start()
