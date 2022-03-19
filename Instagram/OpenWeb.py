from urllib import request
from InstagramGrabber import Organization
import webbrowser

database = Organization()
request = 'howardnsbe'

for i in database:
    if i == request:
        webbrowser.open(database[i][0][0])

