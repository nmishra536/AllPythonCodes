
#-------------------------------------------------------------------------------
#  Subset.py
#-------------------------------------------------------------------------------
#------------------------------------------------------------------------------ 
#  Navya Mishra
#  nmishra3
#  CSE 30-02 Spring 2021
#  la2 
#  Subset.py
#------------------------------------------------------------------------------

import sys

def to_string(L):
  if len(L) == 0:
    return"{ }"
  else:
    return "{" + str(L)[1:-1] +"}"

def printSubsets(L, n, k, i):
  if k == 0:
      print(to_string(L))
  elif k > n-i + 1:
      pass 
  elif k > 0: 
      L.append(i)
      printSubsets(L, n, k-1, i+1)
      L.pop()
      printSubsets(L,n, k, i+1) 
  else:
      printSubsets(L, n, k, i+1) 

def main():

  usage = "Usage: python3 Subset.py n k (where 0<=k<=n)"
  if len(sys.argv) !=3:
    print(usage, file = sys.stderr)
    exit()
  if len(sys.argv) == 3:
    if sys.argv[1].isdigit():
      if sys.argv[2].isdigit():
        B = int(sys.argv[1])
        k = int(sys.argv[2])
        s = []
        if B < k:
          print(usage, file = sys.stderr)
          exit()
        else:
          printSubsets(s, B, k, i=1)
      else:
        print("cannot parse '"+str(sys.argv[2])+"' as int\n" + usage, file = sys.stderr)
        exit()
    else:
      print("cannot parse '"+str(sys.argv[1])+"' as int\n" + usage, file = sys.stderr)
      exit()
        


 
 
    
if __name__=='__main__':
  main()
  
