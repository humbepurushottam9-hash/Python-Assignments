import os
import time
import schedule
import datetime

def CountFiles(dirname):
    count = 0

    for entry in os.scandir(dirname):
        if entry.is_file():
            count += 1

    current_time = datetime.datetime.now()

    with open("DirectoryCountLog.txt", "a") as file:
        file.write("Directory Path : " + dirname + "\n")
        file.write("Number of Files : " + str(count) + "\n")
        file.write("Date and Time : " + current_time + "\n")
        file.write("-" * 40 + "\n")

    print("Directory scanned successfully.")

def main():
    dirname = input("Enter directory path: ")

    if not os.path.isdir(dirname):
        print("Invalid Directory")
        return

    schedule.every(5).minutes.do(CountFiles, dirname)

    print("Directory monitoring started...")
    print("Press Ctrl+C to stop.")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()