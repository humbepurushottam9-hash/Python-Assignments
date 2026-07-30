import sys
import os
import ProcInfo

def main():
    try:
        ProcInfo.ConfigureLogger()

        if len(sys.argv) != 1:
            raise ValueError("This program does not accept command line arguments")

        if ProcInfo.ValidateArguments():

            ProcInfo.GetProcessInformations()

    except ValueError as e:
        import logging
        logging.error(e)

    except Exception as e:
        import logging
        logging.error(e)

if __name__=="__main__":
    main()                    
