indic-num2words - Convert numbers to words for indian languages
===============================================================

The code has been converted into PyPI module for the easy installation and update.

``indic-num2words`` moduls converts numbers like ``36`` to words like ``छत्तीस``.

Use Cases:-
------------
1. Speech recognition pre-processing
2. Language modeling data pre-processing


Installation :-
------------
To install latest PyPI stable release

.. code::

    pip install indic-num2words


Usage :-
------------

In code there's only one function to use

.. code:: python

    >>> from num_to_words import num_to_word
    >>> num_to_word(36, lang='hi')
    छत्तीस
    >>> num_to_word('४५', lang='hi')
    पैंतालीस
    >>> num_to_word("35,43,57,730", lang='hi')
    पैंतीसकरोड़ तैंतालीसलाख सत्तावनहज़ार सातसौ तीस
    >>> num_to_word(795, lang='kn', separator='-')
    ಏಳುನೂರ-ತೊಂಬತ್ತೈದು
    >>> num_to_word(545589, lang='en', separator=', ', combiner='-')
    five-lakh, forty-five-thousand, five-hundred, eighty-nine



The module currently supports the following languages:

* ``en`` (English-India)
* ``hi`` (Hindi)
* ``gu`` (Gujarati)
* ``mr`` (Marathi)
* ``bn`` (Bengali)
* ``te`` (Telugu)
* ``ta`` (Tamil)
* ``kn`` (Kannada)
* ``or`` (Oriya)
* ``pa`` (Punjabi)



What's next
-----------

Add Support for following Languages

* Malayalam
* Urdu
* Assamese

check utils/constants.py to add support for any indian languages.

``Shout out if you want to help :)``
