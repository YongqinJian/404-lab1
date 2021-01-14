import requests

#print(requests.__version__)

home_page = requests.get('http://google.com/')

my_script = requests.get('https://raw.githubusercontent.com/YongqinJian/404-lab1/main/lab1.py')
print(my_script.text)
