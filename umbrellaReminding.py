# IMPORTING LIBRARIES
from requests import get
from twilio.rest import Client
from bs4 import BeautifulSoup
from os import environ
from logging import basicConfig, DEBUG, debug, disable, CRITICAL

# Doing the basic configuration for the debugging feature
basicConfig(level=DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Comment out the line to enable debugging.
disable(CRITICAL)

def main():
    """The function which runs the entire program"""
    sendText(message=weatherDataParser())

def sendText(message):
    """A function which sends text messages"""
    # Setting the twilio sid from the environment variables.
    sid = environ['TWILIOSID']
    # Setting the twilio token from the environment variables.
    token = environ['TWILIOTOKEN']
    # Creating the twilio client.
    twilioCli = Client(sid,token)
    # Setting the twilio phone number using the environment variables.
    myTwilioNumber = environ['MYTWILIOPHONENUM']
    # Setting the target cell phone number using the environment variables.
    targetCellPhone = environ['MYREGULARPHONENUM']
    # Printing the twilio phone number, target phone number and the message in debug mode.
    debug(f'From: {myTwilioNumber} - To: {targetCellPhone} -- Message: {weatherDataParser()}')
    # Sending text message
    message = twilioCli.messages.create(body=message,from_=myTwilioNumber, to=targetCellPhone)


def weatherDataParser():
    """A function which gets the weather data from https://weather.gc.ca/"""
    # Creating a url string. Hint: Government of Canada local forecast. Very credible!
    url = 'https://weather.gc.ca/city/pages/on-143_metric_e.html'
    # Sending the get request to the url
    res = get(url)
    # Creating a soup object to parse html pages.
    soup = BeautifulSoup(res.text, 'html.parser')
    # Getting the weather condition text from the html page.
    weatherCondition = str(soup.select('section details p')[0].getText())
    # Getting the weather temperature text from the html page.
    weatherTemperature = str(soup.select('dl .mrgn-bttm-0')[6].getText())[0:-1]
    # Checking if "rain" or "shower" keywords are in the weather condition.
    if 'rain' in weatherCondition.lower() or 'shower' in weatherCondition.lower():
        # Creating a message.
        message = f'Hi, I\'m your computer.\nWeather is {weatherCondition.lower()}, {weatherTemperature} -> Don\'t forget your umbrella'
    # Checking if "rain" or "shower" keywords are not in the weather condition.
    else:
        # Creating a message.
        message = f'Hi, I\'m your computer.\nWeather is {weatherCondition.lower()}, {weatherTemperature}'
    # Printing the message in debug mode.
    debug(message)
    # Returning the message.
    return message

# Evaluate if the source is being run on its own or being imported somewhere else. With this conditional in place, your code can not be imported somewhere else.
if __name__ == '__main__':
    main()
