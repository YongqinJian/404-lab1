import requests

print(requests.__version__)

home_page = requests.get('http://google.com/')
