import networkx as nx
from multipledispatch import dispatch


class Node:
    def __init__(self, num, typeNode="hidden"):
        self.typeNode = typeNode
        self.num = num


    def __getitem__(self, index):
      return_tuple = []
      if type(index) == tuple:
        for i in index:
          try:
            return_tuple.append(getattr(self, i))
          except:
            raise KeyError(f"{index} does not exist")
        return tuple(return_tuple)
      try:
        return getattr(self, index)
      except:
        raise KeyError(f"{index} does not exist")
      

class NodeGenome:
    nodes = []
    def __init__(self, input, output):
      for i in range(0, input):
        self.nodes.append(Node(i, "input"))
      for i in range(0, output):
        self.nodes.append(Node(len(self.nodes), "output"))

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n >= len(self.nodes):
            raise StopIteration

        self.n = self.n + 1
        return self.nodes[self.n - 1].num

    def __len__(self):
        return len(self.nodes)

    def output_nodes(self):
        for i in self.nodes:
            print(str(i.num) + " is type " + i.typeNode)

    def append(self, node):
        self.nodes.append(node)

    def append(self, nodeNum, typeNode="hidden"):
        self.nodes.append(Node(nodeNum, typeNode))



    def iterate(self, var):
      class iterable_object:
        def __init__(self):
          self.list_obj = []
          
        def add(self, x):
          self.list_obj.append(x)

        def __contains__(self, x):
          return x in self.list_obj
        
        def __iter__(self):
          self.n = 0
          return self
          
        def __next__(self):
          if self.n >= len(self.list_obj):
            raise StopIteration

          self.n = self.n + 1
          return self.list_obj[self.n - 1]
          
      
      
      return_object = iterable_object()
      
      for i in self.nodes:
        return_object.add(i[var])
      return return_object
        
        





    def __getitem__(self, index):
      for i in self.nodes:
        if i.num == index:
          return i
      raise Exception("index not in list")

class Connection:
    def __init__(self, input, output, weight, innov, enabled=True):
        self.input = input
        self.output = output
        self.weight = weight
        self.innov = innov
        self.enabled = enabled

    def __getitem__(self, index):
      return_tuple = []
      if type(index) == tuple:
        for i in index:
          try:
            return_tuple.append(getattr(self, i))
          except:
            raise KeyError(f"{index} does not exist")
        return tuple(return_tuple)
      try:
        return getattr(self, index)
      except:
        raise KeyError(f"{index} does not exist")





class ConnectionGenome:
    def __init__(self):
        self.connections = []

    def __len__(self):
        return len(self.connections)

    def __iter__(self):
        self.n = 0
        return self

    def __contains__(self, x):
      return x in self.list_obj
  
    def __next__(self):
        if self.n >= len(self.connections):
            raise StopIteration

        self.n = self.n + 1
        return self.connections[self.n - 1]

    def append(self, connection):
        self.connections.append(connection)

    def append(self, input, output, weight, innov, enabled=True):
        self.connections.append(Connection(input, output, weight, innov, enabled=True))

    def output_connections(self):
        for i in self.connections:
            print(
                f"Connection with innovation number {i.innov}, goes from {i.input} to {i.output} and has a weight of {i.weight}. Is enabled {i.enabled}")


    def iterate(self, var):
      class iterable_object:
        def __init__(self):
          self.list_obj = []
        def add(self, x):
          self.list_obj.append(x)
        def __iter__(self):
          self.n = 0
          return self
        def __next__(self):
          if self.n >= len(self.list_obj):
            raise StopIteration

          self.n = self.n + 1
          return self.list_obj[self.n - 1]
          
      
      return_object = iterable_object()
      
      for i in self.connections:
        return_object.add(i[var])
      return return_object
        
        










class Genes(ConnectionGenome, NodeGenome):
    def __init__(self, input, output):
        self.g = nx.DiGraph()
        NodeGenome.__init__(self, input, output)
        ConnectionGenome.__init__(self)

        for i, num in enumerate(self.nodes):
            self.g.add_node(num, typeNode=self.nodes[i].typeNode)


  
    def append(self, input, output, weight, innov, enabled=True):
        if not(input in self.iterate_nodes("num")):
          raise Exception("Input neuron must be an existing neuron")
        if not(output in self.iterate_nodes("num")):
          raise Exception("Output neuron must be an existing neuron")
      
      
        input_type = self.nodeList(input).typeNode
        output_type = self.nodeList(output).typeNode
      
        if input_type == "output" and output_type == "output":
            raise Exception("input Neuron and output Neuron cannot both be output")

        if input_type == "output":
            raise Exception("input Neuron cant be an output neuron")

        if input_type == "input" and output_type == "input":
            raise Exception("input Neuron and output Neuron cannot both be input")

        if output_type == "input":
            raise Exception("output Neuron cant be an input neuron")
          
        self.g.add_edge(input, output, innovationNumber=innov,
                        weight=weight, enabled=enabled)

        if not (nx.is_directed_acyclic_graph(self.g)):
            self.g.remove_edge(input, output)
            raise Exception("created a cyclic graph")

        ConnectionGenome.append(self, input, output, weight,
                        innov, enabled=enabled)




  
    def append(self, connection):
        if not(connection.input in self.iterate_nodes("num")):
          raise Exception("Input neuron must be an existing neuron")
        if not(connection.output in self.iterate_nodes("num")):
          raise Exception("Output neuron must be an existing neuron")
      
      
        input_type = self.nodeList(connection.input).typeNode
        output_type = self.nodeList(connection.output).typeNode
      
        if input_type == "output" and output_type == "output":
            raise Exception("input Neuron and output Neuron cannot both be output")

        if input_type == "output":
            raise Exception("input Neuron cant be an output neuron")

        if input_type == "input" and output_type == "input":
            raise Exception("input Neuron and output Neuron cannot both be input")

        if output_type == "input":
            raise Exception("output Neuron cant be an input neuron")
          
        self.g.add_edge(connection.input, connection.output, innovationNumber=connection.innov,
                        weight=connection.weight, enabled=connection.enabled)

        if not (nx.is_directed_acyclic_graph(self.g)):
            self.g.remove_edge(connection.input, connection.output)
            raise Exception("created a cyclic graph")

        ConnectionGenome.append(self, connection)
    def iterate_nodes(self, var):
      return NodeGenome.iterate(self, var)
    def iterate_connections(self, var):
      return ConnectionGenome.iterate(self, var)
    def nodeList(self, index):
      return NodeGenome.__getitem__(self, index)
  

      