from parsel import Selector


def get_districts():
    with open("district_grubber/ria.html", "r+") as file1:
        selector = Selector(file1.read())
        current_district = ''
        districts = {}
        for district in selector.css('.list-columns .scrollbar > div'):
            class_name = district.css('::attr(class)').get()
            if class_name == 'region-group-header':
                current_district = district.css('label::text').get()
                districts[current_district] = []
            if class_name == 'region-group-item':
                micro_district = district.css('label::text').get()
                districts[current_district].append(micro_district)
        return districts


print(get_districts())
