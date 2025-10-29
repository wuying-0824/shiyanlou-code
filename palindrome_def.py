def palindrome(s):
    return s == a
if __name__ == '__main__':
    s = input("Enter a string: ").split()
    n = len(s)
    a = []
    for i in range(n):
        a.append(s[n-1-i])
    if palindrome(s):
        print("is a palindrome")
    else:
        print("not a palindrome")
