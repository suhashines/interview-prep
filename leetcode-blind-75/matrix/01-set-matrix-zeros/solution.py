def setZeroes(mat):

    m = len(mat)
    n = len(mat[0])

    # first pass
    # we use the top row and left column of mat as markers of rows and columns
    col_0 = 1

    for i in range(m):

        for j in range(n):

            if mat[i][j] == 0 :
                if j!=0:
                    mat[0][j] = 0
                    mat[i][0] = 0
                else:
                    col_0 = 0
        
    print(f"mat after first pass {mat}")

    # 2nd pass, don't modify the markers

    for i in range(1,m):

        for j in range(1,n):

            if mat[i][0] == 0 or mat[0][j] == 0 :
                mat[i][j] = 0
    
    print(f"after 2nd pass {mat}")

    # now modify the markers
    for j in range(1,n):
        if mat[0][0] == 0:
            mat[0][j] = 0 

    for i in range(m):
        if col_0 == 0:
            mat[i][0] = 0       
    
    return mat

matrix=[[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]]
print(setZeroes(matrix))