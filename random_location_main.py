import os
import random

import configurations

os.environ.setdefault("DJANGO_CONFIGURATION", "Local")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "realestate.config.local")
configurations.setup()

from realestate.listings.models import Listing
from django.contrib.gis.geos import Point
import geojson

list = [
    {
        'district': 'лул',
        'lat': 30.612,
        'lng': 50.463,
    },
    {
        'district': 'лул',
        'lat': 30.445,
        'lng': 50.426,
    },
    {
        'district': 'лул',
        'lat': 30.4794,
        'lng': 50.4201,
    }
]


for listing in Listing.objects.all():
    location = random.choice(list)
    listing.location = Point(geojson.utils.generate_random("Point", boundingBox=[30.407, 50.400, 30.665, 50.488]).get("coordinates"))
    listing.save()
