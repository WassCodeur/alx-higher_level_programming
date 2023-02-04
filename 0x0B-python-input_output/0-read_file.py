#!/usr/bin/python3
def read_file(filename=""):
    """This function read a text file and print it to sdtout
    args:
        filename: name of the file
    return: text file content
    """
    with open(filename, mode="r", encoding='utf-8' ) as myfile:
        content = myfile.read()
    print(content)
