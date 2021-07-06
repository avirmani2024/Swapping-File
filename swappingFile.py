from os import read


def swapFileData():
    fileName = input("Enter the File Name:")
    fileName2 = input("Enter the 2 File Name:")

    dataA = open(fileName)
    dataB = open(fileName2)
    
    print(dataB.read())
    print(dataA.read())

swapFileData()