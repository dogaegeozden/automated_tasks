# LIBRARIES
from requests import get
from twilio.rest import Client
from bs4 import BeautifulSoup
from os import popen
from re import compile
from logging import basicConfig, DEBUG, debug, disable, CRITICAL
from threading import Thread
from datetime import datetime
from json import load as json_load
from pathlib import Path

# Doing the basic configuration for the debugging feature
basicConfig(level=DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Disabling the debugging feature. Hint: Comment out the line to enable debugging.
disable(CRITICAL)

# Creating a path which leads to the parent folder of this python file.
base_dir = Path(__file__).resolve().parent

def main():
    """The function which runs the entire program"""
    # Calling the read_the_credentials function.
    read_the_credentials()
    # Calling the send_text function.
    send_text(message=create_a_message())

def read_the_credentials():
    """A function which reads the credentials from a json file"""
    # Opening the json file in read mode
    with open(Path(base_dir, "credentials.json"), "r") as file:
        # Reading the json document and storing it's contents in a variable called credentials.
        credentials = json_load(file)
    # Creating global variables called sid, token, my_twilio_number, target_cell_phone
    global sid, token, my_twilio_number, target_cell_phone
    # Setting the twilio sid from the environment variables.
    sid = credentials['TWILIOSID']
    # Setting the twilio token from the environment variables.
    token = credentials['TWILIOTOKEN']
    # Setting the twilio phone number using the environment variables.
    my_twilio_number = credentials['MYTWILIOPHONENUM']
    # Setting the target cell phone number using the environment variables.
    target_cell_phone = credentials['MYREGULARPHONENUM']

def send_text(message):
    """A function which sends text messages"""
    # Creating the twilio client.
    twilio_cli = Client(sid,token)
    # Printing the twilio phone number, target phone number and the message in debug mode.
    debug(f'From: {my_twilio_number} - To: {target_cell_phone} -- Message: {parse_the_weather_data()}')
    # Sending text message
    message = twilio_cli.messages.create(body=message,from_=my_twilio_number, to=target_cell_phone)

def parse_the_weather_data():
    """A function which gets the weather data from https://weather.gc.ca/"""
    # Creating a url string. Hint: Government of Canada local forecast. Very credible!
    url = 'https://weather.gc.ca/city/pages/on-143_metric_e.html'
    # Sending the get request to the url
    res = get(url)
    # Creating a soup object to parse html pages.
    soup = BeautifulSoup(res.text, 'html.parser')
    # Creating globasl variables called weather_condition and weather_temperature.
    global weather_condition, weather_temperature
    # Getting the weather condition text from the html page.
    weather_condition = str(soup.select('section details p')[0].getText())
    # Getting the weather temperature text from the html page.
    weather_temperature = str(soup.select('dl .mrgn-bttm-0')[6].getText())[0:-1]

def get_the_date_and_time():
    """A function which calculates the current date and time"""
    # Creating a varible called now which is equal to the current date and time
    now = datetime.now()
    # Creating a global varible called date_and_time
    global date_and_time
    # Organizing the current date and time
    date_and_time = now.strftime("%m/%d/%Y, %H:%M:%S")

def scan_my_ports():
    # Creating a ip address regular expression to find the ip address.
    ip_address_regex = compile(r'(10|192|172).\d{1,3}\.\d{1,3}.\d{1,3}') # Hint: The Internet Assigned Numbers Authority (IANA) has reserved three blocks of the IP address space for private internets and these are starting with 10, 192 and 172
    # Reading output from the ifconfig system command.
    network_interface_information = str(popen('ifconfig').read())
    # Searching the ip address in the out put using the regular expression that is just created.
    ip_address = ip_address_regex.search(network_interface_information).group()
    # Printing the computer's local ip address in debug mode.
    debug(f'My Local Ip Address = {ip_address}')
    # Creating a global variable called
    global scan_result
    # Executing a system command to scan ports and writing the results to file called results.txt
    scan_result = popen(f'proxychains nmap -sT -sU -sV -sC -A -p- {ip_address}').read()
    # Rrinting the port scanning results in debug mode.
    debug(scan_result)

def create_a_message():
    """A function which creates a message from the gathered information"""
    # Creating weather_thread which executes the parse_the_weather_data
    weather_thread= Thread(target=parse_the_weather_data)
    # Creating datetime_thread which executes the get_the_date_and_time
    datetime_thread = Thread(target=get_the_date_and_time)
    # Creating port_scanning_thread which executes the scan_my_ports
    port_scanning_thread = Thread(target=scan_my_ports)
    # Starting all the threads
    port_scanning_thread.start()
    weather_thread.start()
    datetime_thread.start()
    # Waiting untill all threads are done
    weather_thread.join()
    datetime_thread.join()
    port_scanning_thread.join()
    # Creating a message
    message=f'{date_and_time}\nWeather: {weather_condition} - {weather_temperature}\n\n\nPort Scanning Results:\n{scan_result}'
    # Returning the message
    return(message)

# Evaluate if the source is being run on its own or being imported somewhere else. With this conditional in place, your code can not be imported somewhere else.
if __name__ == '__main__':
    main()
