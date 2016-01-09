def perm3():
 for i in range(0,3):
     for j in range(0,3):
         for k in range(0,3):
 #a possible solution
            possibleSol = [i,j,k]
            if i!=j and j!=k and i!=k:
 #is a solution
                print possibleSol
