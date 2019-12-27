import string


def strip_whitespaces(string_with_whitespace):
    return string_with_whitespace.translate(str.maketrans('', '', string.whitespace))
