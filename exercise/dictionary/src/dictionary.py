"""
Provide a Dictionary class implementation

The Dictionary class provide necessary tools to interact with different classes


Classes:
    Room: Class to manage dictionaries
"""

class Dictionary:
    """
    A class to provide necessary tools to work with dictionaries.

    This class initializes with a new dictionary and with different methods to interact with dictionary
    """
    def __init__(self) -> None:
        """
        Initialize an empty dictionary.
        """
        self._entries: dict[str, str] = {}

    def newentry(self, key: str, value: str) -> None:
        """
        Create a new entry of dictionary.

        :param key: recieves the key of dictionary.
        :type key: str.
        :param value: recieves the value of the new dictionary entry.
        :type value: str.
        :raises TypeError: If 'key' is not of type str.
        :raises TypeError: If 'value' is not of type str.
        """
        if not isinstance(key, str):
            raise TypeError("word must be a string")
        if not isinstance(value, str):
            raise TypeError("definition must be a string")
        self._entries[key] = value

    def all_keys(self) -> tuple[str, ...]:
        """
        return all keys for dictionary.

        :return: A tuple containing all keys.
        :rtype: tuple[str]
        """
        return tuple(self._entries.keys())
    
    def all_values(self) -> tuple[str, ...]:
        """
        return all values for dictionary.

        :return: A tuple containing all values.
        :rtype: tuple[str]
        """
        return tuple(self._entries.values())

    def look(self, word: str) -> str:
        """
        look for an specific entry.

        :param word: key to check definition.
        :type word: str

        :return: Definition for a given entry.
        :rtype: str
        """
        return self._entries.get(word, f"Can't find entry for {word}")