#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """Prints My name is <first name> <last name>
    Args:
        first_name (str): first name
        last_name (str): last name
        
    Raises:
        TypeError: If first_name or last_name is not a string
        
    Returns:
        None
    prints My name is <first name> <last name>
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    else:
        print(f"My name is {first_name} {last_name}")
