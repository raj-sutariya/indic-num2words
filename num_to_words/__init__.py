from .exception import language_specific_exception
from .utils import SUPPORTED_LANGUAGES, NUM_DICT, DIGITS_LANG_MAPPING


def num_to_word(num, lang, separator=", ", combiner=" "):
    """
    Main Method
    :param num: Number digits from any indian language
    :param lang: Language Code from supported Language
    :param separator: Separator character i.e. separator = ', ' --> 'two hundred, sixty'
    :param combiner: combine number with position i.e. combiner = '-' --> 'two-hundred sixty'
    :return: UTF-8 String of numbers in words
    """
    lang = lang.lower()
    num = str(num)

    # Load dictionary according to language code
    assert lang in SUPPORTED_LANGUAGES, "Language not supported"
    num_dic = NUM_DICT[lang]

    # dash default combiner for english-india
    if (lang == "en") & (combiner == " "):
        combiner = "-"

    # Remove punctuations from numbers
    num = str(num).replace(",", "").replace(" ", "")

    # Replace native language numbers with english digits
    for language in SUPPORTED_LANGUAGES:
        for num_index in range(10):
            num = num.replace(DIGITS_LANG_MAPPING[language][num_index], DIGITS_LANG_MAPPING["en"][num_index])

    # Assert that input contains only integer number
    assert num, "Input string is empty"
    for digit in num:
        assert digit in DIGITS_LANG_MAPPING["en"], "Input string contains invalid characters, give proper input"

    # Process
    # For Number longer than 9 digits
    def all_two_digit(digits_2):
        if len(digits_2) <= 1:  # Provided only one/zero digit
            return num_dic.get(digits_2, "")
        elif digits_2 == "00":  # Two Zero provided
            return num_dic["0"] + separator + num_dic["0"]
        elif digits_2[0] == "0":  # First digit is zero
            return num_dic["0"] + separator + num_dic[digits_2[1]]
        else:  # Both digits provided
            return num_dic[digits_2]

    # For Number less than 9 digits
    def two_digit(digits_2):
        digits_2 = digits_2.lstrip("0")
        if len(digits_2) != 0:
            return num_dic[digits_2]
        else:
            return ""

    def all_digit(digits):
        digits = digits.lstrip("0")
        digit_len = len(digits)
        if digit_len > 3:
            num_of_digits_to_process = (digit_len % 2) + 1
            process_digits = digits[:num_of_digits_to_process]
            base = str(10 ** (int(digit_len / 2) * 2 - 1))
            remain_digits = digits[num_of_digits_to_process:]
            return (
                num_dic[process_digits]
                + combiner
                + num_dic[base]
                + separator
                + all_digit(remain_digits)
            )
        elif len(digits) == 3:
            return (
                num_dic[digits[:1]]
                + combiner
                + num_dic["100"]
                + separator
                + two_digit(digits[1:])
            )
        else:
            return two_digit(digits)

    num = num.lstrip("0")
    full_digit_len = len(num)

    if full_digit_len == 0:
        output = num_dic["0"]
    elif full_digit_len <= 9:
        output = all_digit(num)
    else:
        iteration = round(full_digit_len / 2)
        output = all_two_digit(num[:2])  # First to digit
        for i in range(1, iteration):
            output = (
                output + separator + all_two_digit(num[(i * 2): (i + 1) * 2])
            )  # Next two digit pairs
        remaining_digits = num[(iteration * 2):]
        if all_two_digit(remaining_digits) != "":
            output = (
                output + separator + all_two_digit(remaining_digits)
            )  # remaining Last one/two digits

    output = output.strip(separator)

    output = language_specific_exception(output, lang, combiner)

    return output
