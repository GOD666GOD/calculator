def plus (x, y, z):
    return(x + y + z)


def minus(x, y, z):#000000#000000#FF3131#000000#000000
    return(x - y - z)

def mnozenje(x, y, z):
    return(x * y * z)

def delenje(x, y, z):
    return(x / y / z)

print("Izberi operacijo. ")
print("1.Plus")
print("2.Minus")
print("3.Mnozenje")
print("4.delenje")

choice = input("Enter choice (1/2/3/4): ")

num1 = float(input("Enter first number:  "))
num2 = float(input("Enter second number:  "))
num3 = float(input("Enter third number:  "))

if choice == '1':
    print(num1, "+", num2, "+", num3, "=", plus(num1, num2, num3))

elif choice == '2':
    print(num1, "-", num2, "-", num3, "=", minus(num1, num2, num3))

elif choice == '3':
    print(num1, "*", num2, "*", num3, "=", mnozenje(num1, num2, num3))

elif choice == '4':
    print(num1, "/", num2, "/", num3, "=", delenje(num1, num2, num3))

else:
    print("invalid input")








