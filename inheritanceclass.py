class Schoolmembers():
    def __init__(self,name,lastname,id):
        self.name=name
        self.lastname=lastname
        self.id=id
    
    def display2 (self):
        print(self.name)
        print(self.class_num)

class Teacher (Schoolmembers):
    def __init__(self,name,lastname,id,Teacher_num,teach):
        self.Teacher_num=Teacher_num
        self.teach=teach
        Schoolmembers.__init__(self,name,lastname,id)
    def display(self):
        print(self.name)
        print(self.Teacher_num)
    

        


class Student (Schoolmembers):
    def __init__(self,name,lastname,id,Student_num,class_num):
        self.Student_num=Student_num
        self.class_num=class_num
        Schoolmembers.__init__(self,name,lastname,id)

    def display(self):
        print(self.name)
        print(self.class_num)
    

obj_1=Teacher('Ali','shakoori',1111,3,'olooom')
obj_1.display()
obj_2=Student("amir","lesani",2222,4,384)
obj_2.display2()
