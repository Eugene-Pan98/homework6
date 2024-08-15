my_dict = {'Anastasia': 1998, 'Max': 2000, 'Dima': 2003, 'Ludmila': 1998}
print(my_dict)
print(my_dict['Max'])
print(my_dict.get('Toma'))
my_dict.update({'Toma': 1986, 'Vova': 2001})
my_dict.pop('Max')
print(my_dict)
#
my_set = {1, 2, 3, 3, True, 6, 'string'}
print(my_set)
my_set.update([4, 5])
my_set.discard(1)
print(my_set)
