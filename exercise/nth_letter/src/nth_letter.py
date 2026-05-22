"""
Provide an nth_letter function implementation

This module contains a function to construct words by concatenating letters
based on their position within a list.
"""

def nth_letter(words: list[str]) -> str:
    """
    Construct a new word by concatenating the nth letter from each word.

    The nth letter corresponds to the position (index) of the word in the list.
    If a word is too short to have a letter at that position, it is ignored.

    :param words: A list of strings to process.
    :type words: list[str]

    :return: A string formed by the concatenated letters.
    :rtype: str

    :raises TypeError: If 'words' is not of type list.
    :raises TypeError: If any element in the list is not of type str.
    """
    if not isinstance(words, list):
        raise TypeError("input must be a list")

    result = []

    for n, word in enumerate(words):
        if not isinstance(word, str):
            raise TypeError("all elements in the list must be strings")

        if len(word) > n:
            result.append(word[n])

    return "".join(result)