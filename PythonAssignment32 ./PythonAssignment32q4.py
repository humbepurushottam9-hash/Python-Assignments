import os
import shutil
import schedule
import time
import datetime

def CopyTextFiles():
    source = input("Enter source directory path: ").strip()
    destination = input("Enter destination directory path: ").strip()

    if not os.path.isdir(source):
        print("Source directory does not exist.")
        return

    if not os.path.isdir(destination):
        print("Destination directory does not exist.")
        return

    def CopyFiles():
        logfile = open("CopyLog.txt", "a")

        logfile.write("\n----------------------------------------\n")
        logfile.write("Copy Operation : " +
                      datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S") + "\n")

        for filename in os.listdir(source):

            if filename.endswith(".txt"):

                source_file = os.path.join(source, filename)
                destination_file = os.path.join(destination, filename)

                try:
                    shutil.copy2(source_file, destination_file)

                    logfile.write("Copied : " + source_file +
                                  " --> " + destination_file + "\n")

                    print(filename, "copied successfully.")

                except Exception as e:
                    logfile.write("Failed : " + source_file +
                                  " Reason : " + str(e) + "\n")

                    print("Could not copy:", filename)

        logfile.close()

    schedule.every(10).minutes.do(CopyFiles)

    print("Monitoring started...")

    CopyFiles()

    while True:
        schedule.run_pending()
        time.sleep(1)


def main():
    CopyTextFiles()


if __name__ == "__main__":
    main()