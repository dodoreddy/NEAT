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
          weight = self.connections[(i, node)].weight
          x = x+ (calc_node(i) * weight)

          
        x = node.calc(x)
        node.cache = x
        return x

    
    out = []
    node = self.nodes[i]
    while node.type == "output":

      node.cache = calc_node(node)
      out.append(node.cache)

      i += 1
      node = self.nodes[i]

    self.nodes.reset()
    return out

