from .utils import NUM_DICT


def language_specific_exception(words, lang, combiner):
    """
    Language Specific Exception will come here
    """

    def occurs_at_end(piece):
        return words[-len(piece):] == piece

    if lang == "mr":
        # only for number : 100
        if words == ("एक" + combiner + "शे"):
            return "शंभर"
    elif lang == "gu":
        words = words.replace("બે" + combiner + "સો", "બસ્સો")
    elif lang == "te":
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

        test_case = ["100", "1000", "100000", "10000000"]
        for test in test_case:
            test_word = NUM_DICT["te"][test]
            match = NUM_DICT["te"]["1"] + combiner + test_word
            # for numbers like : 100, 1000, 100000
            if words == match:
                return exception_dict[test]
            # for numbers like : 200, 4000, 800000
            elif occurs_at_end(test_word):
                words = words.replace(test_word, exception_dict[test + "+"])
            # for numbers like : 105, 1076, 123993
            elif not occurs_at_end(match):
                replacement = exception_dict["1"] + combiner + exception_dict[test]
                words = words.replace(match, replacement)

        # Exception case for 101...199
        special_case = "ఒక" + combiner + "వంద"
        words = words.replace(special_case, "నూట")
    elif lang == "kn":
        # special case for 100
        if words == ("ಒಂದು" + combiner + "ನೂರ"):
            return "ನೂರು"
        exception_dict = {
            "ನೂರ": "ನೂರು",
            "ಸಾವಿರದ": "ಸಾವಿರ",
            "ಲಕ್ಷದ": "ಲಕ್ಷ",
            "ಕೋಟಿಯ": "ಕೋಟಿ",
        }
        for expt in exception_dict:
            if occurs_at_end(expt):
                words = words.replace(expt, exception_dict[expt])
    return words
