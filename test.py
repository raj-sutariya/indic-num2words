import random
from tabulate import tabulate
from num_to_word import num_to_word, supported_lang

# test with user input numbers
# number = '0'
# while number != '':
#     number = input("Enter Num: ")
#     print(num_to_word(number, lang='te', combiner=' '))


# test module with random integer
data_list = []
header = ['num']
for _ in range(5):
    current_range = 1
    for _ in range(12):
        current_range = current_range*10
        i = random.randint(current_range, current_range*10)
        one_data = [i]
        for lang in supported_lang:
            one_data.append(num_to_word(i, lang=lang, separator=', ', combiner='-'))
            header.append(lang)
        data_list.append(one_data)

print(tabulate(data_list, headers=header))
