import os
import schedule
import time

def MonitorFile():
    filepath = input("Enter the file path: ").strip()

    def ReadFile():
        try:
            if not os.path.exists(filepath):
                print("Error: File does not exist.")
                return

            if os.path.getsize(filepath) == 0:
                print("Error: File is empty.")
                return

            file = open(filepath, "r")

            print("\n----- File Contents -----")
            print(file.read())
            print("-------------------------\n")

            file.close()

        except PermissionError:
            print("Error: Permission denied.")

        except OSError:
            print("Error: File cannot be opened.")

    schedule.every(1).minutes.do(ReadFile)

    print("Monitoring started...")

    
    ReadFile()

    while True:
        schedule.run_pending()
        time.sleep(1)

def main():
    MonitorFile()

if __name__ == "__main__":
    main()