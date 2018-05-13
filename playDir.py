from bs4 import BeautifulSoup
import requests
import sys, subprocess

URL = sys.argv[1]
r = requests.get(URL)
soup = BeautifulSoup(r.text, 'html.parser')

for vid in soup.find_all('a'):
    url = "{0}{1}".format(URL, vid.get('href'))
    print("Playing: {0}{1}".format(URL, vid.get('href')))
    subprocess.call(["mpv", url])
