#python programme to find largest of two numbers

a = float(input("Enter the first Number a :"))
b = float(input("Enter the Second Number b :"))

if (a > b):
    print("{0} is greater than {1}".format(a, b))
elif (b > a): 
    print("{0} is greater than {1}".format(b, a))
else:
    print("a and b are equal")
