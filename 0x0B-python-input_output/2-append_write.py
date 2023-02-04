#!/usr/bin/python3
def append_write(filename="", text=""):
    """This function append a string at the end of a text file
    and return the number of characters added
    args:
        filename: name of the file
        text: text to append
    return: number of characters added
    """
    with open(filename, mode='a', encoding='utf-8' ) as myfile:
        myfile.write(text)
    return len(text)
