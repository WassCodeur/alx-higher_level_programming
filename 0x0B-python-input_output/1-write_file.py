#!/usr/bin/python3
def write_file(filename="", text=""):
    """This function write a string to a text file and return the number of
        characters written 
        If the file does not exist, it will be created. 
        If the file already exists, its contents will be overwritten.
    args:
        filename: name of the file
        text: text to write
    return: number of characters written
    """
    with open(filename, mode="w", encoding='utf-8') as myfile:
        myfile.write(text)
    return len(text)
