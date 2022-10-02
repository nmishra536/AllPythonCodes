#------------------------------------------------------------------------------
#  Navya Mishra
#  nmishra3
#  CSE 30-02 Spring 2021
#  pa3
#  lines.py
#------------------------------------------------------------------------------
import math


#------------------------------------------------------------------------------
#  Do not change the definition of the Point class, other than to define 
#  the function join() at the end.
#------------------------------------------------------------------------------
class Point(object):
   """Class representing a Point in the x-y coordinate plane."""

   def __init__(self, x, y):
      """Initialize a Point object."""
      self.xcoord = x
      self.ycoord = y
   # end

   def __str__(self):
      """Return the string representation of a Point."""
      return '({}, {})'.format(self.xcoord, self.ycoord)
   # end

   def __repr__(self):
      """Return the detailed string representation of a Point."""
      return 'geometry.Point({}, {})'.format(self.xcoord, self.ycoord)
   # end

   def __eq__(self, other):
      """
      Return True if self and other have the same coordinates, False otherwise.
      """
      eqx = (self.xcoord==other.xcoord)
      eqy = (self.ycoord==other.ycoord)
      return eqx and eqy
   # end

   def distance(self, other):
      """Return the distance between self and other."""
      diffx = self.xcoord - other.xcoord
      diffy = self.ycoord - other.ycoord
      return math.sqrt( diffx**2 + diffy**2 )
   # end

   def norm(self):
      """Return the distance from self to the origin (0, 0)."""
      return self.distance(Point(0,0))
   # end

   def midpoint(self, other):
      """Return the midpoint of the line segment from self to other."""
      midx = (self.xcoord + other.xcoord)/2
      midy = (self.ycoord + other.ycoord)/2
      return Point(midx, midy)
   # end

   #---------------------------------------------------------------------------
   #  Fill in the definition of this function, belonging to the Point class.
   #---------------------------------------------------------------------------
   def join(self, other):
      if self.xcoord == other.xcoord and self.ycoord == other.ycoord:
        return None
      else:
        if (other.xcoord - self.xcoord) != 0:
           slope = (other.ycoord - self.ycoord)/(other.xcoord - self.xcoord)
        else:
           slope = "infinity"
        return Line(Point(self.xcoord, self.ycoord), slope)
        
      
   # end     

# end


#------------------------------------------------------------------------------
#  Fill in the definitions of each method in the Line class.
#------------------------------------------------------------------------------
class Line(object):
   """Class representing a Line in the x-y coordinate plane."""
   
   def __init__(self, P, m):
      self.slope = m
      self.point = P
      
   # end

   def __str__(self):
      """Return a string representation of a Line."""
      return "Line through ({}, {}) of slope {}".format(self.point.xcoord, self.point.ycoord, self.slope)
   # end

   def __repr__(self):
      """ Return a detailed string representation of a Line."""
      return "lines.Line(point=({}, {}), slope={})".format(self.point.xcoord, self.point.ycoord, self.slope)
   # end

   def __eq__(self, other):
      if self.slope == "infinity":
         if (self.slope == other.slope)and (self.point.xcoord== other.point.xcoord):
            return True
      else:
         if self.slope == other.slope and self.point.ycoord - (self.slope * self.point.xcoord) == other.point.ycoord - (other.slope * other.point.xcoord):
            return True
   # end

   def parallel(self, other):
      """
      Return True if self and other are parallel lines, False otherwise.
      """
      if self.slope == other.slope:
        return True
   # end

   def perpendicular(self, other):
      """
      Return True if self and other are perpendicular lines, False otherwise.
      """
      if self.slope != 0 and self.slope != "infinity":
         if other.slope == (-1 / self.slope):
           return True
      elif self.slope == 0 and other.slope == "infinity":
         return True
      elif self.slope == "infinity" and other.slope == 0:
         return True
   # end

   def contains_point(self, P):
      """
      Return True if self contains point P, False otherwise.
      """
      m = self.slope
      if m != 0 and m!= "infinity":
         b = self.point.ycoord - (m * self.point.xcoord)
         if ((m*P.xcoord)+b) == P.ycoord:
            return True
      elif m == "infinity":
         if self.point.xcoord == P.xcoord:
            return True
      elif m == 0:
         if self.point.ycoord == P.ycoord:
            return True
   # end

   def intersect(self, other):
      """
      If self and other are parallel, return None.  Otherwise return their
      Point of intersection.
      """
      if self.slope == other.slope:
        return None
      else:
        m1 = self.slope
        m2 = other.slope
        if m1 != "infinity" and m2 != "infinity":
           b1 = self.point.ycoord - (m1 * self.point.xcoord)
           b2 = other.point.ycoord - (m2 * other.point.xcoord)
           x = (b1-b2)/(m2-m1)
           y = (m1 * x) + b1
           return Point(x, y)
        elif m1 == "infinity":
            x = self.point.xcoord
            b2 = other.point.ycoord - (m2 * other.point.xcoord)
            y = (m2 * x) + b2
            return Point(x,y)
        elif m2 == "infinity":
            x = other.point.xcoord
            b1 = self.point.ycoord - (m1 * self.point.xcoord)
            y = (m1 * x) + b1
            return Point(x,y)
            
            
        
        

   # end

   def parallel_line(self, P):
      """Returns the Line through P that is parallel to self."""
      return Line(P, self.slope)
      
   # end

   def perpendicular_line(self, P):
      """Returns the Line through P that is perpendicular to self."""
      if self.slope != 0 and self.slope != "infinity":
         return Line(P, -1/(self.slope))
      elif self.slope == 0:
         return Line(P, "infinity")
      else:
         return Line(P, 0)
   # end

# end


#------------------------------------------------------------------------------
#  Do not change functon main(). Its role is just to test all of the above.
#  Actually you can change it during your own independent testing, but return
#  it to exactly this state before you submit the project.
#------------------------------------------------------------------------------
def main():

   P = Point(1, 3)
   Q = Point(3, 3)
   R = Point(1, 1)
   S = Point(3, 1)
   T = Point(4, 3)
   U = Point(5, 5)
   V = Point(2, 2)
   W = Point(2, 5)
   X = Point(2, -1)

   A = Line(P, -1)
   B = Line(R, 1)
   C = S.join(T) #points_to_line(S, T)
   D = Line(W, 'infinity')
   E = Line(Q, 0)
   F = C.parallel_line(P)

   print()
   print('A =', A)
   print(repr(A))
   print()
   print('B =', B)
   print(repr(B))
   print()
   print('C =', C)
   print(repr(C))
   print()
   print('D =', D)
   print(repr(D))
   print()
   print('E =', E)
   print(repr(E))
   print()
   print('F =', F)
   print(repr(F))

   print()
   print(B.intersect(C)==U)
   print(A.intersect(B)==V)
   print(D.intersect(C)==X)
   print(D.intersect(Line(T,'infinity'))==None)
   print(A.perpendicular(B))
   print(D.perpendicular(E))
   print(A.parallel(B.perpendicular_line(Q)))
   print(A.contains_point(S))
   print(B.contains_point(U))
   print(C.contains_point(X))
   print(F.contains_point(W))

   print()

# end

#------------------------------------------------------------------------------
if __name__=='__main__':

   main()

# end
