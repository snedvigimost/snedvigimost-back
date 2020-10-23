from collections import namedtuple

from parsel import Selector

Street = namedtuple('Street', ['district', 'street', 'lat', 'long'])


def get_streets():
    with open("result.html", "r+") as file1:
        selector = Selector(file1.read())
        streets = []
        for tr in selector.css('tbody > tr'):
            lat, long = tr.css('::attr(data-coo)').get().split(' ')
            street = tr.css('td:nth-child(1) a::text').get()
            district = tr.css('td:nth-child(2)::text').get()
            streets.append(Street(district=district, street=street, lat=lat, long=long))
        return streets
