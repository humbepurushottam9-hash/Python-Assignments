import os
import sys

def CopyFile(FileName):
    if os.path.isfile(FileName):
        Source = open(FileName,"r")
        Destination = open("Demo2.txt","w")

        Data = Source.read()
        Destination.write(Data)

        Source.close()
        Destination.close()

        print("Contents copied successfully into Demo2.txt")
    else:
        print("File does not exist")  

def main():
    if len(sys.argv) != 2:
        print("Usage:python Program.py<FileName>")
        return
    
    CopyFile(sys.argv[1])

if __name__=="__main__":
    main()


    