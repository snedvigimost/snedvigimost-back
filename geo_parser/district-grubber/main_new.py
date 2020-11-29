import os
import configurations

os.environ.setdefault("DJANGO_CONFIGURATION", "Local")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "realestate.config.local")
configurations.setup()

from realestate.districts.models import Districts
from realestate.micro_districts.models import MicroDistricts

from parser import get_districts


for district, micro_districts in get_districts().items():
    districts = Districts.objects.get(name__contains=district)
    for micro_district in micro_districts:
        md = MicroDistricts(name=micro_district)
        md.save()
        districts.micro_districts.add(md)
        districts.save()
