#!/usr/bin/python3
def text_indentation(text):
    """Prints a text with 2 new lines after each of these characters: ., ? and :
    Args:
        text (str): text to print
    Raises:
            TypeError: If text is not a string
    Returns:
        None
    prints:
        a text with 2 new lines after each of these characters: ., ? and :
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in text:
        print(f"{i}", end="")
        if i == "." or i == ":" or i =="?":
            print()
