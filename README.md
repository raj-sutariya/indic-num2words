# indic-num2words - Convert Numbers to Words for Indian Languages

The `indic-num2words` module converts numerical digits like `36` into words like `छत्तीस` in various Indian languages.

## Installation

To install the latest stable release from PyPI:

```sh
pip install indic-num2words
```

## Usage

The module provides a single function for converting numbers to words:

```python
from num_to_words import num_to_word

# Examples:
print(num_to_word(36, lang='hi'))  # Output: छत्तीस
print(num_to_word('४५', lang='hi'))  # Output: पैंतालीस
print(num_to_word("35,43,57,730", lang='hi'))  # Output: पैंतीसकरोड़ तैंतालीसलाख सत्तावनहज़ार सातसौ तीस
print(num_to_word(795, lang='kn', separator='-'))  # Output: ಏಳುನೂರ-ತೊಂಬತ್ತೈದು
print(num_to_word(545589, lang='en', separator=', ', combiner='-'))  # Output: five-lakh, forty-five-thousand, five-hundred, eighty-nine
```

### Function Parameters

- `num` (int, str): The number to be converted. This can be an integer, string of digits, or a formatted number string.
- `lang` (str): The language code for the desired output language. Supported languages are listed below.
- `separator` (str, optional): A string to use as a separator between number groups. Default is a space.
- `combiner` (str, optional): A string to combine words in complex numbers. Default is a space.

## Supported Languages

The module currently supports conversion to the following languages:

- `en` (English-India)
- `hi` (Hindi)
- `gu` (Gujarati)
- `mr` (Marathi)
- `bn` (Bengali)
- `te` (Telugu)
- `ta` (Tamil)
- `kn` (Kannada)
- `or` (Oriya)
- `pa` (Punjabi)
- `ml` (Malayalam)

## Use Cases

1. **Speech Recognition Pre-processing:** Convert numbers to words to improve speech recognition accuracy.
2. **Language Modeling Data Pre-processing:** Prepare text data for training language models by converting numerical data to words.

## What's Next

We are planning to add support for the following languages:

- Urdu
- Assamese

If you'd like to contribute or request support for another language, check `utils/constants.py` to see how you can add support. It's designed to be straightforward.

## Contributing

We welcome contributions! If you'd like to help out, feel free to submit pull requests or raise issues on our GitHub repository.

---

Feel free to reach out if you have any questions or need further assistance. Happy coding!
