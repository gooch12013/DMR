import requests
Pass = "thegooch1"
un = "KJ4MSN"

url = "http://xmldata.qrz.com/xml/current/?username="+ un + ";password=" + Pass + ";agent=q5.0"

print(url)
response = requests.get(url)
with open('auth.xml', 'wb') as file:
    file.write(response.content)