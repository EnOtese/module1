immutable_var = ('Пельмени', True, 5)
print(immutable_var)
# immutable_var [0] = 'Макароны'  # Кортеж не поддерживает замену элементов, поэтому выдаёт ошибку. Кортеж - неизменняемый тип данных.
# print(immutable_var)
mutable_list = ['Водохранилище', False, 10]
mutable_list[0:3] = 200, 'Гидроэлектростанция', True
print(mutable_list)