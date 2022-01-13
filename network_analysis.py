#!/usr/bin/python3
# Class: NSSA 221
# Author: Robert Shepard ras2966
# Date: 9/17/2021
import os
import subprocess
import netifaces
answer = ""
gateway = netifaces.gateways()
gateway = gateway["default"][netifaces.AF_INET][0]

while answer != "q": # script ends when the user enters 'q'
    os.system("clear")
    print("********** Ping Test Troubleshooter **********")
    print("Commands: \n- '1' Test connectivity to your gateway\
        \n- '2' Test for remote connectivity (RIT DNS)\
        \n- '3' Test for DNS resolution.\
        \n- '4' Display your gateway IP address \
        \n- 'help' displays commands \
        \n- 'q' quit the program\n")
    answer = input("Enter selection: ")
    if answer == "1": # default gateway test
        os.system("clear")
        print("Pinging default gateway ...")
        os.system("sleep 3")
        ping = subprocess.run(["ping", "-c", "1", gateway], stdout=subprocess.DEVNULL) # command to ping an ip address and DEVNULL suppreses the data
        os.system("clear")
        if ping.returncode == 0:
            print("Ping to your default gateway was SUCCESSFUL")
        else:
            print("pPng to your default gateway FAILED")
        os.system("sleep 3")
    elif answer == "2": # remote connectivity test 
        os.system("clear")
        print("Pinging RIT's DNS 129.21.3.17 ...")
        os.system("sleep 3")
        ping = subprocess.run(["ping", "-c", "1", "129.21.3.17"], stdout=subprocess.DEVNULL)
        os.system("clear")
        if ping.returncode == 0:
            print("Ping to the outside IP Address (129.21.3.17) was SUCCESSFUL")
        else:
            print("Ping to the outside IP Address (129.21.3.17) FAILED")
        os.system("sleep 3")

    elif answer == "3": # DNS resolution test, uses www.google.com
        os.system("clear")
        print("Resolving DNS, pinging www.google.com ...")
        os.system("sleep 3")
        ping = subprocess.run(["ping", "-c", "1", "www.google.com"], stdout=subprocess.DEVNULL)
        os.system("clear")
        if ping.returncode == 0:
            print("Ping to www.google.com was SUCCESSFUL")
        else:
            print("Ping to www.google.com FAILED")
        os.system("sleep 3")

    elif answer == "4": # displays default gateway IP Address to the user
        os.system("clear")
        print("Getting default gateway IP ...")
        os.system("sleep 1")
        gateway_acquire = netifaces.gateways()
        gateway_acquire = gateway_acquire["default"][netifaces.AF_INET][0]
        os.system("clear")
        print("Your default gateway IP address is " + gateway_acquire)
        os.system("sleep 3")


    elif answer == "help": #display all commands 
        os.system("clear")
        print("Commands: \n- '1' Test connectivity to your gateway\
        \n- '2' Test for remote connectivity (RIT DNS)\
        \n- '3' Test for DNS resolution.\
        \n- '4' Display your gateway IP address \
        \n- 'help' Displays commands \
        \n- 'q' Quit the program \
        \n- Be sure to enter one of the options without '' around your input")
        os.system("sleep 5")
    elif answer == "q":
        continue
        # just so invalid commands work properly with the else statement
    else: # for invalid commands
        os.system("clear")
        print("Invalid command,'", answer ,"'try again", sep = "")
        os.system("sleep 3")
os.system("clear")
print("Have a nice day!")





        