"""
textstats — a tiny text-analysis library.

NOTE: This module ships with 5 intentional bugs so the demo has something to
fix. The accompanying test suite (test_textstats.py) defines the correct
behavior. The whole point of the demo is to make the tests pass:

  * WITHOUT loops: you fix them one prompt at a time (see README).
  * WITH loops:    you run ./fix_loop.ps1 and the loop drives Amp until green.
"""


def word_count(text: str) -> int:
    """Number of whitespace-separated words."""
    # BUG 1: returns character count instead of word count.
    return len(text)


def char_count(text: str, include_spaces: bool = True) -> int:
    """Number of characters, optionally excluding whitespace."""
    if include_spaces:
        return len(text)
    # BUG 2: removes only literal spaces, not tabs/newlines.
    return len(text.replace(" ", ""))


def average_word_length(text: str) -> float:
    """Mean length of words. Returns 0.0 for empty input."""
    words = text.split()
    # BUG 3: ZeroDivisionError on empty text instead of returning 0.0.
    return sum(len(w) for w in words) / len(words)


def most_common_word(text: str) -> str:
    """Most frequent word, case-insensitive. Ties broken by first appearance."""
    words = text.split()
    counts: dict[str, int] = {}
    for w in words:
        # BUG 4: not lowercased, so 'The' and 'the' count separately.
        counts[w] = counts.get(w, 0) + 1
    return max(counts, key=counts.get) if counts else ""


def is_palindrome(text: str) -> bool:
    """True if text reads the same forwards/backwards, ignoring case/spaces."""
    # BUG 5: does not ignore case or spaces.
    return text == text[::-1]
