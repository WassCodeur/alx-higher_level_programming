#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
        addTuble = ()
        List = list(addTuble)
        list_a = list(tuple_a)
        list_b = list(tuple_b)
        if len(list_a) == len(list_b):
            for i in range(len(list_a)):
                A = list_b[i] + list_a[i]
                List.append(A)
        elif len(list_b) == 0:
            for i in range(len(list_a)):
                A = list_a[i]
                List.append(A)
        elif len(list_a) == 0:
            for i in range(len(list_b)):
                A = list_b[i]
                List.append(A)
        elif len(list_a) > len(list_b):
            for j in range(len(list_b)):
                A = list_b[j] + list_a[j]
                List.append(A)
            for i in range(j+1, len(list_a)):
                A = list_a[i]
                List.append(A)
        elif len(list_b) > len(list_a):
            for j in range(len(list_a)):
                A = list_b[j] + list_a[j]
                List.append(A)
            for i in range(j+1, len(list_b)):
                A = list_b[i]
                List.append(A)
        addTuble = tuple(List)      
        return addTuble
