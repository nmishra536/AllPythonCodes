#ContinuedFractions.py
import sys
from rational import *
from decimal import *
def usage():
   sys.stderr.write("Usage: $ python3 ContinuedFractions.py <input file> <output file>")
   exit()




def CF(L):
    if len(L) - 1 >= 1:
        a= L.pop(0)
        return Rational(a) + Rational.inverse(CF(L))
    else:
        return Rational(L[0])
    

def main():

   # check command line arguments and open files
   if len(sys.argv)!=3:
      usage()
   # end
   try:
      infile = open(sys.argv[1])
   except FileNotFoundError as e:
      print(e, file=sys.stderr)
      usage()
   # end
   outfile = open(sys.argv[2], 'w')

   # read in each line of infile, reverse it, then print to outfile
   lines = infile.readlines()
   print("", file=outfile)
   for S in lines:
      l = list(S.split(" "))
      L = list(map(int,l))
      h = (CF(L))
      getcontext().prec = 100 # set Decimal precision to 1000 digits
      a = Decimal(h.n)/Decimal(h.d)
      print(str(h), file=outfile)
      print(a, file=outfile)
      print("", file=outfile)
  # end

   infile.close()
   outfile.close()

 

# end

        
    

if __name__ == '__main__':
    main()
