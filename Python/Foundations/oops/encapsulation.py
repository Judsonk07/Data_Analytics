# class student:
#     def __init__(self,attendance):
#         # self.name = name
#         self._attendance = attendance
#         #protect
#         # 0 to 100
#     def get_attendance(self):
#         return self._attendance
#         #When needed, display
#     def set_attendance(self,value):
#         if 0<=value<=100:
#             self._attendance = value
#         else:
#              raise ValueError("Enter valid attendance ranging from 0 to 100")

#     # def display(self):
#     #     return f"Student Name: {self.name}\nAttendance: {self.attendance}%"

# std1 = student(90)
# std1.set_attendance = 200
# print(std1.attendance)



class Student:
    university="Nova University"
    def __init__(self,name,id,dept,marks,attendance):
        self.name=name
        self.id=id
        self.dept=dept
        self._marks=marks
        self._attendance=attendance

    # Getter
    def get_marks(self):
        sum_=0
        for mark in self._marks:
            sum_=sum_+mark
        self.average=sum_/len(self._marks)
        cgpa = self.average / 10
        return round(cgpa, 2)

    # Setter
    def set_marks(self,marks):
        self._marks=marks

'''
Name
id
dept
Marks
Attendance
'''

std1=Student("Pranav","CS101","CSE",[89,90,78],0)
std2=Student("Lokesh","CS102","CSE",[99,88,95],0)
std3=Student("Subha","CS103","CSE",[90,80,70],0)
st4=Student("Sanjay","CS104","CSE",[80,70,60],0)
st5=Student("Karthi","CS105","CSE",[70,60,50],0)


print(std1.get_marks())
print(std2.name, std2.id, std2.dept,"CGPA:",std2.get_marks())
print(std3.get_marks())
print(st4.name, st4.id, st4.dept,"CGPA:",st4.get_marks())
print(st5.get_marks())