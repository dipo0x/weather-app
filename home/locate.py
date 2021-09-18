# import module
from geopy.geocoders import Nominatim

# initialize Nominatim API
geolocator = Nominatim(user_agent="geoapiExercises")

# Latitude & Longitude input
Latitude = "6.5786038"
Longitude = "3.3492318"

location = geolocator.reverse(Latitude+","+Longitude)

# Display
address = location.raw['address']
city = address.get('city', '')
print(city)

