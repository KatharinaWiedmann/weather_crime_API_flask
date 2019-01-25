# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 10:42:31 2019

@author: Katharina
"""
import requests
import config
#-------------------------------------------------------------------------#
#1st API: GETTING CITY TO CORREPONDING POSTCODE 
def finding_city(postcode):
    
#    postcode = input('Which city would you like to search in the UK? Please type in the postcode ')
    
    endpoint = "https://api.postcodes.io/postcodes/"
    payload = {'q': postcode}
    #
    response = requests.get(endpoint, params=payload)
    data = response.json()
    
#    print(response.url)
    #print(data)
    
    results = []
    if response.status_code == 200:
    
        #Converting the Postcode into the city 
        city = (data['result'][0]['admin_district'])
        state = (data['result'][0]['region'])
        
        longitude = (data['result'][0]['longitude'])
        latitude = (data['result'][0]['latitude'])
        
        
#        print("You'll get all important information on", city+ ",", state)
        
        results = [city, state, longitude, latitude]
    return results

#results = finding_city(postcode)

#print(results)
#endpoint = "http://api.openweathermap.org/data/2.5/weather"
#
##Doesn't work with city cause there are several cities with the same name in the world and by default it will take the largest city. 
##payload = {"q": (city_string (+',uk' )), "units":"metric", "appid": config.api_key_weather}
#payload = {"lat": latitude, "lon": longitude, "units":"metric", "appid": config.api_key_weather}
#
#
#response = requests.get(endpoint, params=payload)
#data = response.json()
#
##-------------------------------------------------------------------------#
#
#
##-------------------------------------------------------------------------#
###2nd API: USING CITY FROM ABOVE TO GET WEATHER INFO 
#temperature = data['main']['temp']
#name = data['name']
#weather = data['weather'][0]['main']
#print('TEMPERATURE', temperature)
#print('WEATHER', weather)
#
#print('It is {}C in {}, {}, and the sky is {}'.format(temperature, name,  state, weather))
#
#
#def userSuggestion():
#    if temperature < 10:
#        print("It's cold today, take your big coat!")
#    elif temperature < 20:
#        print("Light jacket should do today.")
#    else:
#        print("It's getting hot in here - take your swimsuit!")
#        
#userSuggestion()
##        
##-------------------------------------------------------------------------#
#
#
#
#
##-------------------------------------------------------------------------#
###3rd API: POLLUTION INFO --> Get info from 1st API 
###HOW DOES IT WORK FOR ENGLAND?! COUNTY VS STATE
##endpoint = "http://api.airvisual.com/v2/city?"
##payload = {'city': city, 'county': state, 'country': 'England', 'key': config.api_key_pollution}
##
##response = requests.get(endpoint, params=payload)
##data = response.json()
##
##print(response.url)
#
##-------------------------------------------------------------------------#
##4th API: CRIME
#endpoint = "https://data.police.uk/api/crimes-street/all-crime"
#payload = {'lat': latitude, 'lng': longitude}
#
#response = requests.get(endpoint, params=payload)
#data = response.json()
#
##print(response.url)
#crime = (data[0]['category'])
#crime_location = (data[0]['location']['street']['name'])
#
#print('The latest crime in your area was a {} and it took place {}'.format(crime, crime_location))
#
#
#
#
#
#
#
#
