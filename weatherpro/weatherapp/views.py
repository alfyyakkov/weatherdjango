import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

# Create your views here.

def index(request):
	url='http://api.openweathermap.org/data/2.5/weather?q={}&appid=09fec6be8dbc98f68c98fe6338c38324&units=metric'
	form=CityForm()
	if request.method=='POST':
		form=CityForm(request.POST)
		form.save()
	cities=City.objects.all()
	weather_data=[]
	for city in cities:
		r=requests.get(url.format(city.name)).json()
		city_weather={
			'city':city.name,
			'temperature':r['main']['temp'],
			'description':r['weather'][0]['description'],
			'icon':r['weather'][0]['icon'],
			}
		weather_data.append(city_weather)
	context={'weather_data':weather_data,'form':form}
	return render(request,'weather/weather.html',context)


	 #{
	 #"coord":{"lon":-115.1372,"lat":36.175},
	 #"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],
	 #"base":"stations",
	 #"main":{"temp":304.06,"feels_like":305.24,"temp_min":302.39,"temp_max":305.53,"pressure":1012,"humidity":48},
	 #"visibility":10000,
	 #"wind":{"speed":2.57,"deg":60},
	 #"clouds":{"all":1},
	 #"dt":1626962635,
	 #"sys":{"type":1,"id":6171,"country":"US","sunrise":1626957597,"sunset":1627008824},
	 #"timezone":-25200,
	 #"id":5506956,
	 #"name":"Las Vegas",
	 #"cod":200
	 #}