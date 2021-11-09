import os
# from django.conf import settings
import configurations

# os.environ.setdefault("DJANGO_CONFIGURATION", "Local")
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.local")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "realestate.config")
os.environ.setdefault("DJANGO_CONFIGURATION", "Local")
configurations.setup()

# from realestate.countries.models import Country
# from realestate.districts.models import Districts
# from realestate.streets.models import Streets

# from parse import get_streets
#
# country = Country(name="Киев")
# country.save()
#
# for street in get_streets():
#     try:
#         district = Districts.objects.get(name__contains=street.district)
#         street = Streets(name=street.street, district_id=district.id)
#         street.save()
#     except Districts.DoesNotExist:
#         district = Districts(name=street.district, country_id=country.id)
#         district.save()
#         street = Streets(name=street.street, district_id=district.id)
#         street.save()


# print(get_streets())
