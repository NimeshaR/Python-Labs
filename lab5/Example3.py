#python programme to find smallest of three numbers 

a = int(input('Enter the first number a :'))
b = int(input('Enter the second number b :'))
c = int(input('Enter the third number c :'))

smallest = 0

if a < b and a < c:
    smallest = a
elif b < c:
    smallest = b
else:
    smallest = c

print("The smallest number is", smallest)
