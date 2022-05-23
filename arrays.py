LotR = ["Bilbo", "Frodo", "Gandalf", "Sam", "Gollum"]
#setting up the elements of the list
print(len(LotR))
#determines how many elements there are
#Finds out the LENGTH of the array
print(max(LotR))
#Last(highest) in alphebetical order
print(min(LotR))
#First(lowest) in alphebetical order
LotR.append("Sam")
print(LotR)
#Adds another "Sam" to the end of the array
print(LotR.count("Sam"))
#Counts how many times "Sam" appears in array
print(LotR.index("Sam"))
#prints what index "Sam" has
LotR.remove("Sam")
print(LotR)
#Thisremoved the first "Sam" in the array
LotR.insert(2, "Legolas")
print(LotR)
#This added "Legolas" in the number 2 spot
LotR.sort()
#It sorts the array
LotR.reverse()
#reverses the entire list
print(LotR)