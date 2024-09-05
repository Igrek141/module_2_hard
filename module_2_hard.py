first = int(input('Введите число в первый камень от 3 до 20: '))
list_ = []
for i in range(1, first):
    for j in range(i + 1, first):
        if first % (i +j) == 0:
            list_1 = list_.append(i)
            list_2 = list_.append(j)
converted_list = map(str, list_)
result = ''.join(converted_list)
print(first, ' - ', result)