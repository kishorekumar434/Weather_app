import requests,sys

def get_weather(city):
    api="d71f82a6c0a3d9ac9f13c1de3539b990"
    url= f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric'

    responce=requests.get(url)
    data=responce.json()
    print(data)

    if data['cod']==200:
        lon=data['coord']['lon']
        lat=data['coord']['lat']
        weather=data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        country=data['sys']['country']


        print(f"""
Coordinate(lon/lat): {lon}/{lat}
Weather: {weather}
Temperature: {temperature}°C
Humidity: {humidity}%
Wind Speed: {wind_speed} m/s
Country: {country}
    """)
    else:
        print("City not found, Please check spelling or try again!")

def main():
    
    city=input("Enter the city name:")
    get_weather(city)

main()
