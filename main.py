import gene_encoding

nodes = gene_encoding.Genes(5, 3)

nodes.add_connection(0, 5, 4, 0, False)

nodes.output_connections()