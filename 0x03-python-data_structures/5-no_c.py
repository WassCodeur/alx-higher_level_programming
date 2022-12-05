#!/usr/bin/python3
def no_c(my_string):
    new_String = ""
    for c in my_string:
        if c == "c" or c == "C":
            c = ""
        new_String += c   
        
    return new_String
    