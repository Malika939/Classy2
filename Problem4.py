class Student:
    def __init__(self, name, lastname, department, year_of_entrance):
        self.name = name
        self.lastname = lastname
        self.department = department
        self.year_of_entrance = year_of_entrance
    
    def get_student_info(self):
        return f'{self.name} {self.lastname} поступил в {self.year_of_entrance} году на факультет: {self.department}'

s = Student('Вася', 'Иванов','Программист', 2021) 
print(s.get_student_info())   
