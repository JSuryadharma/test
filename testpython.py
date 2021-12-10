class sallyOne:

    gbArray = []

    def __init__(self):
        self.value = 10
        self.second = 20
        self.arrayList = ["Test", "Satu", "Dua", "Tiga"]

    def callSallyTwo(self):
        obj = sallyTwo(self)
        obj.printValue()

    def addGbArray(self):
        self.gbArray = ["Test"]
        print(self.gbArray)

class sallyTwo:
    def __init__(self, ref):
        self.ref = ref

    def printValue(self):
        print(self.ref.value)
        # self.ref.arrayList = ["Testy"]
        self.changedArray = self.ref.arrayList
        self.changedArray = ["Amanda"]
        print(self.ref.arrayList)

    def checkGbArray(self, gbArray):
        sallyOne.gbArray = gbArray
        print(sallyOne.gbArray)
        sallyOne.gbArray = ["Ini", "dari", "sallyTwo"]
        print(sallyOne.gbArray)

class sallyThree:
    arrayList = ["Sally"]

    def cetak(self):
        print(self.arrayList)

class sallyFour:
    def action(self):
        # sallyThree.arrayList = ["One", "Two"]
        print(sallyThree.arrayList)

if __name__ == "__main__":
    obj1 = sallyOne()
    # obj1.addGbArray()
    obj1.addGbArray()
    # print(obj1.arrayList)
    # obj1.addGbArray()
    obj2 = sallyTwo(obj1)
    obj2.checkGbArray(obj1.gbArray)
    print(obj1.gbArray)
    # obj3 = sallyThree()
    # obj3.cetak()
    # obj4 = sallyFour()
    # obj4.action()
    # obj3.cetak()
    # obj5 = sallyThree()
    # obj5.cetak()