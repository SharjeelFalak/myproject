def LargestSquare(n):
 f = 1
 while n >= f*f:
 f += 1
 q = (f-1)*(f-1)
 print("The largest square number provided is " + 
str(q) + " which is the square of " + str(f-1)) 
# it looks like I learned how to use 
#git today