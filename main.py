from NEAT.node import Node, Node_genome
from NEAT.connection import Connection, Connection_genome
from NEAT.creature import Creature



if __name__ == "__main__":
  a = Creature(2,2)
  a.new(Connection(a.nodes[0], a.nodes[3], 3, 3))
  print (a.calc([1,4]))




    
  

