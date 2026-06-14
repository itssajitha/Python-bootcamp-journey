class student:
   def __init__(self,name,age,marks):
     self.name=name
     self.age=age
     self.marks=marks
   
   def display(self):
     print("name:",self.name)
     print("age:",self.age)
     print("marks:",self.marks)
     
s1=student("saji",18,40)
s2=student("binu",22,60)
   
s1.display()
s2.display()
   
   