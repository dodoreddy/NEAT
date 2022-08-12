import gene_encoding

nodes = gene_encoding.Genes(5, 3)
connection = gene_encoding.Connection(2,6, 3, 1)
nodes.append(connection)

nodes.output_connections()

