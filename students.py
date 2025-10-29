n = int(input("Enter the number of students: "))
subject = ('Physics', 'Maths', 'History')
marks = []
data = {}
for i in range(0, n):
    name = input("Enter the name of students{}: ".format(i+1))
    for x in subject:
        marks.append(int(input("Enter the marks of {}: ".format(x))))
    data[name] = marks
for x, y in data.items():
    total = sum(y)
    print("student {}'s total marks {}: ".format(x, y))
    if total < 120:
        print("student {} failed".format(x))
    else:
        print("student {} passed".format(x))
