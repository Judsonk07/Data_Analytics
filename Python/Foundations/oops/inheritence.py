from abc import ABC,abstractmethod
class Person(ABC):                   #  Super Class (Parent Class)
    def __init__(self,name,email):
        self.name = name
        self.email = email
    @abstractmethod
    def display_role(self):
        return "University Person"
    @abstractmethod
    def display_dashboard(self):
         pass

class Student(Person):          # Sub Class (Child Class)
    def __init__(self,name,email,dept):
        super().__init__(name,email)
        self.dept = dept
    def display_role(self):
            return "Student"
    def display_dashboard(self):
             return "Student Dashboard"

class Teacher(Student):          # Sub Class (Child Class)
    def __init__(self, name, email, dept,subjects):
        super().__init__(name, email, dept)
        self.subjects = subjects
    def display_role(self):
            return "Teacher"
    def display_dashboard(self):
             return "Teacher Dashboard"

std1 = Student("Judson","xyz@gmail.com","cse")
# print(std1.display_role())

people = [
     Student("judson","juddu@gmail.com","AI"),
     Teacher("Ragul","ragul@gmail.com","cs",["CS","AI"])
]

# for person in people:
#     print (person.display_role())


class HOD(Person):
     def __init__(self, name, email):
          super().__init__(name, email)
     def display_role(self):
          return super().display_role()
     def display_dashboard(self):
              return super().display_dashboard()


hod1 = HOD("hod","email")
print(hod1.display_dashboard())