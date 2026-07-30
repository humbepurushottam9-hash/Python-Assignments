import psutil
import logging
import os

def ConfigureLogger():
    logging.basicConfig(
        filename = "ProcessLog.txt",
        level = logging.INFO,
        format = "%(asctime)s : %(levelname)s : %(message)s"
    )

def ValidateArguments():
    return True

def GetProcessInformations():
    try:
        logging.info("Running Process Information")  

        for process in psutil.process_iter(['pid', 'name', 'username']):
            try:
                info = process.info

                logging.info(
                    f"Name : {info['name']} |"
                    f"PID : {info['pid']} |"
                    f"User : {info['username']}"
                ) 

            except(psutil.NoSuchProcess,
                   psutil.AccessDenied,
                   psutil.ZombieProcess):
                continue

        logging.info("Process information collected successfully")

    except Exception as e:
        logging.error(f"error : {e}")             
