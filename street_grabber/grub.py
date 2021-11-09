import httpx
r = httpx.get('https://locator.ua/ua/list/kyiv/streets/n1/')

with open("result.html", "w") as file1:
    file1.write(r.text)
