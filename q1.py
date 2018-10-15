# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

# modify this function, and create other functions below as you wish
def question01(portfolios):
# modify and then return the variable below
  list_1 = []
  list_2 = []

  for i in portfolios:
      for j in portfolios:
          a = bin(i)
          y = int(i)^int(j)
          list_1.append(bin(y)[2:].zfill(len(a)))
  for i in list_1:
      list_2.append(int(i,2))
  answer = max(list_2)
  return answer
