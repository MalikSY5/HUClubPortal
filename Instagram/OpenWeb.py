from urllib import request
from InstagramGrabber import Organization
import webbrowser
# Runs the function from InstagramGrabber
database = Organization()
# Currently a place holder. Further into project cycle this will be replaced with a function that grabs the post depending on what the user has entered.
request = 'howardnsbe'
# Grabs link and opens the post on a webrowser.
for i in database:
    if i == request:
        webbrowser.open(database[i][0][0])

