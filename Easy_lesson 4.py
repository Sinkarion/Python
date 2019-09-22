# coding=utf-8
#  задание 1.1

my_list = [3, 6, 14, 0, 28, 47]
new_list = [a ** 2 for a in my_list]
print(new_list)


#  задание 1.2

list_one = ['мандарин', 'киви', 'апельсин', 'банан', 'груша', 'яблоко']
list_two = ['банан', 'киви', 'грейпфрукт', 'яблоко']
list_sort = list(set(list_one) and set(list_two))
print('Фрукты, находящиеся в обоих списках:' , list_sort)


#  задание 1.3

data_list = [3, 4, 18, -5, 28, -12, 47, 32]
list_elements = [x for x in data_list if x % 3 == 0 and x >= 0 and x % 4]
print('Положительные числа, кратные 3, не кратные 4:' , list_elements)
