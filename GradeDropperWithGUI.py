import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox 

class GradeDropper:
	assignmentList = []
	overallGrade = []

	def calculate():
		if GradeDropper.overallGrade[0] == GradeDropper.overallGrade[1]:
			GradeDropper.assignmentList.clear()
			return tkinter.messagebox.showerror(title="Error", message="Error: All assignments have a perfect score. I don't recomend dropping any assignment.") 
		
		assignmentsCalculated = []
		for assignment in GradeDropper.assignmentList:
			if type(assignment) != Assignment:
				raise GradeDropperExceptions.gradeNotAssignment()
			
			#overall_effect = round(float((GradeDropper.overallGrade[0] - assignment.numerator ) / (GradeDropper.overallGrade[1] - assignment.denominator)), 2)
			overall_effect = float((assignment.numerator ) / (GradeDropper.overallGrade[1]))
			
			assignment.overall_effect = overall_effect
			print(f"Grade overall_efect: {overall_effect}")
			
			assignmentsCalculated.append(assignment)
		bestComparison = None
		lastAssignment = None
		
		print(assignmentsCalculated)
		for assignment in assignmentsCalculated:
			print(f"Looking at {assignment.name} with a grade of {assignment.overall_effect}")
			if lastAssignment == None:
				lastAssignment = assignment
				bestComparison = assignment
			else:
				if assignment.overall_effect < lastAssignment.overall_effect:
					print(f"Is greater. Storing.")
					bestComparison = assignment
			lastAssignment = assignment

		previous_grade = round(((GradeDropper.overallGrade[0] / GradeDropper.overallGrade[1]) * 100), 2)
		after_grade = round((((GradeDropper.overallGrade[0] - bestComparison.numerator) / (GradeDropper.overallGrade[1] - bestComparison.denominator)) * 100), 2)
		print(bestComparison)
		print(f"The best assignment to drop is {bestComparison.name}, as it makes your grade go from {(GradeDropper.overallGrade[0] / GradeDropper.overallGrade[1]) * 100} to {bestComparison.overall_effect * 100}")
		tkinter.messagebox.showinfo(title="Summary", message=f"The best assignment to drop is {bestComparison.name}, as it makes your grade go from %{previous_grade} to %{after_grade}")
		return GradeDropper.assignmentList.clear()
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
	def __init__(self, name, numerator, denominator, grade=None, overall_effect=None):
		self.name = name
		self.numerator = numerator
		self.denominator = denominator
		self.grade = grade
		self.overall_effect = overall_effect

assignmentlist = []

window = tk.Tk()
window.title("Grade Dropper")
window.configure(bg='#0E1D2F')
window_width = 600
window_height = 400

# get the screen dimension
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
window.minsize(width=340, height=125)

main = tk.Frame(master=window, bg='#0E1D2F')
main.grid(row=0, column=0, padx=10, pady=10, sticky="W")

def delete_all():
	for item in assignmentlist:
		item[0].destroy()

	for item in assignmentlist:
		del item

	assignmentlist.clear()

def destroy_assignment(frame):
	this_assignment = None
	starting_index = 0
	for assignment in assignmentlist:
		if assignment[0] == frame:
			this_assignment = assignment
			break
		else:
			starting_index += 1
	print(this_assignment)
	print(starting_index)
	for frames_after in assignmentlist[starting_index + 1:]:
		frames_after[0].grid(row=frames_after[1] - 1)
		frames_after[1] -= 1
	assignmentlist.remove(this_assignment)
	frame.destroy()
	del frame

def create_assignment():
	assignment_frame = ttk.Frame(master=main)
	ttk.Label(master=assignment_frame, text="Assignment name:").grid(row=0, column=0, padx=(3, 0), pady=(3, 3))
	ttk.Entry(master=assignment_frame).grid(row=0, column=1, padx=(2, 0), pady=(3, 3))
	ttk.Label(master=assignment_frame, text="Grade:").grid(row=0, column=2, padx=(2, 0), pady=(3, 3))
	ttk.Entry(master=assignment_frame, width=5).grid(row=0, column=3, padx=(2, 0), pady=(3, 3))
	ttk.Label(master=assignment_frame, text="/").grid(row=0, column=4, padx=(2, 0), pady=(3, 3))
	ttk.Entry(master=assignment_frame, width=5).grid(row=0, column=5, padx=(2, 0), pady=(3, 3))
	ttk.Button(master=assignment_frame, text="Delete", command=lambda: destroy_assignment(frame=assignment_frame)).grid(row=0, column=6, padx=(2, 3), pady=(3, 3))
	
	row = len(assignmentlist) + 4
	assignment_frame.grid(row=row, column=0, pady=(5, 0))

	assignmentlist.append([assignment_frame, row])

	print(assignmentlist)
	#print(assignment_add_button)
	assignment_add_button.grid(row=len(assignmentlist) + 4, column=0, sticky="W")

def calculate():
	if len(assignmentlist) == 0:
		return tkinter.messagebox.showerror(title="Error", message="Error: No assignments have been created.")
	if len(assignmentlist) == 1:
		return tkinter.messagebox.showerror(title="Error", message="Error: You must have more than one assignment.")

	for item in assignmentlist:
		children = item[0].children
		print(children)
		assignment_name = children["!entry"].get()	
		numerator = round(float(children["!entry2"].get()), 2)
		denominator = round(float(children["!entry3"].get()), 2)

		GradeDropper.assignmentList.append(Assignment(assignment_name, numerator, denominator))
	GradeDropper.calculateOverallGrade()
	GradeDropper.calculate()

#top_elements = tk.Frame(master=main).grid(row=0, column=0, sticky="W")

ttk.Button(master=main, text="Calculate", command=lambda: calculate()).grid(row=0, column=0, sticky="W")
button2 = ttk.Button(master=main, text="Delete all assignments", command=lambda: delete_all()).grid(row=0, column=0, padx=(90, 0), sticky="W")

assignment_add_button = ttk.Button(master=main, text="Add new assignment", command=lambda: create_assignment())
assignment_add_button.grid(row=3, column=0, pady=(5, 0), sticky="W")

#ttk.Button(master=main, text="print", command=lambda: print(window.children)).grid(row=7, column=0, sticky="W")
window.mainloop()