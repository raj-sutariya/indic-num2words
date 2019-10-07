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


def language_specific_exception(words, lang, combiner):
    """
    Language Specific Exception will come here
    """
    def occurs_at_end(piece):
        return words[-len(piece):] == piece

    if lang == 'mr':
        words = words.replace("एक" + combiner + "शे", "शंभर")
    elif lang == 'gu':
        words = words.replace('બે' + combiner + 'સો', 'બસ્સો')
    elif lang == 'te':
        exception_dict = {
            "1": "ఒక",
            "100": "వంద",
            "100+": "వందలు",
            "1000": "వెయ్యి",
            "1000+": "వేలు",
            "100000": "లక్ష",
            "100000+": "లక్షలు",
            "10000000": "కోటి",
            "10000000+": "కోట్లు",
        }

        test_case = ['100', '1000', '100000', '10000000']
        for test in test_case:
            test_word = num_dict['te'][test]
            match = num_dict['te']['1'] + combiner + test_word
            # for numbers like : 100, 1000, 100000
            if words == match:
                return exception_dict[test]
            # for numbers like : 200, 4000, 800000
            elif occurs_at_end(test_word):
                words = words.replace(test_word, exception_dict[test + '+'])
            # for numbers like : 105, 1076, 123993
            elif not occurs_at_end(match):
                replacement = exception_dict['1'] + combiner + exception_dict[test]
                words = words.replace(match, replacement)

        # Exception case for 101...199
        special_case = "ఒక" + combiner + "వంద"
        words = words.replace(special_case, "నూట")
    elif lang == 'kn':
        # special case for 100
        if words == ('ಒಂದು' + combiner + 'ನೂರ'):
            return 'ನೂರು'
        exception_dict = {
            'ನೂರ': 'ನೂರು',
            'ಸಾವಿರದ': 'ಸಾವಿರ',
            'ಲಕ್ಷದ': 'ಲಕ್ಷ',
            'ಕೋಟಿಯ': 'ಕೋಟಿ'
        }
        for expt in exception_dict:
            if occurs_at_end(expt):
                words = words.replace(expt, exception_dict[expt])
    return words


def num_to_word(num, lang, separator=', ', combiner=' '):
    """
    Main Method
    :param num: Number digits from any indian language
    :param lang: Language Code from supported Language
    :param separator: Separator character i.e. separator = '-' --> 'two hundred-sixty'
    :param combiner: combine number with position i.e. combiner = '-' --> 'two-hundred sixty'
    :return: UTF-8 String of numbers in words
    """
    lang = lang.lower()
    num = str(num)

    # Load dictionary according to language code
    assert lang in supported_lang, 'Language not supported'
    num_dic = num_dict[lang]

    # dash default combiner for english-india
    if lang == 'en':
        combiner = '-'

    # Remove punctuations from numbers
    num = str(num).replace(',', '').replace(' ', '')

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
        if len(digits_2) <= 1:  # Provided only one/zero digit
            return num_dic.get(digits_2, '')
        elif digits_2 == '00':  # Two Zero provided
            return num_dic['0'] + separator + num_dic['0']
        elif digits_2[0] == '0':  # First digit is zero
            return num_dic['0'] + separator + num_dic[digits_2[1]]
        else:  # Both digit provided
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
        digit_len = len(digits)
        if digit_len > 3:
            num_of_digits_to_process = (digit_len % 2) + 1
            process_digits = digits[:num_of_digits_to_process]
            base = str(10**(int(digit_len / 2) * 2 - 1))
            remain_digits = digits[num_of_digits_to_process:]
            return num_dic[process_digits] + combiner + num_dic[base] + separator + all_digit(remain_digits)
        elif len(digits) == 3:
            return num_dic[digits[:1]] + combiner + num_dic['100'] + separator + two_digit(digits[1:])
        else:
            return two_digit(digits)

    num = num.lstrip('0')
    full_digit_len = len(num)

    if full_digit_len == 0:
        output = num_dic['0']
    elif full_digit_len <= 9:
        output = all_digit(num)
    else:
        iteration = round(full_digit_len / 2)
        output = all_two_digit(num[:2])  # First to digit
        for i in range(1, iteration):
            output = output + separator + all_two_digit(num[i * 2:(i + 1) * 2])  # Next two digit pairs
        remaining_digits = num[iteration * 2:]
        if not all_two_digit(remaining_digits) == '':
            output = output + separator + all_two_digit(remaining_digits)  # remaining Last one/two digits

    output = output.strip(separator)

    output = language_specific_exception(output, lang, combiner)

    return output
