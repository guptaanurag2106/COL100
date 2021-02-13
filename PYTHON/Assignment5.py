#1
def gridPlay(grid):
    M=len(grid)
    N=len(grid[0])
    #initialize all elements of minPenalty list as 0
    minPenalty=[[0 for i in range(N)] for j in range(M)]

    #minPenalty for border points is the sum of penalties along the border
    #INV at ith iteration, minPenalty[i][0] contains the correct minimum penalties to reach the first row ith column
    for i in range(M):        #1
        minPenalty[i][0]=minPenalty[i-1][0]+grid[i][0]
    #INV at jth iteration, minPenalty[0][j] contains the correct minimum penalties to reach the first column jth row
    for j in range(N):        #2
        minPenalty[0][j]=minPenalty[0][j-1]+grid[0][j]
    
    #INV at ith iteration minPenalty[i] stores the minimum cost to reach any point on the i-1th row from (0,0) 
    for i in range(1,M):      #3
        #INV at j th iteration minPenalty[i][j] stores the minPenalty in travelling from (0,0) to (i-1,j-1)
        for j in range(1,N):  #4
            minPenalty[i][j]=min(minPenalty[i-1][j],minPenalty[i][j-1],minPenalty[i-1][j-1])+grid[i][j]
       
    #Since are final destination is (M,N)
    return minPenalty[M-1][N-1]

grid =[[8,1,6],[3,5,7],[4,9,2]]
print(gridPlay(grid))


#2
def stringProblem(str1, str2):
    m=len(str1)
    n=len(str2)
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]
    #vorc1 and vorc2 stores 1 for a vowel 0 for a consonant in str1 and str2 respectively
    vorc1=[]
    vorc2=[]

    #INV at ith iteration vorc1 has i-1th entries, consisting of 1 if the corresponding entry in
    #str1 is vowel hence is 0
    for c in str1:           #1
        if c=='a' or c=='e' or c=='i' or c=='o' or c=='u':
            vorc1.append(1)
        else:
            vorc1.append(0)

    #INV at jth iteration vorc1 has j-1th entries, consisting of 1 if the corresponding entry in
    #str2 is vowel hence is 0
    for c in str2:            #2
        if c=='a' or c=='e' or c=='i' or c=='o' or c=='u':
            vorc2.append(1)
        else:
            vorc2.append(0)

    #INV at the ith iteration dp[i] consists of minimum number of ways to convert str1[0:i] to str2
    #which can be of all length 0 to n.
    for i in range(m + 1):     #3
        #INV at the ith iteration dp[i][j] consists of minimum number of ways to convert str1[0:i] to str2[0:j]
        for j in range(n + 1): #4
            #if str1 is null and str2 is of length j then we need to add j elements in str1 
            if i == 0:
                dp[i][j] = j
            #if str2 is null and str1 is of length j then we need to remove j elements in str1 
            elif j == 0:
                dp[i][j] = i

            #if the last characters in the two strings are the same then appende in them are
            #equal to appends if we ignore their last characters
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
 
            else:
                if vorc1[i-1] and not vorc2[j-1]:
                    dp[i][j] = 2 +min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
                                    
                else:
                    dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
    
    #since final strings to be compared are of length 'm' and 'n' respectively
    return dp[m][n]
 
print(stringProblem("bplpcd", "apple"))


#3
nonlp=[31,28,31,30,31,30,31,31,30,31,30,31]
lp=[31,29,31,30,31,30,31,31,30,31,30,31]
#checks if the year 'y' is leap year or not
def leapYear(y):
    t= (y%4==0 and (y%400==0 or y%100!=0))
    return t

#creates a list of the first day of every month of a particular year 'y'
def firstDayM(y):
    t=leapYear(y)
    count=0
    #find the first day of the year
    for i in range(1753,y):
        if leapYear(i):
            count+=1
    d=((y-1753)+count)%7
    L=[d]
    #finds the first day of the rest of the months in year 'y'
    for m in range(2,13):
        c=0
        for i in range(1,m):
            if not t:
                c+=nonlp[i-1]
            else:
                c+=lp[i-1]
        L.append((d+c)%7)
    return L

#returns month name, with correct spaces, for month index 'm'
def month(m):
    if m==1:
        return "     -JANURARY-        "
    elif m==2:
        return "    -FEBRUARY-        "
    elif m==3:
        return "   -MARCH-"
    elif m==4:
        return "      -APRIL-          "
    elif m==5: 
        return "     -MAY-         "
    elif m==6:
        return "      -JUNE-"
    elif m==7:  
        return "       -JULY-          "
    elif m==8:
        return "    -AUGUST-        "
    elif m==9:
        return "    -SEPTEMBER-"
    elif m==10:
        return "     -OCTOBER-      "    
    elif m==11:
        return "      -NOVEMBER-    "
    elif m==12:
        return "       -DECEMBER-"

#returns a string of the lth row of the calendar of year 'y' month 'm'
def printMonth(y,m,l):
    day1=firstDayM(y)[m-1]
    ld=""
    if l==0:
        ld=month(m)
    elif l==1:
        ld=" M  T  W  T  F  S  S "
    elif l==2:
        for i in range(day1):
            ld+="   "
        for i in range(len(ld)//3+1,8):
            ld+=" "+str(i-day1)+" "
    else:
        d1=(l-3)*7+8-day1
        for i in range(d1,d1+7):
            if (leapYear(y) and i>lp[m-1]) or (not leapYear(y) and i>nonlp[m-1]):
                ld+="   "
            elif i>=10:
                ld+=str(i)+" "
            else:
                ld+=" "+str(i)+" "
    return ld

#writes strings from the printMonth function onto the txt file Calendar.txt
def printCalendar(year):
    file1=open("Calendar.txt","w+")
    y=str(year)
    file1.write(y.center(66)+"\n\n")
    for i in range(4):
        for j in range(8):
            file1.write(printMonth(year,3*i+1,j)+"   "+printMonth(year,3*i+2,j)+"   "+printMonth(year,3*i+3,j))
            file1.write("\n")
        file1.write("\n")   
    file1.close()   
     
printCalendar(2021)




