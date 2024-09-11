# Simple troubleshooting system for a computer issue

def troubleshoot():
    print("Welcome to Computer Troubleshooter!")
    print("Answer 'yes' or 'no' to the following questions.")

    response = input("Is your computer turning on? ").lower()

    if response == 'no':
        print("Check the power supply and make sure the cable is connected properly.")
        return
    else:
        response = input("Is the screen displaying properly? ").lower()

        if response == 'no':
            print("Check the display cables or try restarting your computer.")
            return
        else:
            response = input("Is the system running slow? ").lower()

            if response == 'yes':
                print("Try restarting the computer or clearing unnecessary files.")
            else:
                print("Your computer seems to be functioning normally.")

# Running the troubleshooting function
troubleshoot()

