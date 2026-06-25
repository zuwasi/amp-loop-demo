"""Test suite = the loop's 'done' gate. These define correct behavior."""
import textstats as ts


def test_word_count():
    assert ts.word_count("the quick brown fox") == 4
    assert ts.word_count("") == 0
    assert ts.word_count("one") == 1


def test_char_count_with_spaces():
    assert ts.char_count("a b c") == 5


def test_char_count_no_spaces():
    # must strip ALL whitespace, including tabs and newlines
    assert ts.char_count("a b\tc\nd", include_spaces=False) == 4


def test_average_word_length():
    assert ts.average_word_length("aa bb cc") == 2.0
    # empty input must not raise; must return 0.0
    assert ts.average_word_length("") == 0.0


def test_most_common_word_case_insensitive():
    assert ts.most_common_word("The the THE cat") == "the"


def test_is_palindrome():
    assert ts.is_palindrome("racecar") is True
    assert ts.is_palindrome("Race car") is True   # ignore case + spaces
    assert ts.is_palindrome("hello") is False
