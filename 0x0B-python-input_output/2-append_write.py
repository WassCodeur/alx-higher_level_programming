#!/usr/bin/python3
"""function that write a text file

"""

def append_write(filename="", text=""):
    """This function append a string at the end of a text file

    args:
        filename: name of the file
        text: text to append

    return: number of characters added

    """
    with open(filename, mode='a', encoding='utf-8' ) as myfile:
        myfile.write(text)
    return len(text)
