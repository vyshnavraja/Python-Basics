a = int(input("Enter a number: "))  # 242
temp = a
rev = 0
while a > 0:
    rem = a % 10
    rev = rev * 10 + rem
    a //= 10
if temp == rev:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")
