import schedule
import time

def DisplayMessage(message):
    print(message)

def main():
    Value = input("Enter message: ")

    schedule.every(5).seconds.do(DisplayMessage,Value)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()