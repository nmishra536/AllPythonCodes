from list import *
def main():
  try:
    L = List()
    L.append(1)
    L.append(2)
    L.append(3)
    print(L[1])
    L[1] = 69
    J = L.reverse()
    J * 2 == 2 * L
    H = List()
    H.append(5)
    H.append(6)
    H.append(7)
    print(L + J)
    print(L+= J)


  except ValueError:
    pass
if __name__=='__main__':
  main()
