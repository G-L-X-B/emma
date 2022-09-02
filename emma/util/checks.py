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
