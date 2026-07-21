import os

def DisplayContent(FileName):
    if os.path.isfile(FileName):
        file = open(FileName,"r")

        Data = file.read()
        print(Data)

        file.close()

    else:
        print("File does not exist")    

def main():
    Value = input("Enter file name: ")

    DisplayContent(Value)

if __name__=="__main__":
    main()