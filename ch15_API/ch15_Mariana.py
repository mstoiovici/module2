# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 14:04:29 2019

@author: maria
"""
#in order for this code to work you need to put in you domain and private key from mailgun 
print("------------Task1 - Test code for my Mailgun API-------------------")
import requests
def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/domain/messages",
        auth=("api", "api-key"),
        data={"from": "Excited User <mariana.stoiovici@gmail.com>",
              "to": ["stoiovici@gmail.com"],
              "subject": "This is an email send only with Python",
              "text": "If this works, then I've just send you an email just by using Python!!!! Isn't this really exciting?? :D"})
#send_simple_message()

    
print("------------Task2 A weather app-------------------")
print("-----exp1p-------")
endpoint = "http://api.openweathermap.org/data/2.5/weather"
payload = {"q": "London,UK", "units":"metric", "appid":"api key"}
response = requests.get(endpoint, params=payload)
print (response.url)
#####dir(response)run on our console gives us all the options
#print (response.status_code)
#print (response.headers["content-type"])
#print (response._content)
#print (response.raw)
print("-----exp2 -------")
endpoint = "http://api.openweathermap.org/data/2.5/weather"
payload = {"q": "Constanta,Romania", "units":"metric", "appid":"api -key"}
response = requests.get(endpoint, params=payload)
print (response.url)
print("-----------------")
print (response.headers["content-type"])




print("-----exp3------")
endpoint = "http://api.openweathermap.org/data/2.5/weather"
payload = {"q": "Constanta,Romania", "units":"metric", "appid":"api -key"}
response = requests.get(endpoint, params=payload)

print("ex 3.1 - Update the ﬁle so that it converts the response to JSON format, prints the temperature in Constanta and also prints the response in its original (non-JSON) format.")
data=response.json()

print("this is what data looks like \n")
print(data)
print("-------------------")
print("this is what data['main'] looks like \n")
print(data['main'])
#print("-------------------")
#print (response.url)
#print("---------------------")
#print (response.headers["content-type"])
print("---------------------")
print("exp -  Update your Python ﬁle so that it prints out a nice statement to your command line about the weather")
temperature = data["main"]["temp"]
name = data["name"]
weather = data["weather"][0]["main"]
print (u"It's {}C in {}, and the sky is {}".format(temperature, name, weather))


print("------------------------------Task3 - independent practice----------------")
import requests
endpoint="https://api.openweathermap.org/data/2.5/weather"
payload={"q":"London","units":"metric", "appid":"api key"}
response=requests.get(endpoint, params=payload)
print(response.url)
print(response.content)

print(response.status_code)
print(response.headers["content-type"])

print()
print("------This is the information with the raw format---")
print(response.content)

a=response.content
print(type(a))
print("--------------")
print(response.text)
b=response.text
print("--------------------")
print(type(b))

print()
print("------This is the information with the json format---")
data=response.json()
print(data)
print(type(data))
print(data["main"])


print("------------This is for our project-----------")
import requests

# The base url to access the API information
endpoint_weather = "https://api.openweathermap.org/data/2.5/weather"
endpoint_postcode = "https://api.postcodes.io/postcodes/"

# The parameters to what exactly you need from the API
# The structure of this varies from API to API
payload = {"q": "Zermatt, CH", "units": "metric", "appid": "apy-key"}

# Sometimes you don't need a parameter, just a value
postcode = "LE111LG"

# Before requesting anything from an API test the url by going to it in a browser
test_weather_url = (endpoint_weather,payload)
#print(test_weather_url)

test_postcode_url = (endpoint_postcode + postcode)
print(test_postcode_url)

## If you get a decent response in a browser, you can go ahead and request it with Python
weather_response = requests.get(endpoint_weather, params=payload)
postcode_response = requests.get(endpoint_postcode + postcode)

## Convert your return into json
data_weather = weather_response.json()
print("------This is data_weather--------------")
print(data_weather)
data_postcode = postcode_response.json()
print("\n","------This is data_postcode--------------","\n")
print(data_postcode)
print(type(data_postcode))
#
## To be able to read the data you need to look at what you actually get.
## Look at the type of brackets that surrounds each item in your json file.
## If it's {} it will work like a dictionary
## If it's [] it will work like a list
#print(data_weather['weather'][0]['description'])
print(data_postcode['result']['longitude'])


endpoint_postcode="https://api.postcodes.io/postcodes/"
postcode="SE10 9JP"
test_postcode_url=(endpoint_postcode+postcode)
print(test_postcode_url)

postcode="SE109JP"
test_postcode_url=(endpoint_postcode+postcode)
print(test_postcode_url)
postcode_response=requests.get(endpoint_postcode+postcode)
data_postcode=postcode_response.json()
print(data_postcode)
print(type(data_postcode))
latitude=data_postcode["result"]["latitude"]
print(latitude)
longitude=data_postcode["result"]["longitude"]
print(longitude)