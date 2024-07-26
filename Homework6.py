my_dict = {'Сергей': 2008, 'Саша': 1999, 'Тимур': 2007}
print('Dict: ', my_dict)
print('Existing value: ', my_dict.get('Сергей'))
print('Not existing value: ', my_dict.get('Маша'))
my_dict.update({'Алексей': 1989,
                'Арсений': 2010})
a = my_dict.pop('Саша')
print('Deleted value: ', a)
print('Modified dictionary: ', my_dict)

my_set = {1, 2, 1, 2, (5, 4), (5, 4), 'Краска', 'Краска'}
print('Set: ', my_set)
my_set.add(99), my_set.add(44)
my_set.remove('Краска')
print('Modified set: ', my_set)