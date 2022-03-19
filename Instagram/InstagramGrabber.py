from copyreg import pickle
from instagramy import InstagramUser
import pickle
def Organization():
    name = input('Enter a org by their instagram name please!:')
    user = InstagramUser(name)

    temp_database = {}

    count = 0
    data = []
    for i in user.posts:
        while count != 3:
            data.append([i[7], i[8]])
            count += 1
        if count == 3:
            break
    a_file = open('Data.txt', 'rb')
    updated_database = pickle.load(a_file)
    updated_database[name] = data
    a_file.close
    a_file = open('Data.txt', 'wb')
    pickle.dump(updated_database, a_file)
    a_file.close()
    return updated_database

