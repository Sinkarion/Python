#  задание 1.1


def man_info(a, b, c):
    print(name, age, 'год(а),', 'проживает в городе', city, '.')


name = input('введите имя: ')
age = input('введите возраст: ')
city = input('укажите город проживания: ')

man_info(name, age, city)


#  задание 1.2


def max_number(a, b, c):
    data = [a, b, c]
    max_n = (max(data))
    return max_n


a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))

result = max_number(a, b, c)
print('Максимальное число: ', result)


#  задание 1.3

def max_str(*args):
    max_len = max(args, key=len)
    return max_len


str_1 = input('Введите первое слово: ')
str_2 = input('Введите второе слово: ')
str_3 = input('Введите третье слово: ')

result = max_str(str_1, str_2, str_3)
print('Самое длинное слово: ', result)
