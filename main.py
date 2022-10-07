from gene_encoding import *
from gene_encoding import Genes
import calculate

def main():
  gene = Genes(2,1, True)

  #checks for 1s
  gene.add_node(4)

  #checks for 1
  gene.add_node(5)

  #connections
  #s e w i
  gene.append(1, 4, -20, 1)
  gene.append(2, 4, -20, 1)
  gene.append(0, 4, 30, 1)
  
  gene.append(1, 5, 20, 1)
  gene.append(2, 5, 20, 1)
  gene.append(0, 5, -10, 1)
  
  gene.append(4, 3, 20, 1)
  gene.append(5, 3, 20, 1)
  gene.append(0, 3, -30, 1)
  
  tests = [[0,0],[0,1],[1,0],[1,1]]
  expected = [0,1,1,0]
  out = []
  for test in tests:
    output = calculate.calculate_network(gene, test)
    out.append(round(output[0]))
    for i in output: print(round(i))
  print(out)
  print(expected)












if __name__ == "__main__":
  main()