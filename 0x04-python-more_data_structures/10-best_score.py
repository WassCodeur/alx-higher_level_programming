#!/usr/bin/python3
def best_score(a_dictionary):
    best_score = 0
    best_person_name = ""
    if a_dictionary == None:
        return None
    elif not a_dictionary:
        return None
    else:
        for key in a_dictionary:
            if a_dictionary[key] > best_score:
                best_score = a_dictionary[key]
                best_person_name = key
    return best_person_name