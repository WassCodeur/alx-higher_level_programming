def uppercase(str):
  for i in range(0,len(str)):
    if str[i] >= 'a' and str[i] <= 'z':
      number = ord(str[i]) - 32
      print("{:c}".format(number), end="")
    elif str[i] >= 'A' and str[i] <= 'Z':
      print("{:c}".format(ord(str[i])), end="")
    if str[i] == ' ':
      print(" ", end="")
    if str[i] <= '9':
      print("{}".format(str[i]),end="")
  print()
