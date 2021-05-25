from classes import Person

p1 = Person("Tom","Smith",170, 78)
p2 = Person("Marta","Smith",150, 58)
p3 = Person("Chris","Smith",100, 28)
p4 = Person("Adam","Smith",70, 18)
p5 = Person("Ben","Smith",178, 88)

list_people=[]
list_people.append(p1)
list_people.append(p2)
list_people.append(p3)
list_people.append(p4)
list_people.append(p5)

for i in list_people:
  print(i.first_name)
