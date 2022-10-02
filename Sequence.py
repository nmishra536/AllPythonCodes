#-------------------------------------------------------------------------------
#  SequenceTemplate.py
#  Two functions that return generators.
#-------------------------------------------------------------------------------
#------------------------------------------------------------------------------ 
#  Navya Mishra
#  nmishra3
#  CSE 30-02 Spring 2021
#  la1 
#  Sequence.py
#------------------------------------------------------------------------------
def power_remainder(n, m, r):
   k = 1
   while True:
        if ((k ** n) % m) == r:
            yield (k ** n)
        k += 1
   



# end

def common_terms(g, h):
   n = next(g)
   j = next(h)
   while True:
        if n > j:
            j = next(h)
        if n < j:
            n = next(g)
        if n == j:
            yield j #rlly doesnt matter if j or n
            j = next(h)
            n = next(g)





   # end
# end

def main():

   A = power_remainder(2, 3, 1)
   B = power_remainder(3, 5, 4)
   C = common_terms(power_remainder(2, 3, 1), power_remainder(3, 5, 4))

   print()
   for i in range(15):
      s = "  {0:<12}{1:<12}{2:<12}".format(next(A), next(B), next(C))
      print(s)
   # end
   print()

# end

#-------------------------------------------------------------------------------
if __name__=='__main__':

   main()

# end
      
