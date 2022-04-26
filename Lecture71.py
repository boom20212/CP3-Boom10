menuList = []
priceList = []

def showBill():
    print("---------My Food-----------")
    for number in range(len(menuList)):
        print(menuList[number],priceList[number])

def total():
    total = 0
    for i in range(len(priceList)):
        total = total + int(priceList[i])
    print("total :",total,"THB")

while True:
    menuName = input("Please Enter Menu:")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price :")
        menuList.append(menuName)
        priceList.append(menuPrice)
showBill()
total()