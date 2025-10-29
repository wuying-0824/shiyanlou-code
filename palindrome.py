s = input("Enter a string: ").split()
print(s)
n = len(s)
a = []
for i in range(n):
    a.append(s[n-1-i])
print(a)
if a == s:
    print("the string is a palindrome")
else:
    print("the string is not a palindrome")

