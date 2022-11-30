#!/usr/bin/python3
def islower(c):
  if ord(c) <= 122 and ord(c) >= 97:
    print('true')
    return (True)
  else:
    print("false {}".format(c))
    return (False)
