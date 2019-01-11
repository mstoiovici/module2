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
print("-----exp2-------")
endpoint = "http://api.openweathermap.org/data/2.5/weather"
payload = {"q": "Constanta,Romania", "units":"metric", "appid":"api -key"}
response = requests.get(endpoint, params=payload)
print (response.url)
print("-----------------")
print (response.headers["content-type"])




print("-----Task3 Convert the response to json------")
endpoint = "http://api.openweathermap.org/data/2.5/weather"
payload = {"q": "Constanta,Romania", "units":"metric", "appid":"api -key"}
response = requests.get(endpoint, params=payload)

print("ex 1 - Update the ﬁle so that it converts the response to JSON format, prints the temperature in Constanta and also prints the response in its original (non-JSON) format.")
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
print("ex 2 -  Update your Python ﬁle so that it prints out a nice statement to your command line about the weather")
temperature = data["main"]["temp"]
name = data["name"]
weather = data["weather"][0]["main"]
print (u"It's {}C in {}, and the sky is {}".format(temperature, name, weather))
