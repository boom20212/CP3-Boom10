usernameInput = input("Username :")
passwordInput = input("Password :")

if usernameInput == "123" and passwordInput == "456":
    print("Login Successfully")
    print("Welcome!")

    print("===== Ur Anus Shop =====")
    print("1. Apple 10 THB")
    print("2. Water 15 THB")

    userSelected = int(input("Please Select Item Number >>"))
    quantity = int(input("Amount :"))

    if userSelected == 1:
        item = "Apple"
        Price = 10*quantity
        total = print(Price)

    elif userSelected == 2:
        item = "Water"
        Price = 15*quantity
        total = print(Price)

        print("Your Product :", item, ":", Price, "THB" )

    else:
        print("Item not found")
        print("---------------")

else:
    print("Vaild Username or Password")

