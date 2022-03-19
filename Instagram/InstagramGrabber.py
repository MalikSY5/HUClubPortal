from copyreg import pickle
from instagramy import InstagramUser
import pickle

""" This file handles generating the links for the specified user. The links are then stored in a dictionary format in the Data.txt file that we then 
to open the posts for the desiered organization name """
# Function to add organization to database
def Organization():
    
    name = input('Enter a org please!:')
    # Finds the user/org
    user = InstagramUser(name)
    #Temporary data holder
    temp_database = {}

    count = 0
    data = []
    # Loops through users posts and collects links
    for i in user.posts:
        while count != 3:
            data.append([i[7], i[8]])
            count += 1
        if count == 3:
            
    # Opens Data.txt tpo receive database
    a_file = open('Data.txt', 'rb')
    updated_database = pickle.load(a_file)
    # Adds tempoary data to database and updates it
    updated_database[name] = data
    a_file.close
    a_file = open('Data.txt', 'wb')
    # Saves updated database into Data.txt file
    pickle.dump(updated_database, a_file)
    a_file.close()
    # Returns the database
    return updated_database

