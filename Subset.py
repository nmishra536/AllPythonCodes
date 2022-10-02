import sys
#someone said this is how you do commandline
def to_string(B):
  leonard = "{"
  print(leonard, end = '')
  for i in range(len(B)):
    if B[i] == 1:
     leonard = leonard + str(i)+","
  carolina = leonard[:-1]+"}"
  if len(carolina) > 2:
     print(carolina.lstrip("{"))
     return carolina
  else:
     print(' ' +carolina)
     return "{"+' ' +carolina


def printSubsets(B, k, i): 

  n = len(B)-1
  B[0]= '*' #put in something random 
  if k == 0: 
        to_string(B)
  elif k > n-i + 1:
      pass #it's hopeless just move on
  elif k > 0: 
      B[i] = 1
      printSubsets(B, k-1, i+1)
      B[i] = 0
      printSubsets(B,k, i+1) #tutors are great
  else:
      printSubsets(B, k, i+1) 
 
 
    
if __name__=='__main__':
  if len(sys.argv) == 3:

    B = sys.argv[1]
    k = sys.argv[2]
    try:
      B = sys.argv[1]
      k = sys.argv[2]
      B = int(B)
      k = int(k)
      s = []
      for j in range(B+1):
        s.append(0) 
      #the set has been made
      (printSubsets(s, k, i=1))

    except ValueError:
      exit
      

     
