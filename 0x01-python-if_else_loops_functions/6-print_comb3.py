#!/usr/bin/python3
for i in range (0, 10):
  for k in range (0, 10):
    if i < k:
      if i < 8:
        print("{}{}, ".format(i,k), end="")
      else:
          print("{}{}".format(i,k))
