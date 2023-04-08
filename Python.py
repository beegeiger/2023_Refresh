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

