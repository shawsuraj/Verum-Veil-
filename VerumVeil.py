#!/usr/bin/python3

from Defs.main import main_menu

if __name__ == "__main__" :
    try :
        main_menu()

    except KeyboardInterrupt :
        #exit command
        print ("exit placeholder")