from gene_encoding import *
from gene_encoding import Genes
import calculate
def main():
  gene = Genes(3,3, True)
  gene.append(0, 4, 1, 1, True)

  
  output = calculate.calculate_network(gene, [5,5,5], bottom = 0, top=10)

  for i in output: print(i)












if __name__ == "__main__":
  main()