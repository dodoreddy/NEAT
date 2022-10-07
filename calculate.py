import math
import networkx as nx

def calculate_network(genome, input, is0to1 = True, bottom = 0, top = 1):
  
  if not is0to1:
    for i in range(0, len(input)):
      input[i] = sigmoid(input[i])
  
  else:
    for i in range(0, len(input)):
      input[i] = make_0_to_1(input[i], bottom, top)
  
  graph = genome.g
  
  nx.set_node_attributes(graph, None, "out")

  for i, item in enumerate(input):
      list(graph.nodes(data=True))[i][1]["out"] = item 

  
  if genome.bias:
    list(graph.nodes(data=True))[i+1][1]["out"] = 1 

  i = i+2
  output = []
  current_type_node = list(graph.nodes(data=True))[i][1]["typeNode"]
  while current_type_node == "output":

    try:
      current_type_node = list(graph.nodes(data=True))[i][1]["typeNode"]
    except:# IndexError or KeyError:
      break


    node = (list(graph.nodes)[i])

    calc = calculate_node(graph, node)
    graph.nodes(data=True)[node]["out"] = calc
    output.append(calc)
    i += 1

  return output


def calculate_node(graph, node):

  
  predecessors = list(graph.predecessors(node))
    
  if len(predecessors) == 0:
    graph.nodes(data=True)[node]["out"] = 0.5
    return 0.5
  else:
    inputs = []
    weights = []
    for j in predecessors:
      
      connection_atributes = graph.get_edge_data(j, node)
      if connection_atributes["enabled"]:
        out = (graph.nodes(data=True))[j]["out"]
        
        if not (out is None):#out exists
          inputs.append(out)
        else:
          inputs.append(calculate_node(graph, j))
        
        weights.append(connection_atributes["weight"])
    return calculate_percepetron(inputs, weights)
        


def calculate_percepetron(inputs, weights):
  total = 0
  for i,item in enumerate(inputs):
    total += item*weights[i]
  return sigmoid(total)


#makes x a number between 0 to 1


def sigmoid(x):
  return 1/(1+math.exp(-x))

def make_0_to_1(x, bottom, top):
  x = x-bottom
  x = x/top
  return x