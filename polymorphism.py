

class Students: # Parent Class
	def __init__(self, first, last):
		self.first = first
		self.last = last
		self.email = first.lower() + '.' + last.lower() + '@college.edu'

	def fullname(self): # Method to create full name
		return '{} {}'.format(self.first, self.last)

class Major(Students): # Child Class
	def __init__(self, first, last, major, focus):
		super().__init__(first, last)
		self.major = major
		self.focus = focus

class Advisor(Students):
	def __init__(self, first, last, students=None): #This adds student to advisor
		super().__init__(first, last)
		if students is None:
			self.students = []
		else:
			self.students = students

	def add_student(self, stud):
		if stud not in self.students:
			self.students.append(stud)

	def print_studs(self):
		for stud in self.students:
			print('-- ', stud.fullname())

# instances for major class
student_1 = Major('Eren', 'Jaeger', 'Titan', 'War titan')
student_2 = Major('Mikasa', 'Ackerman', 'Titan', 'Slayer')

adv_1 = Advisor('Hange', 'Zoe', [student_1])


print(student_1.email)

adv_1.print_studs()
