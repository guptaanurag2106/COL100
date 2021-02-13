class Student:                          
    def __init__(self,str1,list1):            #takes as input entryno. and list of courses
        self.entryNo = str1
        self._listOfCourse = list1.copy()        #created copy so that original list is intact
        temp1=[]                       #this will store list of tuple having name of course and a quiz title
        for i in self._listOfCourse: #inv is for every i temp will have tuple of course and quizes till that i course
            for j in i.ListOfQuiz(): #inv is after j temp will have tuple of course and quizes till j
                temp1.append((i.courseCode,j.title))
        self._QuizToAttend=temp1   #list as mentioned above
        
        courseCodeQuiztoQuiz={}        #key is code, quiztitle value is quiz
        
        for i in self._listOfCourse:
            for j in i.ListOfQuiz():
                courseCodeQuiztoQuiz[(i.courseCode,j.title)]=j
        self._courseCodeQuiztoQuiz=courseCodeQuiztoQuiz    #this is a dictionary which maps each tuple of _QuizToAttend to the specific quiz(of class quiz)
        
        grades={}
        for i in self._listOfCourse:
            grades[i.courseCode]=(0,)
        self.grades= grades     #this will map each course to the scores of subsequent quizzes, initially all have been mapped to a tuple having 0 so that it becomes easier to add later scores in this tuple 
    

    def attempt(self, courseCode, quizTitle, attemptedAnswers):    #this is th attempt method which is as asked in question
        i=0
        quiz= self._courseCodeQuiztoQuiz[(courseCode,quizTitle)]   #using our dictionary to figure out which quiz we are talking about 
        for i in range(len(self._QuizToAttend)):
            if self._QuizToAttend[i]==(courseCode,quizTitle):
                self.grades[courseCode]=self.grades[courseCode]+(quiz.scoring(attemptedAnswers),)    #this adds the score of this quiz(using method defined in quiz)
                self._QuizToAttend.pop(i)    #removing this quiz from the list of Quizzes to attempt
                break
    
    def getUnattemptedQuizzes(self):
        return self._QuizToAttend    #returns required list as asked in question
    def getAverageScore(self, courseCode):
        x=0
        if len(self.grades[courseCode])==1:  #this will check if the length of the tuple in the grade dictionary is 1 which means no quiz has been attempted 
            return x
        else:
            for i in self.grades[courseCode]:  #this will sum up the scores of attempted quizzes  
                x+=i 
            return x/(len(self.grades[courseCode])-1)    #-1 because of the extra 0 i used to initialize the tuple in the dictionary




class Quiz:
    def __init__(self,title,ListOfCorrectAns):        #takes as input title of quiz and list of correct answers
        self.title=title
        self._correctOptions= ListOfCorrectAns.copy()   #created copy so that original list remains intact 
    def scoring(self,attemptedAns):     # this is a method i defined which will basically take as input the list of attempted answers by the student and returns the score
        score=0
        for i in range(len(attemptedAns)):
            if self._correctOptions[i]==attemptedAns[i]:       #checking with the list of correctanswers and increasing score accordingly
                score+=1
        return score      
       


class Course:
    def __init__(self,str1,list1):             #takes as input the name of the course and the list of quizzes it has
        self.courseCode= str1
        self._ListOfQuiz= list1.copy()       #creating copy so that orgignal lit remains intact
    def ListOfQuiz(self): #this method return a copy of the list of quiz as it an private attribute and should not be modified outside this class
        x= self._ListOfQuiz.copy()   
        return x

col100q1 = Quiz('Quiz1', ['a','b','b'])
col100q2 = Quiz('Quiz2', ['b','d','c'])
col100 = Course('COL100', [col100q1, col100q2])
mtl100q1 = Quiz('Quiz1', ['a','b','d'])
mtl100q2 = Quiz('Quiz2', ['d','c','a'])
mtl100 = Course('MTL100', [mtl100q1, mtl100q2])
s1 = Student('2019MCS2562', [col100, mtl100])
s2 = Student('2017CS10377', [col100])
s2.attempt('COL100', 'Quiz1', ['a','b','c'])

print(s2.getUnattemptedQuizzes())
print(s2.getAverageScore('COL100'))

print(.1+.1+.1+.1+.1+.1+.1+.1+.1+.1)
y=0
for i in range(10):
    y+=10*.1
print(y/10)

# Python program for implementation of Insertion Sort 

# Function to do insertion sort 
def insertionSort(arr): 

	# Traverse through 1 to len(arr) 
	for i in range(1, len(arr)): 

		key = arr[i] 

		# Move elements of arr[0..i-1], that are 
		# greater than key, to one position ahead 
		# of their current position 
		j = i-1
		while j >= 0 and key < arr[j] : 
				arr[j + 1] = arr[j] 
				j -= 1
		arr[j + 1] = key 


# Driver code to test above 
arr = [12, 11, 13, 5, 6] 
insertionSort(arr) 
for i in range(len(arr)): 
	print ("% d" % arr[i]) 

# This code is contributed by Mohit Kumra 
