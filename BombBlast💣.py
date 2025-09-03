def max_blast(grid,m):
    n = len(grid)
    mid = m//2
    max_effect = 0
    best = None
    destroyed_pts = []

    #checking all possible centres
    for i in range(n):
        for j in range (n):
            #no explosion
            if grid[i][j] ==0:
                continue

            c=0
            pts =[]
            for x in range(i-mid,i+mid+1):
                for y in range(j-mid,j+mid+1):
                    if 0<=x<n and 0<=y<n :
                        if grid[x][y] ==1:
                            c +=1
                            pts.append((y,n-1-x))

            if c > max_effect :
                max_effect = c
                best = (j,n-1-i)
                destroyed_pts = pts
    return max_effect , best,destroyed_pts

grid = [
    [1,1,0,0,0,1],
    [1,0,0,0,1,1],
    [1,0,0,1,1,0],
    [1,1,0,0,0,1],
    [1,0,0,0,1,1],
    [1,0,0,1,1,0]
]
m=3
dmg , best , dest = max_blast(grid,m)
print(f'The bomb is blasted on {best} with {dmg} coordinated destroyed at {dest}')

