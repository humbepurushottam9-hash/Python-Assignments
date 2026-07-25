import schedule
import time
import datetime

def Writeinfile():

    fileobj = open("Marvellous.txt","a")

    fileobj.write("Task executed at: " + str(datetime.datetime.now()) + "\n")

    fileobj.close()

def main():
    print("Automation script started")

    schedule.every(1).minutes.do(Writeinfile)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()            