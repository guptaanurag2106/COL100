#1
def gridPlay(grid):
    M=len(grid)
    N=len(grid[0])
    #initialize all elements of minCost list as 0
    minCost=[[0 for i in range(N)] for j in range(M)]

    #minCost for border points is the sum of costs along the border
    #INV at ith iteration first row upto i-1 th column of minCost have been given correct costs
    for i in range(M):
        minCost[i][0]=minCost[i-1][0]+grid[i][0]
    #INV at jth iteration first column upto j-1 th row of minCost have been given correct costs
    for j in range(N):
        minCost[0][j]=minCost[0][j-1]+grid[0][j]
    
    #INV at ith iteration minCost[i] stores the minimum cost to reach any point on the i-1th row from (0,0) 
    for i in range(M):
        #INV at j th iteration minCost[i][j] stores the minCost in travelling from (0,0) to (i-1,j-1)
        for j in range(N):
            minCost[i][j]=min(minCost[i-1][j],minCost[i][j-1])+grid[i][j]
        #post condition minCost has i rows storing the minimum cost to reach a point on the i-1th row from (0,0)
    #Since are final destination is (M,N)
    return minCost[M-1][N-1]

grid =[[8,1,6],[3,5,7],[4,9,2]]
print(gridPlay(grid))