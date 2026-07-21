import os

def ChkFile(FileName):
    if os.path.isfile(FileName):
        print(FileName,"is present in the current directory")
    else:
        print(FileName,"is not present in the current directory")    

def main():
    Value = input("Enter file name: ")

    ChkFile(Value)

if __name__=="__main__":
    main()    