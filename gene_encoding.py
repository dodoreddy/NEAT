import networkx as nx


class Node:
    def __init__(self, num, typeNode="hidden"):
        self.typeNode = typeNode
        self.num = num


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

    def add_node(self, node):
        self.nodes.append(node)

    def add_node(self, nodeNum, typeNode="hidden"):
        self.nodes.append(Node(nodeNum, typeNode))


class Connection:
    def __init__(self, input, output, weight, innov, enabled=True):
        self.input = input
        self.output = output
        self.weight = weight
        self.innov = innov
        self.enabled = enabled


class ConnectionGenome:
    def __init__(self):
        self.connections = []

    def __len__(self):
        return len(self.connections)

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n >= len(self.connections):
            raise StopIteration

        self.n = self.n + 1
        return self.connections[self.n - 1]

    def add_connection(self, connection):
        self.connections.append(connection)

    def add_connection(self, input, output, weight, innov, enabled=True):
        self.connections.append(Connection(input, output, weight, innov, enabled=True))

    def output_connections(self):
        for i in self.connections:
            print(
                f"Connection with innovation number {i.innov}, goes from {i.input} to {i.output} and has a weight of {i.weight}. Is enabled {i.enabled}")


class Genes(ConnectionGenome, NodeGenome):
    def __init__(self, input, output):
        self.g = nx.DiGraph()

        NodeGenome.__init__(self, input, output)
        ConnectionGenome.__init__(self)

        for i, num in enumerate(self.nodes):
            self.g.add_node(num, typeNode=self.nodes[i].typeNode)

    def add_connection(self, connection):
        if  connection.input == "output" and connection.output == "output":
            raise Exception("input Neuron and output Neuron cannot both be output")

        if connection.input == "output":
            raise Exception("input Neuron cant be an output neuron")

        if  connection.input == "input" and connection.output == "input":
            raise Exception("input Neuron and output Neuron cannot both be input")

        if connection.ouput == "input":
            raise Exception("output Neuron cant be an input neuron")

        self.g.add_edge(connection.input, connection.output, innovationNumber=connection.innov,
                        weight=connection.weight, enabled=connection.enabled)

        if not (nx.is_directed_acyclic_graph(self.g)):
            self.g.remove_edge(connection.input, connection.output)
            raise Exception("created a cyclic graph")

        self.add_connection(connection)

    def add_connection(self, input, output, weight, innov, enabled=True):
        if input == "output" and output == "output":
            raise Exception("input Neuron and output Neuron cannot both be output")

        if connection.input == "output":
            raise Exception("input Neuron cant be an output neuron")

        if connection.input == "input" and connection.output == "input":
            raise Exception("input Neuron and output Neuron cannot both be input")

        if connection.ouput == "input":
            raise Exception("output Neuron cant be an input neuron")

        self.g.add_edge(connection.input, connection.output, innovationNumber=connection.innov,
                        weight=connection.weight, enabled=connection.enabled)

        if not (nx.is_directed_acyclic_graph(self.g)):
            self.g.remove_edge(connection.input, connection.output)
            raise Exception("created a cyclic graph")

        self.add_connection(connection)


