import schedule
import time

def Display(Value1):
    print(Value1)
    
def main():
    Value = input("Enter message: ")
    Interval = int(input("Enter the interval: ")) 

    schedule.every(Interval).seconds.do(Display,Value)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()