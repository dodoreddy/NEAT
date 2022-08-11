class node:
  def __init__(self, num, type = "hidden"):
    self.type = type
    self.num = num


class node_genome:
  nodes = []
  def __init__(self, input, output):
    for i in range(0, input):
      self.nodes.append(node(i, "input"))
    for i in range(0, output):
      self.nodes.append(node(len(self.nodes), "output"))

  def output_nodes(self):
    for i in self.nodes:
      print(str(i.num)+" is type "+i.type)

class connection:
  def __init__(self, input, output, weight, innov, enabled = True):
    