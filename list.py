class student():
  def __init__(self,name,roll,cgpa):
       self.name=name
       self.roll=roll
       self.cgpa=cgpa

def sortcgpa(sortlist):
  sortedstu=sorted(sortlist, key=lambda x: x.cgpa, reverse=True)
  return sortedstu

stuobj=[student("Kalaiselvan","22CS2114",8.9),student("Yogesh","22CS2115",8.5),student("Vijay","22CS2116",6.3),student("Vikram","22CS2117",9.8)]
sortedstu=sortcgpa(stuobj)

for stu in sortedstu:
  print(f"Name: {stu.name}   Roll.no: {stu.roll}    CGPA: {stu.cgpa}")