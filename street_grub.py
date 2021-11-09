import os
import configurations

os.environ.setdefault("DJANGO_CONFIGURATION", "Local")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "realestate.config.local")
configurations.setup()

from realestate.countries.models import Country
from realestate.districts.models import Districts
from realestate.streets.models import Streets

from street_grabber.parse import get_streets

# country = Country(name="Киев")
# country.save()

for street in get_streets():
    district = Districts.objects.translated(name__contains=street.district)
    if district:
        print(district[0].id)
        street = Streets(name=street.street, district_id=district[0].id)
        street.save()
    else:
        district = Districts(name=street.district, country_id=1)
        district.save()
        street = Streets(name=street.street, district_id=district.id)
        street.save()
