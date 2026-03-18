def spiral_matrix(mat):

    ans = []
    l,r = 0, len(mat[0])
    t,b = 0, len(mat)

    while l<r and t<b :

        # go right
        for j in range(l,r):
            ans.append(mat[t][j])
        
        # we're done with the top row
        t += 1
        # go down
        for i in range(t,b):
            ans.append(mat[i][r-1])
        
        #  we're done with the right column
        r -= 1

        # now the important thing, if we have a row or column matrix we must stop here
        if not (t<b and l<r) :
            break

        # go left
        for j in range(r-1,l-1,-1):
            ans.append(mat[b-1][j])
        # we're done with the bottom
        b -= 1
        # go up
        for i in range(b-1,t-1,-1):
            ans.append(mat[i][l])
        
        # we're done with the left
        l += 1
    return ans

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(spiral_matrix(matrix))