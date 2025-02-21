import pytest
from app.api.utils import reverse_string


def test_reverse_string_basic():
    """Test that a basic string is reversed correctly."""
    assert reverse_string("hello") == "olleh"


def test_reverse_string_empty():
    """Test that an empty string returns an empty string."""
    assert reverse_string("") == ""


def test_reverse_string_with_spaces():
    """Test that a string with spaces is reversed correctly."""
    assert reverse_string("Hello World") == "dlroW olleH"


def test_reverse_string_single_char():
    """Test that a single character returns the same character."""
    assert reverse_string("a") == "a"


def test_reverse_string_unicode():
    """Test that a string with Unicode characters is reversed correctly."""
    assert reverse_string("😊abc") == "cba😊"
