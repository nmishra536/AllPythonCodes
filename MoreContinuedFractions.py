
#------------------------------------------------------------------------------ 
#  Navya Mishra
#  nmishra3
#  CSE 30-02 Spring 2021
#  la3
#
#  MoreContinuedFractions.py
#
#------------------------------------------------------------------------------


from rational import *
from decimal import *





def CF2R(L):
    if len(L) - 1 >= 1:
        a= L.pop(0)
        return Rational(a) + Rational.inverse(CF2R(L))
    else:
        return Rational(L[0])
    
def R2CF(x):
  
  n = x.n
  d = x.d
  L = []
  while d != 0:
    q = n%d
    r = (n - q)//d
    L.append(r)
    n = d
    d = q
  return L
     
  
  
   
def GCF2R(L):
   if len(L) == 0:
      return Rational(1)
   if len(L) == 1:
      return Rational(L[0])
   else:
     p = Rational(L[0])
     o = Rational(L[1])
     return p + (o/ GCF2R(L[2:]))
   

def pi_gen():
   yield 0
   yield 4
   k = 1
   while True:
      yield (2*k)-1
      yield k**2
      k += 1

   
def main():
   J = []

   
   A = pi_gen()
   for i in range(265):
     J.append(next(A))
     #this part is fine manually checked 
     
   g = GCF2R(J)
   print()
   print(str(g))
   
   
   getcontext().prec = 101 
   a = Decimal(g.n)/Decimal(g.d)
   #this also works manually tested
   print()
   print(a)
   Y = R2CF(g)
   #this works (manually tested)
   print()
   print(Y)
   print()
   
# end

        
    

if __name__ == '__main__':
    main()
