class GradeDropper:
	assignmentList = []
	overallGrade = []
	
	def calculate():
		assignmentsCalculated = []
		for assignment in GradeDropper.assignmentList:
			if type(assignment) != Assignment:
				raise GradeDropperExceptions.gradeNotAssignment()
			
			grade = float((GradeDropper.overallGrade[0] - assignment.numerator ) / (GradeDropper.overallGrade[1] - assignment.denominator))
			assignment.grade = grade
			print(f"Grade: {grade}")
			
			assignmentsCalculated.append(assignment)
		bestComparison = None
		lastAssignment = None
		
		print(assignmentsCalculated)
		for assignment in assignmentsCalculated:
			print(f"Looking at {assignment.name} with a grade of {assignment.grade}")
			if lastAssignment == None:
				lastAssignment = assignment
				bestComparison = assignment
			else:
				if assignment.grade >= lastAssignment.grade:
					print(f"Is greater. Storing.")
					bestComparison = assignment
			lastAssignment = assignment
		print(bestComparison)
		print(f"The best assignment to drop is {bestComparison.name}, as it makes your grade go from {(GradeDropper.overallGrade[0] / GradeDropper.overallGrade[1]) * 100} to {bestComparison.grade * 100}")
	
	def calculateOverallGrade():
				totalNumerator = 0
				totalDenominator = 0
				for assignment in GradeDropper.assignmentList:
					print(assignment.numerator)
					print(assignment.denominator)
					totalNumerator += assignment.numerator
					totalDenominator += assignment.denominator
				GradeDropper.overallGrade = [totalNumerator, totalDenominator]
				print(f"Set the overall grade at {totalNumerator}/{totalDenominator}")
				
	def addAssignment(name, numerator, denominator):
				GradeDropper.assignmentList.append(Assignment(name, numerator, denominator, None))
				print("Added new assignment")
				
				
			
class GradeDropperExceptions(Exception):
	def gradeNotAssignment():
		print("Error: assignments must be created using the Assignment class.")
		exit(1)

class Assignment:
	def __init__(self, name, numerator, denominator, grade):
		self.name = name
		self.numerator = numerator
		self.denominator = denominator
		self.grade = grade

#GradeDropper.overallGrade = [37, 36]

#GradeDropper.addAssignment("assignment 1", 15, 15)1
#GradeDropper.addAssignment("assignment 2", 22, 21)
#GradeDropper.addAssignment("", , )

#GradeDropper.calculateOverallGrade()
#GradeDropper.calculate()

#main loop
running = True
print("This program is supposed to calculate what the best assignment to drop is based on how much it increases your grade. Made by King Tootsie.")
while running:
	assignment_name = str(input("Enter the name of the assignment (just press enter if done adding): "))
	if assignment_name == "":
		break
	numerator = int(input("Enter the number of points you got: "))
	denominator = int(input("Enter the max number of points: "))

	GradeDropper.addAssignment(assignment_name, numerator, denominator)
GradeDropper.calculateOverallGrade()
GradeDropper.calculate()

