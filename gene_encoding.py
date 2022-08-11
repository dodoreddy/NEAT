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

    def output_nodes(self):
        for i in self.nodes:
            print(str(i.num) + " is type " + i.typeNode)


class Connection:
    def __init__(self, input, output, weight, innov, enabled=True):
        pass
