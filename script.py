name = input("Enter the name: ")
grade = int(input("Enter the class: "))
mark1 = int(input("Enter marks of first subject: "))
mark2 = int(input("Enter marks of second subject: "))
total = mark1 + mark2
avg = (mark1 + mark2)/2
print(name,"of grade ", grade, "has scored ", total, "and percentage ",avg)
