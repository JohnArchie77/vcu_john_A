# (2n+1)^2 is that is equal to the area square
# to find the corners you first multiple the (2n+1)^2 by 4 and then to compensate for the angles 2,3,4 you should subtract by 12n
# the formula should look like this 4(2n+1)^2-12n
# to sum up all corners for 4(2n+1)^2-12n+a(n-1)
# a is equal to the 501**501 and 5*5 to find the area of the square
# by using using the total of of sum of diagonals I was able to find the rings I used this to properly work out the math
#101 = 4(2n+1)^2 - 12n + 25(n-1) # Solving for n where n = number of rings, 
#  # 101 = 4(2n+1)*(2n+1) -12n + 25(n-1) # FOIL out the right side of the equation
#101 = 4(4n+1)- 12n + 25(n-1) 
#101 = 16n^2+16n+4 -12n + 25n - 25 # Distributing the 4 
# #101 = 16n^2 +29n - 21 
#16n^2 + 29n -21 = 101 # Flip the equation
#n^2 + 29n/16 = 61/8 
#n^2 + 29n/16 + 841/1024 = 8649/1024 # Take one half of the coefficient of n and square it, then add it to both sides. 
#(n+(29/32))^2 = 8649/1024 # Factor left side
#n+(29/32) = 93/32 +Square root both sides
#n = 93/32 - 29/32
#n = 2  n = number of rings
#83960501 = 4(2n+1)^2 - 12n + 251001(n-1) # Solving for n where n = number of rings, 
# 83960501 = 4(2n+1)(2n+1) -12n + 251001(n-1) # FOIL out the right side of the equation
#83960501 = 4(4n+1)- 12n + 251001(n-1) 
#83960501 = 16n^2+16n+4 -12n + 251001n - 251001 # Distributing the 4 
#83960501 = 16n^2 +251005n - 250997 
#16n^2 + 251005n -250997 = 83960501 # Flip the equation
#n^2 + 251005n/16 = 42105749/8  **
#n^2 + 251005n/16 + 63003510025/1024 = 68393045897/1024 # Take one half of the coefficient of n and square it, then add it to both sides. 
#(n+(251005/32))^2 = 68393045897/1024 # Factor left side
#n + (251005/32) = ((sqrt(68393045897))/32)#Square root both sides
#n = ((sqrt(68393045897))/32) - (251005/32)
#n = 328.613795 # n = number of rings


n = 328.613795 #Number of rings in 501x501 
part_one = 2*n+1
part_two = part_one**2*4
part_three= part_two -12*n
part_four= (n-1)*251001 # the area of the square
answer_before_round= part_three +part_four
answer= round(answer_before_round)
print(answer)