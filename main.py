from NEAT.node import Node, Node_genome
from NEAT.connection import Connection, Connection_genome
from NEAT.creature import Creature
import math



if __name__ == "__main__":
  xor = Creature(3,1)

  xor.nodes.append(Node(4)) #top
  xor.nodes.append(Node(5)) #bottom

  xor.connections.append(Connection(xor.nodes.get_node(0), (xor.nodes.get_node(4)), -10, 1))
  xor.connections.append(Connection(xor.nodes.get_node(1), (xor.nodes.get_node(4)), 20, 2))
  xor.connections.append(Connection(xor.nodes.get_node(2), (xor.nodes.get_node(4)), 20, 3))
  
  xor.connections.append(Connection(xor.nodes.get_node(0), (xor.nodes.get_node(5)), 30, 4))
  xor.connections.append(Connection(xor.nodes.get_node(1), (xor.nodes.get_node(5)), -20, 5))
  xor.connections.append(Connection(xor.nodes.get_node(2), (xor.nodes.get_node(5)), -20, 6))

  xor.connections.append(Connection(xor.nodes.get_node(0), (xor.nodes.get_node(3)), -30, 7))
  xor.connections.append(Connection(xor.nodes.get_node(4), (xor.nodes.get_node(3)), 20, 8))
  xor.connections.append(Connection(xor.nodes.get_node(5), (xor.nodes.get_node(3)), 20, 9))

  print(xor)
  print()
  
  input = [[1,0,0],
           [1,1,0],
           [1,0,1],
           [1,1,1]]
  
  expected_out = [[0], [1], [1], [0]]








  
  for i, item in enumerate(input):
    output = xor.calc(item)
    print(f"input:-  {item}")
    print(f"Output:- {[round(x) for x in output]}")
    print(f"expected:- {expected_out[i]}")
    print(f"Working?:- {expected_out[i] == [round(x) for x in output]}")
    print()

    
  

