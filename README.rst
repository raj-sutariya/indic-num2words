indic-num2words - Convert numbers to words for indian languages
===============================================================

``indic-num2words`` moduls converts numbers like ``36`` to words like ``छत्तीस``.

Contributions are welcome.

The module currently supports the following languages:

* ``hi`` (Hindi)
* ``gu`` (Gujarati)
* ``mr`` (Marathi)
* ``bn`` (Bengali)
* ``te`` (Telugu)
* ``ta`` (Tamil)
* ``kn`` (Kannada)
* ``or`` (Oriya)
* ``pa`` (Punjabi)

Usage
-----

Just import num_to_word.py to your code

In code there's only one function to use::

    >>> from num_to_word import num_to_word
    >>> num_to_word(36, lang='hi')
    छत्तीस
    >>> num2words('४५', lang='hi')
    पैंतालीस
    >>> num2words(35,43,57,730, lang='hi')
    पैंतीसकरोड़ तैंतालीसलाख सत्तावनहज़ार सातसौ तीस
    >>> num2words(795, lang='kn', separator='-')
    ಏಳುನೂರು-ತೊಂಬತ್ತೈದು


What's next (and being worked upon)
-----------------------------------
``Shout out if you want to help :)``

* Add Malayalam, Urdu and Assamese support
