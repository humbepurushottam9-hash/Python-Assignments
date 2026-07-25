import time
import schedule
import datetime

def Display():
    
    print(datetime.datetime.now())

def main():
    print("Automation script started")

    schedule.every(1).minute.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()        