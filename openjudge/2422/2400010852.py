def f(n,m,s):
    temp=[]
    for i in s:
        if i==' ':
            k=0
        else:
            k=ord(i)-64
        for j in range(5):
            temp.append(k%2)
            k=k//2
    temp=temp[::-1]
    matrix=[[0]*m for _ in range(n)]
    flag = [[False] * m for _ in range(n)]
    path=[0,-1]
    directions=[[0,1],[1,0],[0,-1],[-1,0]]
    q=0
    for i in range(len(temp)):
        nx,ny=path[0] + directions[q][0],path[1]+directions[q][1]
        if not (0<=nx<=n-1 and 0<=ny<=m-1 and flag[nx][ny]==False ):
            q=(q+1)%4
            nx,ny= path[0] + directions[q][0], path[1] + directions[q][1]
        matrix[nx][ny]=temp[i]
        flag[nx][ny]=True
        path[0],path[1]=nx,ny
    output=''
    for i in range(n):
        for j in range(m):
            output=output+str(matrix[i][j])
    return output
l=list(map(str,input().split(maxsplit=2)))
n,m,s=l[0],l[1],l[2]
n,m=int(n),int(m)
s=s[::-1]
print(f(n,m,s))
