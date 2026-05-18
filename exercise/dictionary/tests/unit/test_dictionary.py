import pytest

from src.dictionary import Dictionary


@pytest.fixture
def dictionary():
    """Fixture to create an empty dictionary."""
    return Dictionary()

@pytest.fixture
def key():
    """Fixture to create an key to add to the dictionary."""
    return "Apple"

@pytest.fixture
def value():
    """Fixture to create an value to add to the dictionary."""
    return "Apple"

def test_add_value(dictionary,key ,value):
    """Test to validate adding new values."""
    dictionary.newentry(key, value)
    assert key in dictionary.all_keys()
    assert value in dictionary.all_values()

def test_newentry_invalid_key_type(dictionary, value):
    """Test to evalate invalid key types."""
    with pytest.raises(TypeError):
        dictionary.newentry(123, value)

def test_newentry_invalid_value_type(dictionary, key):
    """Test to evaluate invalid value type."""
    with pytest.raises(TypeError):
        dictionary.newentry(key, 123)

def test_look_existing_entry(dictionary, key, value):
    """Test to check correct implementation of look command"""
    dictionary.newentry(key, value)
    assert dictionary.look(key) == value

def test_look_missing_entry(dictionary):
    """Test to check a correct message with incorrect implementation of entry."""
    assert dictionary.look("Banana") == "Can't find entry for Banana"

def test_look_empty_dictionary(dictionary):
    """Test to check a correct message with incorrect implementation of entry."""
    assert dictionary.look("Apple") == "Can't find entry for Apple"