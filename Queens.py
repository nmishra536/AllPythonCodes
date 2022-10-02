#------------------------------------------------------------------------------ 
#  Navya Mishra
#  nmishra3
#  CSE 30-02 Spring 2021
#  pa2
#  Queens.py
#------------------------------------------------------------------------------
import sys
#------------------------------------------------------------------------------
#i is row number

def placeQueen(B, i, j): #individually checked. this works
  #mark all the squares she could kill
  if B[i][j] == 0:
    B[i][0] = j
    B[i][j] = 1 
    for k in range(1, len(B)):
      if k < len(B):
        if B[k][j] != 1:
          B[k][j] -=1
      for l in range(1, len(B)): 
        if (abs(k-i)==abs(l-j)):
          if B[k][l] != 1:
            B[k][l] -=1 #takes care of diagonals 
            #if on (2,3), (3-2) == (4-3) and abs(1-2) == abs(4-3) 
      

def removeQueen(B, i, j): #individually checked. this works
  if B[i][j] == 1:
    B[i][0] = 0
    B[i][j] = 0 
    for k in range(1, len(B)):
      if k < len(B): 
        if B[k][j] != 0:
          B[k][j] +=1
      for l in range(1, len(B)): 
        if (abs(k-i)==abs(l-j)):
          if B[k][l] != 0:
            B[k][l] +=1 
      
              



def printBoard(B): #individually checked. this works
    print("(", end = "")
    for venti in range(1,len(B)):
      if venti != len(B)-1:
        print(str(B[venti][0]) + ", ", end = "")
      else:
        print(str(B[venti][0]) + ")")

     


def findSolutions(B, i, mode, sammy=0):
  #n is the last row 
  #all the queens have already been placed base case for recursion 
  #if verbose, print that solution to n-queens
  #else return 1 so it can add to sum
  
  if i > len(B)-1:
    if mode == "-v":
      printBoard(B)
    return 1
  else: 
    for horse in range(1,len(B)): #for each square on row i
      if B[i][horse] == 0:
        placeQueen(B,i ,horse)
        sammy += findSolutions(B, i+1, mode) #I hope this is actually adding 
        removeQueen(B,i ,horse)
  return sammy


#------------------------------------------------------------------------------
# definition of function main()
#------------------------------------------------------------------------------
def main():
  

  vars = "Usage: python3 Queens.py [-v] number\nOption: -v verbose output, print all solutions"
  if len(sys.argv) == 2:
    if sys.argv[1].isdigit() == True:
      n = int(sys.argv[1])
      caillou = "standard"
      B = [[0 for i in range(n+1)] for j in range(n+1)]
      print(str(n)+"-Queens has", findSolutions(B,1,caillou) , "solutions")
    else:
      print(vars, file = sys.stderr)
      exit()

  elif len(sys.argv) > 2:
    if sys.argv[1] == '-v' and sys.argv[2].isdigit() == True :
      n = int(sys.argv[2])
      caillou = sys.argv[1]
      B = [[0 for i in range(n+1)] for j in range(n+1)]
      print(str(n)+"-Queens has", findSolutions(B,1,caillou) , "solutions")
    else:
      print(vars, file = sys.stderr)
      exit()

  else:
    print(vars, file = sys.stderr)
    exit()
   

# end

#------------------------------------------------------------------------------
# closing conditional that calls main()
#------------------------------------------------------------------------------
if __name__=='__main__':

   main()

# end

 
