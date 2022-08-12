import gene_encoding

nodes = gene_encoding.Genes(5, 3)
o = 7
i = 0
nodes.add_node(8)
nodes.add_node(9)

nodes.append(gene_encoding.Connection(i, 8, 3, 9))
nodes.append(gene_encoding.Connection(8, 9, 3, 1))

nodes.append(gene_encoding.Connection(9, o, 3, 1))
nodes.append(gene_encoding.Connection(9, 8, 3, 1))


nodes.output_connections()

