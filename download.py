import xmltodict
import urllib.request
import os

f=open('PFC DL.xml').read()
d=xmltodict.parse(f)
elements=d['Schedule']['ScheduledEvent']['ScheduledElement']

os.makedirs('downloads')

for i in elements:
    url = i['EventData']['PrivateInformation']['LibraryItem']['FileSource']
    title = i['EventData']['PrivateInformation']['LibraryItem']['Title']
    print(url)
    print(title)
    print("downloading")
    file = urllib.request.urlretrieve(url, f"downloads/{title}.mp4")
    print()

