# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 10:29:50 2019

@author: Katharina
"""
##TO MAKE THIS WORK INSERT API KEYS!


import requests
#-------------------------------------------------------------------------#
#1st API: GETTING CITY TO CORREPONDING POSTCODE 
postcode = input('Which city would you like to search in the UK? Please type in the postcode ')

endpoint = "https://api.postcodes.io/postcodes/"
payload = {'q': postcode}
#
response = requests.get(endpoint, params=payload)
data = response.json()

print(response.url)
#print(data)

#Converting the Postcode into the city 
city = (data['result'][0]['admin_district'])

state = (data['result'][0]['region'])

longitude = (data['result'][0]['longitude'])
latitude = (data['result'][0]['latitude'])


print("You'll get all important information on", city+ ",", state)


print('LONGITUDE', longitude)
print('LATITUDE', latitude)

endpoint = "http://api.openweathermap.org/data/2.5/weather"
payload = {"q": city, "units":"metric", "appid":"API-KEY"}

response = requests.get(endpoint, params=payload)
data = response.json()

#print(data)

#print(response.url)
#print(response.status_code)
#-------------------------------------------------------------------------#


#-------------------------------------------------------------------------#
##2nd API: USING CITY FROM ABOVE TO GET WEATHER INFO 
temperature = data['main']['temp']
name = data['name']
weather = data['weather'][0]['main']
print('TEMPERATURE', temperature)
print('WEATHER', weather)

print('It is {}C in {}, and the sky is {}'.format(temperature, name, weather))


def userSuggestion():
    if temperature < 10:
        print("It's cold today, take your big coat!")
    elif temperature < 20:
        print("Light jacket should do today.")
    else:
        print("It's getting hot in here - take your swimsuit!")
        
userSuggestion()
#        
#-------------------------------------------------------------------------#




#-------------------------------------------------------------------------#
##3rd API: POLLUTION INFO --> Get info from 1st API 
##HOW DOES IT WORK FOR ENGLAND?! COUNTY VS STATE
#endpoint = "http://api.airvisual.com/v2/city?"
#payload = {'city': city, 'county': state, 'country': 'England', 'key':'API-KEY'}
#
#response = requests.get(endpoint, params=payload)
#data = response.json()
#
#print(response.url)

#-------------------------------------------------------------------------#
#4th API: CRIME
endpoint = "https://data.police.uk/api/crimes-street/all-crime"
payload = {'lat': latitude, 'lng': longitude}

response = requests.get(endpoint, params=payload)
data = response.json()

#print(response.url)
crime = (data[0]['category'])
crime_location = (data[0]['location']['street']['name'])

print('The latest crime in your area was a {} and it took place {}'.format(crime, crime_location))








