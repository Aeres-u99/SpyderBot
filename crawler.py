import requests
import re
from bs4 import BeautifulSoup

URL="http://sdev2.flairfirst.com/"
query = "Contact us"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')
#print(soup.prettify())

print("=========================================================")
output = {}
contact_us = []
query_test=""
for link in soup.find_all('a'):
    output[link.get_text().lower()]=link.get("href")
    #print("-"*10)
    #print(link.get("href"))
    #print("=>")
    print("-------------------------------------------------")
    print(link.get_text())
    print("-------------------------------------------------")
print("\/\/\/\/\/\/\/\/\//\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
print(output.keys())

theset = set(k.lower() for k in output)
if query.lower() in output:
    print("found")
    print(output[query.lower()])
#print(output.values())
