class Node:
  def __init__(self, number, type="hidden", is_active = True):
    self.number = number
    self.active = is_active
    self.type = type

  def __repr__(self):
    return(f"{self.type} Node {self.number} is set to {self.active}")

class Node_genome:
  def __init__(self, input, output):
    self.nodes= []

    #input
    for i in range(input):
      node = Node(i, "input")
      self.nodes.append(node)

    #output
    for i in range(output):
      node = Node(i, "output")
      self.nodes.append(node)

  def __repr__(self):
    out = ""
    for i in self.nodes:
      out = out+(i.__repr__()+"\n")

    out = out[:-1]
    return out
      