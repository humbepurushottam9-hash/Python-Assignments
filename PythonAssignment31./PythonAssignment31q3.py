import os
import time
import schedule
import datetime

def ScanDirectory(dirname):
    file_count = 0
    dir_count = 0

    for entry in os.scandir(dirname):
        if entry.is_file():
            file_count += 1

        elif entry.is_dir():
            dir_count += 1

    print("------------------------------------")
    print("Directory Name            :", dirname) 
    print("Number of files           :", file_count) 
    print("Number of subdirectories  :", dir_count)
    print("Date and time             :",datetime.datetime.now())
    print("-------------------------------------")

def main():
    dirname = input("Enter directory name: ")

    if not os.path.isdir(dirname):
        print("Invalid Directory")              
        return

    schedule.every(1).minutes.do(ScanDirectory, dirname)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()        