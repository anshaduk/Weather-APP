from django.shortcuts import render
import requests
import datetime

# Create your views here.
def home(request):
    city = request.POST.get('city', 'calicut')
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=e2d241c7aaf2fbaf60da13e5ac82de15"
    PARAMS = {'units': 'metric'}  # temperature in Celsius

    response = requests.get(url, PARAMS)
    if response.status_code != 200:
        return render(request, 'index.html', {
            'error': f"Could not fetch weather data for {city}. Please try again.",
            'day': datetime.date.today(),
            'city': city,
        })

    data = response.json()
    if 'weather' not in data or 'main' not in data:
        return render(request, 'index.html', {
            'error': f"Invalid data received for {city}.",
            'day': datetime.date.today(),
            'city': city,
        })

    description = data['weather'][0]['description']
    icon = data['weather'][0]['icon']
    temp = data['main']['temp']
    day = datetime.date.today()

    return render(request, 'index.html', {
        'description': description,
        'icon': icon,
        'temp': temp,
        'day': day,
        'city': city,
    })