#all coding for both classes LowScores and HighScores done by Daniel Cook


class LowScores:

	def _init_(self,grades):
		self.grades = grades
#initializes variables
	def highest(list):
		high_index = 0
		for i in range(0, len(list)):
			if list[i] > list[high_index]:
				high_index = i
		return high_index
#finds index of highest number in a list
	def weakest_subject(self):
		num_tests = len(self.grades)
		thirdOf = num_tests // 3
		if thirdOf == 0:
			thirdOf = 1
		listOfGrades = []
		listOfSubjects = []
		for key in self.grades:
			listOfGrades.append(self.grades[key])
			listOfSubjects.append(key)
			if len(listOfSubjects) >thirdOf:
				indexToRemove = highest(listOfSubjects)
				listOfGrades.remove(listOfGrades[indexToRemove])
				listOfSubjects.remove(listOfSubjects[indexToRemove])
		return listOfSubjects
#returns list of weakest subjects

class HighScores:

	def _init_(self,grades):
		self.grades = grades
#initializes variables
	def lowest(list):
		low_index = 0
		for i in range(0, len(list)):
			if list[i] < list[low_index]:
				low_index = i
		return low_index
#finds index of lowest number in a list
	def best_subject(self):
		listOfGrades = []
		listOfSubjects = []
		for key in self.grades:
			listOfGrades.append(self.grades[key])
			listOfSubjects.append(key)
			if len(listOfSubjects) > 1:
				indexToRemove = lowest(listOfSubjects)
				listOfGrades.remove(listOfGrades[indexToRemove])
				listOfSubjects.remove(listOfSubjects[indexToRemove])
		return listOfSubjects[0]
#finds the students best subject



print("hello %s\n",name)
    # a user interface that can type a letter 
    # after typeing a letter it will redirect it to the method that
    # you want to run. 
print("type a letter for what you would like to do?\n")
print("Find your best subject \t 'N' or 'n'\n")
print("find your weakest subjects\t 'L' or 'l'\n")
print("quit program\t 'Q' or 'q'\n")
    
a = str(input("enter the letter: " ))
#print(subject)

if ((a == 'N') or (a== 'n')):
    HighScores.best_subject()
if ((a == 'L') or (a== 'l')):
    LowScores.weakest_subject()
if ((a == 'Q') or (a== 'q')):
    exit()
}
print("welcome to the gradeing system.\n");
print("\n");
g = raw_input("Enter the subject(what class is it?) :",subject ) 
print name
g = raw_input("Enter your grade : Ex: 88",grade)

