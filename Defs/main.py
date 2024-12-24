import os

from methods.ai_crypt import AICrypt
from methods.emoji_crypt import EmojiCrypt
from methods.skipcode_crpyt import SkipCodeCrypt

def main_menu() :
    methods = {
        "1": ("AI Encryption", AICrypt),
        "2": ("Emoji Encrpytion", EmojiCrypt),
        "3": ("SkipCode Encryption", SkipCodeCrypt)
    }

    while True :
        os.system("clear")
        # logo

        print("1. AI Encryption")
        print("2. Emoji Encrpytion")
        print("3. Skip Code Encryption")
        print("4. Decrypt a message")
        print("5. Exit")

        choice = input ("VerumVeil >>> Choose an Option: ")

        if choice in methods :
            method_name, method_class = methods[choice]

            method = method_class

            message = input("VerumVile >>> Enter your message: ")
            key = input("VerumVile >>> Enter your password: ")

            encypted_data = method.encrypt(message, key)

            print("Encrypted message : {}".format(encypted_data))

        elif choice == "4" :
            #Decrpyt the message
            print("Decrpyted message")

        elif choice == "5" :
            print("Exiting")
            break

        else :
            print ("Invalid choice, Try again")