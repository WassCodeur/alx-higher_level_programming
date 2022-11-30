def uppercase(str):
  for string in str:
    if ord(string) >= 97 and ord(string) <= 122:
      string = chr(ord(string)- 32)
    print("{}".format(string), end='')
  print()
