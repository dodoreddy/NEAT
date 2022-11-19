from NEAT.connection import Connection, Connection_genome
from NEAT.node import Node, Node_genome
import math
class Creature():
  def __init__(self, input, output):
    self.nodes = Node_genome(input, output)
    self.connections = Connection_genome()

  def __repr__(self):
    return self.nodes.__repr__()+"\n\n"+self.connections.__repr__()
  def calc(self, input):
    i=0
    node = self.nodes[i]
    while node.type == "input":
      node.cache = input[i]
      i += 1
      node = self.nodes[i]
    
    
    def calc_node(node):
      if not (node.cache is None):
        return node.cache

      else:
        x = 0
        for i in node.in_connections:
          connection = self.connections[(i, node)]
          if connection.enabled:
            x = x+ (calc_node(i) * connection.weight)

          
        x = node.calc(x)
        node.cache = x
        return x

    
    
    out = []
    node = self.nodes[i]
    while node.type == "output":

      node.cache = calc_node(node)
      out.append(node.cache)

      i += 1
      if i >= len(self.nodes):
        break
      node = self.nodes[i]

    self.nodes.reset()
    return out


  def new(self, connection):

    if not (connection.start in self.nodes):
      raise Exception("Input neuron must be an existing neuron")
    if not (connection.end in self.nodes): 
      raise Exception("Output neuron must be an existing neuron")
    
    if connection.start.type == "output":
      raise Exception("Input Neuron cant be an output neuron")
    if connection.end.type == "input":
      raise Exception("Output Neuron cant be an Input neuron")

    if connection in self.connections:
      raise Exception("This connection already exists")
    
    self.connections.append(connection)

    self.nodes.reset()


    if (self.forms_loop(connection.start)):
      raise Exception("This connection forms a loop")

    self.nodes.reset()


  def forms_loop(self, node):
    if node.cache == True:
      return True
    node.cache = True
    
    for i in node.out_connections:
      x = self.forms_loop(i)
      if x == True:
        return True
    return False
    
    
    