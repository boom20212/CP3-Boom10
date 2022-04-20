number1 = int(input("First Number :"))
number2 = int(input("Second Number :"))
def addNumber(x,y):
    print(number1, "+", number2, "=", x+y)
    print(number1, "-", number2, "=", x-y)
    print(number1, "*", number2, "=", x*y)
    print(number1, "/", number2, "=", x/y)
addNumber(number1,number2)