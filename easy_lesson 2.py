#  coding=utf-8
#  задание 1.1

fruits = ('яблоко', 'банан', 'киви', 'гранат', 'грейпфрукт', 'апельсин', 'лемон')

x = 0
while x < len(fruits):
    for i in range(len(fruits)):
        print(i + 1, fruits[x])
        x += 1

#  задание 1.2

list_one = [47, 32, 14, 58, 96, 88]
list_two = [24, 47, 14, 56, 96, 22, 14]

x = 0
while x < len(list_one):
    for same in list_two:
        if same in list_one:
            list_one.remove(same)
            x += 1
print('из первого списка удалены повторяющиеся элементы\nоставшиеся элементы:', list_one)

#  задание 1.3

source = [4, 16, 47, 32, 14, 96, 83, 56]
result = []
elements = len(source)
for i in range(elements):
    if source[i] % 2 == 0:
        result.append(source[i] / 4)
else:
    result.append(source[i] * 2)
    print(result)







