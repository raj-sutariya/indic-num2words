"""
Method to convert Numbers to Words
for indian languages

Use cases:-
1) Speech recognition pre-processing
2) Language modeling Data pre-processing

-------------------------
check indic_numbers.py to add support
for any indian language
"""
from indic_numbers import supported_lang
from indic_numbers import all_num
from indic_numbers import num_dict


def num_to_word(num, lang, separator=' '):
    """
    Main Method
    :param num: Number digits from any indian language
    :param lang: Language Code from supported Language
    :param separator: Separator character
    :return: UTF-8 String of numbers spoken in words
    """
    lang = lang.lower()
    num = str(num)

    # Load dictionary according to language code
    assert lang in supported_lang, 'Language not supported'
    num_dic = num_dict[lang]

    # Remove punctuations from numbers
    num = str(num).replace(',', '')

    # Replace native language numbers with english digits
    for language in supported_lang:
        for num_index in range(10):
            num = num.replace(all_num[language][num_index], all_num['en'][num_index])

    # Assert that input contains only integer number
    for digit in num:
        assert digit in all_num['en'], "Give proper input"

    # Process
    # For Number longer than 9 digits
    def all_two_digit(digits_2):
        if len(digits_2) <= 1:                          # Provided only one/zero digit
            return num_dic.get(digits_2, '')
        elif digits_2 == '00':                          # Two Zero provided
            return num_dic['0'] + separator + num_dic['0']
        elif digits_2[0] == '0':                        # First digit is zero
            return num_dic['0'] + separator + num_dic[digits_2[1]]
        else:                                           # Both digit provided
            return num_dic[digits_2]

    # For Number less than 9 digits
    def two_digit(digits_2):
        digits_2 = digits_2.lstrip('0')
        if len(digits_2) != 0:
            return num_dic[digits_2]
        else:
            return ''

    def all_digit(digits):
        digits = digits.lstrip('0')
        if len(digits) == 9:
            return num_dic[digits[:2]] + num_dic['10000000'] + separator + all_digit(digits[2:])
        elif len(digits) == 8:
            return num_dic[digits[:1]] + num_dic['10000000'] + separator + all_digit(digits[1:])
        elif len(digits) == 7:
            return num_dic[digits[:2]] + num_dic['100000'] + separator + all_digit(digits[2:])
        elif len(digits) == 6:
            return num_dic[digits[:1]] + num_dic['100000'] + separator + all_digit(digits[1:])
        elif len(digits) == 5:
            return num_dic[digits[:2]] + num_dic['1000'] + separator + all_digit(digits[2:])
        elif len(digits) == 4:
            return num_dic[digits[:1]] + num_dic['1000'] + separator + all_digit(digits[1:])
        elif len(digits) == 3:
            return num_dic[digits[:1]] + num_dic['100'] + separator + two_digit(digits[1:])
        else:
            return two_digit(digits)

    num = num.lstrip('0')
    digit_len = len(num)

    if digit_len == 0:
        output = num_dic['0']
    elif digit_len <= 9:
        output = all_digit(num)
    else:
        iteration = round(digit_len/2)
        output = all_two_digit(num[:2])  # First to digit
        for i in range(1, iteration):
            output = output + separator + all_two_digit(num[i * 2:(i + 1) * 2])  # Next two digit pair
        remaining_digits = num[iteration * 2:]
        if not all_two_digit(remaining_digits) == '':
            output = output + separator + all_two_digit(remaining_digits)  # Last one_digit/two_digits

    output = output.strip()

    # Language Specific Exception will come here
    output = output.replace('બેસો', 'બસ્સો')
    output = output.replace('छःसौ', 'छसौ')

    return output
