import os
import schedule
import time
import datetime

def DeleteEmptyFiles():
    directory = input("Enter directory path: ").strip()

    if not os.path.isdir(directory):
        print("Directory does not exist.")
        return

    def RemoveEmptyFiles():
        with open("DeletedFilesLog.txt", "a") as logfile:

            logfile.write("\n----------------------------------------\n")
            logfile.write("Date & Time : " +
                          datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S") + "\n")

            for foldername, subfolders, filenames in os.walk(directory):

                for filename in filenames:

                    filepath = os.path.join(foldername, filename)

                    try:
                 
                        if os.path.getsize(filepath) == 0:

                            os.remove(filepath)

                            logfile.write("Deleted : " + filepath + "\n")
                            print("Deleted:", filepath)

                    except PermissionError:
                        logfile.write("Permission Denied : " + filepath + "\n")
                        print("Permission denied:", filepath)

                    except Exception as e:
                        logfile.write("Error : " + filepath + " : " + str(e) + "\n")
                        print("Error:", filepath)

    schedule.every(1).hours.do(RemoveEmptyFiles)

    print("Monitoring started... Press Ctrl+C to stop.")

    RemoveEmptyFiles()

    while True:
        schedule.run_pending()
        time.sleep(1)

def main():
    DeleteEmptyFiles()

if __name__ == "__main__":
    main()