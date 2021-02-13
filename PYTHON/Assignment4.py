#1 
def readNumber(s,i):
    n=i
    num=""
    # checks if the number at ith index is negative
    if s[n]=='-':
       num='-'
       n+=1
    #reads number at ith index
    #INV at nth iteration num stores s[i]+s[i+1]...s[n]
    # such that s[i],..s[n-1] all are either digits or one is decimal
    while(n<len(s)):
        if s[n] != "(" and s[n] != ")" and s[n] != "+" and s[n] != "-" and s[n] != "*" and s[n] != "/":
            num+=s[n]
            n+=1
        else:
            break
    #post condition s[n] is either a bracket or a operator
    #num stores s[i]+s[i+1]...s[n]
    return (float(num),n)


def evalParen(s,i):
    (n1,i1)=readNumber(s,i+1)
    (n2,i2)=readNumber(s,i1+1)
    if s[i1]=="+":
        return (n1+n2,i2+1)
    elif s[i1]=="-":
        return (n1-n2,i2+1)
    elif s[i1]=="*":
        return (n1*n2,i2+1)
    elif s[i1]=="/":
        return (n1/n2,i2+1)
    


def evaluate(s):
    #Recursion Invariant- If string 's' has 'x' sets of '(',')'
    #then in the next recursion step there will be 'x-1' sets of brackets.
    s1=""
    t=True
    a=0
    #checks if the string s has no paranthesis 
    #pre condition t=True by default
    #INV at ith iteration none of s[0],s[1]...s[i1] is "(" 
    for i in range(0,len(s)): #1
        if s[i]=="(":
            t=False
            break
    #Post condition i=n(<len(s)) such that s[i]="(" or i>=length(s) and there are no paranthesis in 's'
   
    if t:
        (n,i)=evalParen("("+s+")",0)
    else:
        #loop creates a string s1 =s with one difference, the innermost paranthesis is solved
        #INV at ith iteration s[0],s[1],...s[i-1] is not equal to ")"
        for i in range(0,len(s)): #2
            if s[i]==")":
                for j in range(i,-1,-1): #3
                    if s[j]=="(":
                        a=j
                        break
                #adds the terms from starting to "(" of s to s1
                #INV at kth iteration s1=s1+s[0]+..s[k-1]
                for k in range(0,a): #4
                    s1+=s[k]
                (n1,i1)=evalParen(s,a)
                s1+=str(n1)
                #adds the rest of the terms to s1
                #INV at lth iteration that s1=s1+s[i+1]+...s[l-1]
                for l in range(i+1,len(s)): #5
                    s1+=s[l]
                break
    
        n=evaluate(s1)
    return n

print(evaluate("1+(((123*3)-69)/100)"))



#2
def binarySearch1(l1,left,x):
    low=left
    high=len(l1)-1
    c=0
    #INV element 'x' is in l[low:high] and 0<=low<=high<=length(l)
    #pre condtion low=left, right=index of last element
    while(low<=high):
        mid=(low+high)//2
        
        if l1[mid]==x:
           c=1
           break
            
        elif l1[mid]>x:
            high=mid-1
        else:
            low=mid+1
    #post condition element x is not in the l[left:length(l)] otherwise the function would have returned 1
    return c

  
def sumOfTwo(n,l,x):
    counter=0
    # calculates the number of ways('counter') 'n' can be expressed as sum of two terms of the list
    #pre condition counter=0 x=length(l)
    #INV at ith iteration counter stores the number of ways 'n' can be expressed 
    #as sum of two terms in [l0,l1,...l{i-1}] and [l{i},...lx]
    for i in range(0,x-1):
        temp=n-l[i]
        counter+=binarySearch1(l,i+1,temp)
        if counter>1:
            return False
        
    #post condition i=len(l) counter=number of ways 'n' can be expressed as sum of two terms of the list
  
    if counter==1:
        return True
    else:
        return False


def sumSequence(n):
    #we already know the first and second term of the sequence
    if n==1:
        return [1]
    elif n==2:        
        return [1,2]
    else:
        l=[1,2]
        i=3
        c=2
    #to calculate the sequence of 'n' terms 'c' is the length of the list during each iteration
    #pre condition i=3, l=[1,2]
    #INV at (i)th iteration 'l' consists of 'c' elements (c<n) following the pattern as in the question
        while c<n:
            if sumOfTwo(i,l,c):
                l.append(i)
                c+=1
            i+=1
    #post condition 'l' is a  length 'n' list following the unique sum property         
    return l


print(sumSequence(206)[-1])


#3
def minLength(a,n):
    
    l=len(a)
    min=l+1
    #calculates the number of ways a sublist can be chosen wih the sum of its terms greater than n
    #pre condition min=l+1, t=True
    #INV min stores the minimum length of all sublists of list a[0:i] such that sum of their elements is greater than 'n'
    for i in range(0,l):
        c=0
        s=0

        #INV s stores the sum of elements(c) of list 'a' from index i to j-1 and s<n
        for j in range(i,l):
            s+=a[j]
            c+=1
            if s>n:
                t=True
                break
            else:
                t=False
            
        # if there exists such sublist with length(c)<min then min=c
        if t and c<min:
            min=c
        #post condition min=minimum length of sublist can be chosen wih the sum of its terms greater than n. If no such 
        #sublist exists min=length(l)+1
            
    if min!=l+1:     
     return min
    else:
        return -1

print(minLength([3,1,1,0], 2))



#4
#standard mergeSort algorithm
def mergeAB(arr,b,l,m,r):
    i=l
    j=m
    k=l
    while(i<m and j<r):
        (a,x)=arr[i]
        (c,y)=arr[j]
        if a<=c:
            b[k]=arr[i]
            i+=1
        else:
            b[k]=arr[j]
            j+=1
        k+=1

    while i<m:
        b[k]=arr[i]
        i+=1
        k+=1
    while j<r:
        b[k]=arr[j]
        j+=1
        k+=1
        
def mergeIt(A,B,n,I):
    if n%I==0:
        count=n//I
    else:
        count=n//I+1
    for i in range(count//2):
        left=i*I*2
        right=min(left+2*I,n)
        mergeAB(A,B,left,left+I,right)

        for i in range(right,n):
            B[i]=A[i]

def mergeSort(A):
    n=len(A)
    I=1
    B=[("","") for x in range(n)]
    dir=0
    while I<n:
        if dir==0:
            mergeIt(A,B,n,I)
            dir=1
        else:
            mergeIt(B,A,n,I)
            dir=0
        I*=2
    
    if dir==1:
        for i in range(n):
            A[i]=B[i]


def binarySearch(l,left,right,x):
    low=left
    high=right
    answer=-1
    #calculates last occurence of 'n'
    #INV element 'x' is in l[left:right] and 0<=left<=right<=length(l)
    #pre condtion low=left, right=index of last element
    while(low<=high):
        mid=(low+high)//2
        (n1,e1)=l[mid]
        if n1==x:
            answer=mid
            low=mid+1
        elif n1>x:
            high=mid-1
        else:
            low=mid+1
   
    return answer


def mergeContacts(l):
    mergeSort(l)
    finalL=[]
    i=0
    x=len(l)
    #INV all unique people in l[0:i] have their emails combined in finalL
    #and their mail list and name is appended to finalL list.
    #precondition finalL=[] x=length(l) i=0
    while(i<x):
        (n,e)=l[i]
        c=0
        finalMail=[]
        upper=binarySearch(l,i,x-1,n)
        #combines email=id of all people named n
        #INV finalMail stores email-id of people in l[i,j]
        for j in range(i,upper+1):
            (n1,e1)=l[j]
            finalMail.append(e1)
        #finalL contains the tuples of people and their merged emails
        finalL.append((n,finalMail))
        i=upper+1
        
    return finalL

print(mergeContacts([("RN","narain@cse"), ("HS","saran@cse"), ("RN","Rahul.Narain@iitd"),("HS","asd")]))