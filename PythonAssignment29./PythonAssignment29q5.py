import os

def CountFrequency(FileName,word):
    if os.path.isfile(FileName):
        File = open(FileName,"r")

        Data = File.read()

        Count = Data.count(word)

        print("Frequency of",word,"is",Count)

        File.close()

    else:
        print("File does not exist")

def main():
    Value = input("Enter file name: ")
    str = input("Enter string to search: ")

    CountFrequency(Value,str)

if __name__=="__main__":
    main()