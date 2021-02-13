def isSafe(maze,x,y):
    if x>=0 and y>=0 and x<len(maze) and y<len(maze[0]):
        if not maze[x][y] =='X':
            return True
    else:
        return False

def maze1(maze,start,end):
    visited=[[False for j in range(len(maze[0]))] for i in range(len(maze))]
    s=[]
    l=[start]
    while(len(l)!=0):
        
        (x,y)=l[-1]
        visited[x][y]=True
        if (x,y)==end:
            return s
        if isSafe(maze,x,y-1) and not visited[x][y-1]:
            s+='L'
            l.append((x,y-1))
        elif isSafe(maze,x,y+1) and not visited[x][y+1]:
            s+='R'
            l.append((x,y+1))
        elif isSafe(maze,x+1,y) and not visited[x+1][y] :
            s+='D'
            l.append((x+1,y))
        elif isSafe(maze,x-1,y) and not visited[x-1][y] :
            s+='U'
            l.append((x-1,y))
        else:
            s.pop()
            l.pop()
            (a,b)=l[-1]
            
    return []

def traverseMaze():
    file1=open("mazeFile.txt","r")
    maze=file1.readlines()
    m2=[]
    a=0
    b=0
    c=0
    d=0
    for i in range(len(maze)):
        m1=[]
        for j in range(len(maze[i])-1):
            if maze[i][j]=='X' or maze[i][j]=='S' or maze[i][j]=='E' or maze[i][j]=='_':
                m1.append(maze[i][j])
                if maze[i][j]=='S':
                    a=i
                    b=len(m1)-1
                elif maze[i][j]=='E':
                    c=i
                    d=len(m1)-1
        m2.append(m1)

    start=(a,b)
    end=(c,d)
    print(maze1(m2,start,end))

traverseMaze()

