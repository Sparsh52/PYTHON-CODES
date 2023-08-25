class Person:
    def __init__(self,name,duty) -> None:
        self.name=name
        self.duty=duty
    def printPerson(self):
        print("Name is"+" "+self.name+" "+"duty is"+" "+self.duty)


li=[]
for i in range(5):
    print("Enter the Name of Person")
    name=input()
    print("Enter The duty")
    duty=input()
    p=Person(name,duty)
    li.append(p)
for p in li:
    p.printPerson()
