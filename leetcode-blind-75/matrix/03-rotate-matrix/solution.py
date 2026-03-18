def rotate_matrix(mat):

    m = len(mat)
    n = len(mat[0])

    for i in range(m):

        for j in range(i+1,n):

            # swap mat[i][j] with mat[j][i]
            tmp = mat[i][j]
            mat[i][j] = mat[j][i]
            mat[j][i] = tmp
    
    # after this step, we have a transpose of the original matrix
    # now for each rows we swap the left and right column values

    for i in range(m):

        left,right = 0,n-1

        while left<right:

            # swap the left,right
            tmp = mat[i][left]
            mat[i][left] = mat[i][right]
            mat[i][right] = tmp
            left += 1
            right -= 1
    
    return mat

matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

print(rotate_matrix(matrix))