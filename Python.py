Python Review
Hard
Simple SAT
import itertools
import re

def SimpleSAT(strParam):
  eval_str = ""
  letters = []
  for x in strParam:
    if x in "()":
      eval_str += x
    elif x == "&":
      eval_str += " & "
    elif x == "|":
      eval_str += " or "
    elif x == "~":
      eval_str += " not "
    elif x.isalpha():
      eval_str += x
      if x not in letters:
        letters.append(x)
  option_len = ""
  for l in letters:
    option_len += "0"
  tf_options = itertools.product("01", repeat=len(option_len))
  for opt in tf_options:
    if test_eval(eval_str, letters, opt) == True:
      return "yes"
  
  return "no"


def test_eval(eval_str, letters, opt):
  new_eval_str = ""
  for ind, char in enumerate(eval_str):
    if char in letters:
      var_index = letters.index(char)
      if opt[var_index] == "0":
        new_eval_str += " True "
      elif opt[var_index] == "1":
        new_eval_str += " False "
    elif char == "&":
      new_eval_str += "and"
    else:
      new_eval_str += char
  if eval(new_eval_str) == True:
    return True
  return False

# keep this function call here 
print(SimpleSAT(input()))

Hard
Calculator
def Calculator(strParam):
  new_str = ""
  for ind, x in enumerate(strParam):
    if ind > 0:
      if x == "(" and strParam[ind - 1] not in ["+", "-", "/", "*"]:
        new_str += "*"
      if x.isdigit() and strParam[ind - 1] == ")":
        new_str += "*"
    new_str += x
  answer = eval(new_str)
  # code goes here
  return int(answer)

# keep this function call here 
print(Calculator(input()))

