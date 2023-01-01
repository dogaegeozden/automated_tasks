# IMPORTING LIBRARIES
from twilio.rest import Client
from os import popen, environ
from re import compile
from logging import basicConfig, DEBUG, debug, disable, CRITICAL

# Doing the basic configuration for the debugging feature
basicConfig(level=DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Comment out the line to enable debugging.
disable(CRITICAL)

def main():
    """The function which runs the entire program"""
    # Printing the computer's local ip address in debug mode.
    debug(f'My Ip Address = {findMyIp()}')
    # Executing a system command to scan ports and writing the results to file called results.txt
    scanResult = popen(f'proxychains nmap -sT -sU -sV -sC -A -p- {findMyIp()} > results.txt').read()
    # Opening the results file in read mode
    with open('results.txt', 'r') as f:
        # Reading the contents of the file.
        fContents = f.read()
        # Printing out the file's contents in debug mode.
        debug(fContents)

    # Creating a message from the information that have been collecting.
    message = f'Hi, I\'m your computer, here are your port scanning results:\n{fContents}'
    # Calling the send text function
    sendText(sid=environ['TWILIOSID'], token=environ['TWILIOTOKEN'], myTwilioNumber=environ['MYTWILIOPHONENUM'], targetCellPhone=environ['MYREGULARPHONENUM'], message=message)


def sendText(sid, token, myTwilioNumber, targetCellPhone, message):
    """A function which sends text messages"""
    # Printing the twilio number, regular phone number and the message in debug mode.
    debug(f'From: {myTwilioNumber} - To: {targetCellPhone} -- Message: {message}')
    # Creating a twilio client using sid and token
    twilioCli=Client(sid,token)
    # Sending a text message
    message = twilioCli.messages.create(body=message,from_=myTwilioNumber, to=targetCellPhone)

def findMyIp():
    # Creating a ip address regular expression to find the ip address.
    ipAddrRegex = compile(r'(10|192|172).\d{1,3}\.\d{1,3}.\d{1,3}') # Hint: The Internet Assigned Numbers Authority (IANA) has reserved three blocks of the IP address space for private internets and these are starting with 10, 192 and 172
    # Reading output from the ifconfig system command.
    networkIntInf = str(popen('ifconfig').read())
    # Searching the ip address in the out put using the regular expression that is just created.
    ipAddr = ipAddrRegex.search(networkIntInf).group()
    # Returning the ip addres
    return ipAddr

# Evaluate if the source is being run on its own or being imported somewhere else. With this conditional in place, your code can not be imported somewhere else.
if __name__ == '__main__':
    main()
