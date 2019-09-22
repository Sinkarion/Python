
names = ['Василий', 'Анатолий', 'Павел', 'Сергей', 'Алексей', 'Александр']
salary = [13000, 25000, 38000, 79000, 90000, 55000]

list_info = dict(zip(names, salary))

#  print(list_info)

with open('salary.txt', 'a+', encoding='utf-8') as file:
    for key, item in list_info.items():
        if item < 50000:
            file.write('{} - {}\n'.format(key, item))
            file.seek(0)
            print(file.readlines())
file.close()
