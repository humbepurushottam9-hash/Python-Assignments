import schedule
import time

def Display():
    print("Coding kr...")

def main():

    schedule.every(30).minute.do(Display)

    while True:
        schedule.run_pending()
        time.sleep()

if __name__=="__main__":
    main()            