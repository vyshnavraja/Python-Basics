# Original code with comments and alignment corrected

# t = (2, 3, 4, 5, [10, 20])
# print(t)

# list = []
# tuple = ()
# set = {}
# dis = {K:v}

a = input("Enter a number: ")
n = len(a)
arms = 0
for i in range(0, n):
    arms = arms + int(a[i])**n

if arms == int(a):
    print(a, 'is an Armstrong number')
else:
    print(a, 'is not an Armstrong number')

# 153, 407, 1634, 9474
