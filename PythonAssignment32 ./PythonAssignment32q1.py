import schedule
import time
import datetime

def CreateFile():
    now = datetime.datetime.now()

    filename = "File_"+ now.strftime("%d_%m_%Y_%H_%M_%S") + ".txt"

    with open(filename, "w") as file:
        file.write("Filename : " + filename + "\n")
        file.write("Creation date : " +  now.strftime("%d-%m-%Y") +"\n")
        file.write("Creation time : " +  now.strftime("%H:%M:%S") +"\n")

    print(filename, "created successfully.")


schedule.every(1).minutes.do(CreateFile)

print("File creation scheduler started...")

while True:
    schedule.run_pending()
    time.sleep(1)