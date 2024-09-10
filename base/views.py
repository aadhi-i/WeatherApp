from django.shortcuts import render
import requests
import json


# Create your views here.

def get_weather(city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    api_key = "35b888d9dbbc35ae4dd52495c6f89360"
    parameters = {
        'q': city,
        'appid': api_key,
        'units': 'metric',
    }
    response=requests.get(base_url,params=parameters)
    
    if response.status_code==200:
        return response.json()
    else:
        return None

def home(request):
    city=request.GET.get('city')
    icon_url='https://openweathermap.org/img/wn/10d@2x.png'
    if city==None:
        city='Cochin'
    
    if city:
        weather_data_res=get_weather(city)

        if weather_data_res is not None:
            icon_id=weather_data_res['weather'][0]['icon']
            icon_url=f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
            #extracting details and getting to front end
            weather=weather_data_res['weather'][0]['main']
            weather_description=weather_data_res['weather'][0]['description']
            city=weather_data_res['name']
            country=weather_data_res['sys']['country']
            wind_speed=weather_data_res['wind']['speed']
            pressure=weather_data_res['main']['pressure']
            humidity=weather_data_res['main']['humidity']
            temperature=weather_data_res['main']['temp']
        else:
            return render(request,'index.html')
    return render(request,'index.html',{
        'icon_url':icon_url,
        'weather': weather,
        'weather_description':weather_description,
        'city':city,
        'country':country,
        'wind_speed':wind_speed,
        'pressure':pressure,
        'humidity':humidity,
        'temperature':temperature,
    })

    return render(request,'index.html')