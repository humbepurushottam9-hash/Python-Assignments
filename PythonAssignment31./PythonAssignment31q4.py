import schedule
import time
import datetime

def CreateLogFile():
    
    filename = datetime.datetime.now()

    with open(filename, "w") as file:
        file.write("Log file created successfully.\n")
        file.write("Created on : ")
        file.write(datetime.datetime.now())

    print("Created:", filename)

def main():

    schedule.every(10).minutes.do(CreateLogFile)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
