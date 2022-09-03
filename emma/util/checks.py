def check_word(string: str):
    """Check if input string is a word as a whole.

    If input is not of type `str`, raises `TypeError`.
    If input has correct type, but doesn't quallify as a word, raises
    `ValueError`."""

    if not isinstance(string, str):
        raise TypeError(f'str expected, got {type(string)}')
    if len(string) == 0:
        raise ValueError('String is empty.')
    if len(string.split()) != 1:
        raise ValueError('String contains whitespaces.')

def check_isidentifier(string: str):
    """Check if input is a string containing valid python identifier.

    To pass, input must be of type `str` and must return `True` when called
    `isidentifier` on.

    If input is not of type `str`, raises `TypeError`.
    If input has correct type, but doesn't contain valid python
    identifier, raises `ValueError`."""

    if not isinstance(string, str):
        raise TypeError(f'str expected, got {type(string)}')
    if not string.isidentifier():
        raise ValueError("String is not a valid python identifier.")
