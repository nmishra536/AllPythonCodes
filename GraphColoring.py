#------------------------------------------------------------------------------ 
#  Navya Mishra
#  nmishra3
#  CSE 30-02 Spring 2021
#  pa6
#
#  GraphColoring.py
#------------------------------------------------------------------------------
from graph import *
import sys
def usage():
   print("Usage: $ python3 LineReverse.py <input file> <output file>", 
         file=sys.stderr)
   exit()
# end
  

def CheckProperColoring(G):
  for i in G.vertices:
    for j in G._adj[i]:
      if G.getColor(i)==G.getColor(j):
        return False
  return True
      
   
  

def main():
  # check command line arguments and open files
   if len(sys.argv)!=3:
      usage()
   # end
   try:
      sys.stdin = open(sys.argv[1])
   except FileNotFoundError as e:
      print(e, file=sys.stderr)
      usage()
   # end



   V = []
   sys.stdout = open(sys.argv[2], 'w')
   n = int(input())
   for i in range(1,n+1):
     V.append(i)
   E = [tuple(map(int, i.split(' '))) for i in sys.stdin]
   G = Graph(V,E)
   Color = G.Color()
   m = '{} colors used: {}'.format(len(Color),Color)
   print(m)
   print()
   print("vertex    color")
   print("----------------")
   for h in G.vertices:
     horse = '{:<10}{}'.format(h, G.getColor(h))
     print(horse)

   #print()
   #msg = 'coloring is proper: {}'.format(CheckProperColoring(G))
   #print(msg)
        
     
      
   # end

   sys.stdin.close()
   sys.stdout.close()




if __name__=='__main__':

   main()

# end
