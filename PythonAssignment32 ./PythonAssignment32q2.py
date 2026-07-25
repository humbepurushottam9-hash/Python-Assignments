import os
import schedule
import time
import datetime

def MonitorFile():
    filepath = input("Enter the file path: ").strip()

    def CheckFileSize():
        current = datetime.datetime.now()

        with open("FileSizeLog.txt", "a") as log:
            if os.path.exists(filepath):
                size = os.path.getsize(filepath)

                log.write("File Path : " + filepath + "\n")
                log.write("File Size : " + str(size) + " bytes\n")
                log.write("Date      : " + current.strftime("%d-%m-%Y") + "\n")
                log.write("Time      : " + current.strftime("%H:%M:%S") + "\n")
                log.write("-" * 40 + "\n")

                print("File size logged successfully.")
            else:
                log.write("File Path : " + filepath + "\n")
                log.write("Status    : File does not exist\n")
                log.write("Date      : " + current.strftime("%d-%m-%Y") + "\n")
                log.write("Time      : " + current.strftime("%H:%M:%S") + "\n")
                log.write("-" * 40 + "\n")

                print("File does not exist.")

    schedule.every(30).seconds.do(CheckFileSize)

    print("Monitoring started... Press Ctrl+C to stop.")

    while True:
        schedule.run_pending()
        time.sleep(1)

def main():
    MonitorFile()

if __name__ == "__main__":
    main()