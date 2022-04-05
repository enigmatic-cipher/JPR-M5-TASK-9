"""
Given n as input, print the following pattern.
Input-> 2
Output-> 
X1 
XX12
"""

n = int(input("Enter Number: "))
sy = "X"
pt = ""

for i in range (1,n+1):
  pt = (sy)*i
  for j in range(1,i+1):
    pt = pt + str(j)
  print(pt)
  
  