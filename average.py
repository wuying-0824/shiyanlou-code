N = int(input("how many numbers: "))
sum = 0
for i in range(1,N+1):
    numbers = float(input("pls enter number: "))
    sum +=numbers
average = sum/N
print("average is {:.2f}".format(average))
