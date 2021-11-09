import os
import configurations

os.environ.setdefault("DJANGO_CONFIGURATION", "Local")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "realestate.config.local")
configurations.setup()

from realestate.districts.models import Districts
from realestate.micro_districts.models import MicroDistricts

from district_grubber.parser import get_districts

#
# district = Districts(name='kek', country_id=1)
# district.save()


def fill(db_district):
    for micro_district in micro_districts:
        md = MicroDistricts(name=micro_district)
        md.save()
        print(db_district)
        db_district.micro_districts.add(md)
        db_district.save()


for districtName, micro_districts in get_districts().items():
    district = Districts.objects.translated(name__contains=districtName)
    print(district)
    print(bool(district))
    if district:
        fill(district[0])
    # else:
    #     newDistrict = Districts(name=districtName, country_id=1)
    #     newDistrict.save()
    #     fill(newDistrict)


