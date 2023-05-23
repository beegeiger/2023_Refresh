Python Review
Hard
Simple SAT
import itertools
import re


AB check
def ABCheck(strParam):
  for ind, x in enumerate(strParam[:-4]):
    if x == "a":
      if strParam[ind + 4] == "b":
        return "true"
    elif x == "b":
      if strParam[ind + 4] == "s":
        return "true"
  return "false"

# keep this function call here 
print(ABCheck(input()))

Credit Card Mask
# return masked string
def maskify(cc):
    out = ""
    for ind, x in enumerate(cc):
        if ind < len(cc) - 4:
            out += "#"
        else:
            out += x
    return out


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



Preorder Traversal Try 1 - Assumed Binary Heap Implemented without blank spaces
class Node:
  def __init__(self, name, parent, left=None, right=None):
    self.name = name
    self.left = left
    self.right = right
    self.parent = parent

  def add_right(self, right):
    self.right = right

  def add_left(self, left):
    self.left = left


def create_nodes(strArr):
  line_starts = [1, 3, 7, 15]
  line_ind_counter = 0
  nodes = {}
  current_line_start_ind = 0
  for ind, nod in enumerate(strArr):
    if nod != "#":
      parent = None
      child_type = None
      if ind > 0:
        node_position = ind + 1
        if node_position % 2 == 0:
          parent_position = (node_position / 2) - 1
          child_type = "Left"
        else:
          parent_position = ((node_position -1) / 2) - 1
          child_type = "Right"
        parent = strArr[int(parent_position)]
      new_node = Node(nod, parent)
      nodes[nod] = new_node
      if ind > 0:
        parent_node = nodes[parent]
        if child_type == "Left":
          parent_node.add_left(nod)
        elif child_type == "Right":
          parent_node.add_right(nod)
        nodes[parent] = parent_node
  return nodes

def check_node(current_node_name, nodes):
  current_node = nodes[current_node_name]
  node_order = current_node_name + " "
  if current_node.left == None and current_node.right == None:
    return current_node_name + " "
  else:
    if current_node.left:
      left_values = check_node(current_node.left, nodes)
      node_order += left_values
    if current_node.right:
      right_values = check_node(current_node.right, nodes)
      node_order += right_values
    return node_order

def PreorderTraversal(strArr):
  nodes = create_nodes(strArr)
  for n in nodes:
    nod = nodes[n]
  first_node_name = strArr[0]
  output = check_node(first_node_name, nodes)
  return output[:-1]


# keep this function call here 
print(PreorderTraversal(input()))

Preorder Traversal Try 2 - Prvious Cases fixed but new String still has wrong indexes
class Node:
  def __init__(self, name, parent, left=None, right=None):
    self.name = name
    self.left = left
    self.right = right
    self.parent = parent

  def add_right(self, right):
    self.right = right

  def add_left(self, left):
    self.left = left


def create_nodes(strArr):
  line_starts = [1, 3, 7, 15]
  line_ind_counter = 0
  nodes = {}
  current_line_start_ind = 0
  input_copy = list(strArr)
  missing_indexes = []
  for ind, pre_nod in enumerate(strArr):
    if pre_nod == "#":
      if len(strArr) > (2*ind) + 2:
        input_copy= input_copy[:(2 * ind) + 1] + ["#", "#"] + input_copy[(2 * ind) + 1:]
  for ind, nod in enumerate(input_copy):
    if nod != "#":
      parent = None
      child_type = None
      if ind > 0:
        node_position = ind + 1
        if node_position % 2 == 0:
          parent_position = (node_position / 2) - 1
          child_type = "Left"
        else:
          parent_position = ((node_position -1) / 2) - 1
          child_type = "Right"
        parent = strArr[int(parent_position)]
      new_node = Node(nod, parent)
      nodes[nod] = new_node
      if ind > 0:
        parent_node = nodes[parent]
        if child_type == "Left":
          parent_node.add_left(nod)
        elif child_type == "Right":
          parent_node.add_right(nod)
        nodes[parent] = parent_node
  return nodes

def check_node(current_node_name, nodes):
  current_node = nodes[current_node_name]
  node_order = current_node_name + " "
  if current_node.left == None and current_node.right == None:
    return current_node_name + " "
  else:
    if current_node.left:
      left_values = check_node(current_node.left, nodes)
      node_order += left_values
    if current_node.right:
      right_values = check_node(current_node.right, nodes)
      node_order += right_values
    return node_order

def PreorderTraversal(strArr):
  nodes = create_nodes(strArr)
  for n in nodes:
    nod = nodes[n]
  first_node_name = strArr[0]
  output = check_node(first_node_name, nodes)
  return output[:-1]


# keep this function call here 
print(PreorderTraversal(input()))


Prime Mover
def isPrime(num):
  for i in range(2,num):
    if num%i == 0:
      return False
  return True

def PrimeMover(num):
  counter = 0
  current = 2
  while counter < num:
    if isPrime(current) == True:
      counter += 1
    current += 1
  return current - 1

# keep this function call here 
print(PrimeMover(input()))


Number Encoding
def NumberEncoding(strParam):
  letters = "abcdefghijklmnopqrstuvwxyz"
  output = ""
  for n in strParam:
    if n.isalpha():
      output += str(letters.index(n) + 1)
    else:
      output += n
  return output

# keep this function call here 
print(NumberEncoding(input()))

Medium
Plus Minus
import itertools

def PlusMinus(int_num):
  num = str(int_num)
  possible_options = itertools.product("-+", repeat=(len(num) - 1))
  working_options = []
  for opt in possible_options:
    current_eq = ""
    for n in range(len(num) - 1):
      current_eq += num[n]
      current_eq += opt[n]
    current_eq += num[-1]
    if eval (current_eq) == 0:
      formated_option = ""
      for item in opt:
        formated_option += item
      working_options.append(formated_option)
  if len(working_options) == 0:
    return "not possible"
  elif len(working_options) == 1:
    return working_options[0]
  else:
    tracking = []
    for wo in working_options:
      tracking.append(wo.count("-"))
    highest_val = max(tracking)
    highest_ind = tracking.index(highest_val)
    return working_options[highest_ind]

# keep this function call here 
print(PlusMinus(input()))

Medium
Max SubArray
def MaxSubarray(arr):
  highest = -999999999
  for ind in range(len(arr)):
    if arr[ind] > highest:
      highest = arr[ind]
    tracker = arr[ind]
    for ind2 in range(len(arr) - ind + 1):
      tracker = sum(arr[ind:ind2 + 1])
      if tracker > highest and len(arr[ind:ind2 + 1]) > 0:
        highest = tracker
  return highest

# keep this function call here 
print(MaxSubarray(input()))

Medium
Run Length (RECURSIVE)
def RunLength(strParam):
  first_value = strParam[0]
  counter = 0
  output = ""
  final_index = 0
  for ind, n in enumerate(strParam):
    final_index = ind
    if n == first_value:
      counter += 1
      if ind == len(strParam) - 1:
        return str(counter) + first_value
    else:
      output += str(counter) + first_value
      break
  return output + RunLength(strParam[final_index:])

# keep this function call here 
print(RunLength(input()))


Palindrome
def PalindromicSubstring(strParam):
  longest = ""
  for ind, x in enumerate(strParam):
    tracker = x
    for ind2, y in enumerate(strParam[ind + 1:]):
      tracker += y
      following = strParam[ind + 2]
      reverse_tracker = tracker[::-1]
      if following[:len(reverse_tracker)] == reverse_tracker:
        if len(tracker + followingfollowing[:len(tracker)]) > len(longest):
          longest = tracker + followingfollowing[:len(tracker)]
      elif following[:len(reverse_tracker)-1] == reverse_tracker[1:]:
        if len(tracker + following[:len(reverse_tracker)-1]) > len(longest):
          

  return strParam

# keep this function call here 
print(PalindromicSubstring(input()))

def PalindromicSubstring(strParam):
  longest = ""
  for ind, x in enumerate(strParam):
    tracker = x
    for ind2, y in enumerate(strParam[ind + 1:]):
      tracker += y
      if len(tracker) <= len(strParam) - (ind + ind2):
        following = strParam[ind + 2:]
        reverse_tracker = tracker[::-1]
        if following[:len(reverse_tracker)] == reverse_tracker:
          if len(tracker + following[:len(tracker)]) > len(longest):
            longest = tracker + following[:len(tracker)]
        elif following[:len(reverse_tracker)-1] == reverse_tracker[1:]:
          if len(tracker + following[:len(reverse_tracker)-1]) > len(longest):
            longest = tracker + following[:len(reverse_tracker)-1]
  if longest == "":
    return "none"
  return longest

# keep this function call here 
print(PalindromicSubstring(input()))


Sum Of Prime Factors
def sum_of_prime_factors(n):
  pfs = []
  for y in range(2,n-1):
    if n % y == 0:
      if is_prime(y) == True:
        pfs.append(y)
  if n < 0:
    for y in range(-(n - 1), -2):
      if n % y == 0:
        if is_prime(y) == True:
          pfs.append(y)
  if pfs == []:
    return n
  return sum(pfs)


def is_prime(x):
  if x > 1:
    for i in range(2, int(x/2)+1):
      if x % i == 0:
        return False
  return True

print(sum_of_prime_factors(91))

Edabit Stutter Word
def stutter(word):
  out = ""
  out += word[:2] + "... " + word[:2] + "... " + word + "?"
  return out


Codecademy Find the Xth Number
def getX(x, nums):
  if len(nums) == 0 or x > len(nums):
    return 0
  nums.sort()
  return nums[x - 1]

getX(2, [5, 10, -3, -3, 7, 9])

HackerRank Leap Year
def is_leap(year):
    simplified = False
    while simplified == False:
        year -= 400
        if year < 400:
            simplified = True
    if year % 4 == 0 and year not in [100,200,300]:
        return True
    return False


year = int(input())

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a%b)
    print(a/b)

def StringExpression(strParam):
  written = ["zero","one","two", "three", "four", "five", "six", "seven", "eight", "nine"]
  out_exp = ""
  while len(strParam) > 0:
    if strParam[:3] in written:
      out_exp += str(written.index(strParam[:3]))
      strParam = strParam[3:]
    elif strParam[:4] == "plus":
      out_exp += "+"
      strParam = strParam[4:]
    elif strParam[:4] in written:
      out_exp += str(written.index(strParam[:4]))
      strParam = strParam[4:]
    elif strParam[:5] == "minus":
      out_exp += "-"
      strParam = strParam[5:]
    elif strParam[:5] in written:
      out_exp += str(written.index(strParam[:5]))
      strParam = strParam[5:]
  val = eval(out_exp)
  out = ""
  if val < 0:
    out+="negative"
    val = val * (-1)
  for x in str(val):
    out += written[int(x)]

  return out

# keep this function call here 
print(StringExpression(input()))

Rectange Area
def RectangleArea(strArr):
  x = 0
  y = 0
  for ind, pair in enumerate(strArr):
    if ind < 3:
      for ind2, pair2 in enumerate(strArr[ind + 1:]):
        xdiff = int(pair[1]) - int(pair2[1])
        if xdiff < 0:
          xdiff = xdiff*(-1)
        if xdiff > x:
          x = xdiff
        ydiff = int(pair[3]) - int(pair2[3])
        if ydiff < 0:
          ydiff = ydiff*(-1)
        if ydiff > y:
          y = ydiff
  return x*y

# keep this function call here 
print(RectangleArea(input()))

Longest Word
def LongestWord(sen):
  sim = ""
  for x in sen:
    if x.isalpha() or x.isdigit() or x == " ":
      sim += x
  words = sim.split(" ")
  longest = ""
  for word in words:
    if len(word) > len(longest):
      longest = word
  return longest

# keep this function call here 
print(LongestWord(input()))



RECURSION
def BracketMatcher(strParam):
  checked = False
  if strParam.count("(") == 0 and strParam.count(")") == 0:
    return "1"
  elif strParam.count("(") != strParam.count(")") == 0:
    return "0"
  else:
    removed = remove_bracket(strParam)
    if removed == "False":
      return "0"
    else:
      return BracketMatcher(removed)
  return strParam


def remove_bracket(str_in):
  open_ind = -1
  for ind, x in enumerate(str_in):
    if x == "(":
      open_ind = ind
    elif x == ")":
      if open_ind == -1:
        return "False"
      else:
        out = str_in[:open_ind] + str_in[open_ind + 1:ind]
        if ind != len(str_in) - 1:
          out += str_in[ind + 1:]
        return out
  return "False"


# keep this function call here 
print(BracketMatcher(input()))


SWAP II 
def SwapII(strParam):
  str_split = strParam.split(" ")
  out = ""
  for word in str_split:
    num_yet = False
    non_letter_between = False
    num_ind = -1
    last_num_index = -1
    word_out1 = ""
    word_out2 = ""
    for ind, let in enumerate(word):
      if let.isdigit() and num_yet == False:
        num_ind = ind
        num_yet = True
      elif let.isdigit() and num_yet == True and non_letter_between == False:
        last_num_index = ind
      elif let.isalpha() == False and let.isdigit() == False and num_yet == True and last_num_index > -1:
        non_letter_between = True
      if let.islower():
        word_out1 += let.upper()
      elif let.isupper():
        word_out1 += let.lower()
      else:
        word_out1 += let
    if num_ind > -1 and last_num_index > -1 and non_letter_between == False:
      word_out2 = word_out1[:num_ind] + word_out1[last_num_index] + word_out1[num_ind + 1: last_num_index] + word_out1[num_ind]
      if last_num_index < len(word) - 1:
        word_out2 += word_out1[last_num_index + 1:]
    else:
      word_out2 = word_out1
    out += word_out2 + " "
  # code goes here
  return out[:-1]

# keep this function call here 
print(SwapII(input()))

Medium
Formatted Division
def FormattedDivision(num1,num2):
  prod = round(num1/num2, 4)
  prod_str = str(prod)
  split_prod1 = prod_str.split(".")
  decimals = split_prod1[-1]
  for y in range(4-len(split_prod1[-1])):
    decimals += "0"
  back_prod = ""
  tracker = -5
  prod_str2 = split_prod1[0] + "." + decimals
  for x in prod_str2[::-1]:
    tracker +=1
    if tracker != 3:
      back_prod += x
    else:
      back_prod += x
      back_prod += ","
      tracker = 0
  return back_prod[::-1]

# keep this function call here 
print(FormattedDivision(input()))


Array Addition I
import itertools

def ArrayAdditionI(arr):
  arr_sort = list(arr)
  arr_sort.sort()
  highest = arr_sort[-1]
  options = arr_sort[:-1]
  combs = []
  for m in range(len(arr)):
    for x in itertools.combinations(options, m):
      combs.append(sum(x))
  if highest in combs:
    return "true"
  return "false"

# keep this function call here 
print(ArrayAdditionI(input()))

def ThreeFiveMultiples(num):
  options = []
  for x in [3,5]:
    all_checked = False
    checker = x
    while checker < 100:
      if checker not in options:
        options.append(checker)
      checker += x
  options.sort()
  unders = 0
  for y in options:
    if y < num:
      unders += y
  return unders

# keep this function call here 
print(ThreeFiveMultiples(input()))




def PalindromeSwapper(strParam):
  for ind, n in enumerate(strParam[:-1]):
    opt = ""
    if ind == 0:
      opt = strParam[1] + n + strParam[2:]
    elif ind == len(strParam) - 2:
      opt = strParam[:ind] + strParam[-1] + n
    else:
      opt = strParam[:ind] + strParam[ind + 1] + n + strParam[ind + 2:]
    if check_pal(opt) == True:
      return opt
  return -1

def check_pal(option):
  back = option[::-1]
  if option == back:
    return True
  return False

# keep this function call here 
print(PalindromeSwapper(input()))


def GCF(arrr):
  arr = list(arrr)
  arr.sort()
  first = int(arr[0])
  second = int(arr[1])
  for x in range(int(round(first/2) + 1), 0, -1):
    if first % x == 0 and second % x == 0:
      return x

# keep this function call here 
print(GCF(input()))