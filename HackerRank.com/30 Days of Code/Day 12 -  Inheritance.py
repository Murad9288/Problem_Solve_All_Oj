class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNumber,scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores
        
    def calculate(self):
        sum = 0
        for i in range(len(self.scores)):
            sum += self.scores[i]
        avarage = sum // len(self.scores)
        if avarage >= 90 and avarage <= 100:
            return "O"
        elif avarage >= 80 and avarage < 90:
            return "E"
        elif avarage >= 70 and avarage < 80:
            return "A"
        elif avarage >= 55 and avarage < 70:
            return "P"
        elif avarage >= 40 and avarage < 55:
            return "D"
        elif avarage < 40:
            return "T"
        
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
