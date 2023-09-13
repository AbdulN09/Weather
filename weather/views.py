from django.shortcuts import render, HttpResponse
import requests

API_KEY = '624d3c6f0e30e650e8242f6e4d7374a1'

def home(request):
    return render(request, 'index.html')

def demo(request):
    if request.method == 'POST':
        cityname = request.POST.get('cityname')
        api_url = f'https://api.openweathermap.org/data/2.5/weather?q={cityname}&appid={API_KEY}'      
        response = requests.get(api_url)       
        if response.status_code == 200:
            data = response.json()
            temperature = data['main']['temp']
            weather_description = data['weather'][0]['description']            
            context = {
                'cityname': cityname,
                'temperature': temperature,
                'weather_description': weather_description,
            }           
            return render(request, 'result.html', context)
        return HttpResponse("Invalid page")

def final(request):
    return render(request, 'result.html')

