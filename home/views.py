from django.shortcuts import render
import requests, json
from django.http import HttpResponse
from datetime import datetime as date
import pyowm
from .forms import locationForm
from .models import location

# Create your views here.
owm = pyowm.OWM(API_key=YOUR_API_KEY)
OpenWMap=pyowm.OWM(YOUR_API_KEY)

def home(request):
	inp= request.POST.get('param')
	locations = location.objects.all().order_by('-date_added')[:3]
	if request.method == 'POST':
		form = locationForm(request.POST or None)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.location = inp
			obj.save()
			Weather=OpenWMap.weather_at_place(inp)
			Data=Weather.get_weather()
			temp = Data.get_temperature(unit='celsius')
			city = inp
			obs = owm.weather_at_place(inp)
			w = obs.get_weather()

			k = w.get_status()
			x = w.get_temperature(unit='celsius')
			av = temp['temp']
			mi = temp['temp_min']

			context = {
			'form': form,
			'Current_weather' : 'Current weather in %s is %s. The minimum temperature is %s and the max is %s. The average weather is %0.2f' % (city, k, x['temp_max'], av, mi)
			}
			return render(request, 'home.html', context)
		else:
			return render(request, 'home.html')
	else:
		return render(request = request, template_name = 'home.html', context = {
			'locations': locations
			})