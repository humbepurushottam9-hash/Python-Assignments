import sys
import logging
import ProcInfoLog
import Mailsender


def main():

    try:

        if len(sys.argv) != 3:
            print("Usage : python main.py DirectoryName ReceiverEmail")
            return

        DirectoryName = sys.argv[1]
        ReceiverMail = sys.argv[2]

        LogFile = ProcInfoLog.ConfigureLogger(DirectoryName)

        if ProcInfoLog.ValidateDirectory(DirectoryName) == False:
            return

        ProcInfoLog.GetProcessInformation()

        SenderMail = "humbepurushottam9@gmail.com"

        Password = "gvjlsbrkannuqhvh"

        Status = Mailsender.SendMail(
            SenderMail,
            Password,
            ReceiverMail,
            LogFile
        )

        if Status == True:
            logging.info("Mail sent successfully.")

        else:
            logging.error("Unable to send mail.")

    except Exception as e:
        logging.error(f"Error : {e}")


if __name__ == "__main__":
    main()