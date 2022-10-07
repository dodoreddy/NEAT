import math
import networkx as nx

def calculate_network(genome, input, input_between_0to1 = False):
  
  if not input_between_0to1:
    for i in range(0, len(input)):
      input[i] = sigmoid(input[i])
  
  graph = genome.g
  
  nx.set_node_attributes(graph, None, "out")

  for i, item in enumerate(input):
      list(graph.nodes(data=True))[i][1]["out"] = item 

  if genome.bias:
    list(graph.nodes(data=True))[i+1][1]["out"] = 1 
  
  for i in graph.nodes(data=True):
    print(i[1]["out"])


def calculate_node(inputs, weights):
  total = 0
  for i,item in enumerate(inputs):
    total += item*weights[i]
  return sigmoid(total)


#makes x a number between 0 to 1
def sigmoid(x):
  return 1/(1+math.exp(-x))