import math

class Node:
  def __init__(self, number, type="hidden"):
    self.num = int(number)
    self.type = type
    
    self.in_connections = [] 
    self.out_connections = []

    self.cache = None

  def __repr__(self):
    #Not s just calls __str__ instead of __format__ makes sure to print true not 1
    return((f"{self.type : <6} Node {self.num:02}").capitalize())

  def __eq__(self, other):
    
    #not same type
    if not (type(other) == Node):
      return False

    return(self.__dict__ == other.__dict__)
    
  def append_in(self, node):
    self.in_connections.append(node)
  def append_out(self, node):
    self.out_connections.append(node)
  
  def is_neighbor(self, node):
    for i in self.in_connections + self.out_connections:
      if i == node:
        return True

    return False
    
  def calc(self, x):
    def sigmoid(x):
      return 1/(1+(math.exp(-x)))
    
    return sigmoid(x)
  def extra_detail(self):
    txt = f"im:- {self.num}\n"
    in_conn  = f"Connections that point towards me:- {[x.num for x in self.in_connections]}\n"
    out_conn = f"Connections that point away from me:- {[x.num for x in self.out_connections]}\n"
    if not (self.cache is None): 
      cache = f"Whats cached:- {self.cache}"
      return txt+in_conn+out_conn+cache
    return txt+in_conn+out_conn

class Node_genome(list):
  def __init__(self, input, output):
    list.__init__([])
    #input
    for i in range(input):
      node = Node(len(self), "input")
      self.append(node)

    #output
    for i in range(output):
      node = Node(len(self), "output")
      self.append(node)

  def __repr__(self):
    out = ""
    for i in self:
      out = out+(i.__repr__()+"\n")

    out = out[:-1]
    return out

  def append(self, node):
    if type(node) == Node:
      list.append(self, node)
      
    else:
      raise NotImplementedError(f"Wrong type '{node}'")

  def get_node(self, num):
    for i in self:
      if i.num == num:
        return i
  def __getitem__(self, item):
    if type(item) == int:
      return list.__getitem__(self, item)

    if type(item) == Node:
      for i, node in enumerate(self):
        if node == item:
          return i
          
    else:
      raise TypeError("Wrong type "+item)
      
      
  def reset(self):
    for i in range(len(self)):
      self[i].cache = None
  def extra_details(self):
    for i in self:
      print(i.extra_detail())
      print()