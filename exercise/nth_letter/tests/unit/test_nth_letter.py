import pytest

from src.nth_letter import nth_letter


def test_nth_letter_basic():
    """Test basic case from the exercise description."""
    assert nth_letter(["yoda", "best", "has"]) == "yes"


def test_nth_letter_empty_list():
    """Test that empty list returns empty string."""
    assert nth_letter([]) == ""


def test_nth_letter_single_word():
    """Test that single word returns its first letter."""
    assert nth_letter(["hello"]) == "h"


def test_nth_letter_word_too_short():
    """Test that words shorter than their position are ignored."""
    assert nth_letter(["yoda", "b", "has"]) == "ys"


def test_nth_letter_empty_string_ignored():
    """Test that empty strings are ignored."""
    assert nth_letter(["yoda", "", "has"]) == "ys"


def test_nth_letter_invalid_element_type():
    """Test that TypeError is raised when an element is not a string."""
    with pytest.raises(TypeError):
        nth_letter(["yoda", 123, "has"])


def test_nth_letter_invalid_input_type():
    """Test that TypeError is raised when input is not a list."""
    with pytest.raises(TypeError):
        nth_letter("not a list")