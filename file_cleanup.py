import os
folder_original = '/Users/long/Desktop/'
folder_destination = '/Users/long/Desktop/Cleanedup/'

os.mkdir(folder_destination)

for entry in os.scandir(folder_original):
    location_original = os.path.join(folder_original, 'new.txt')
    location_destination = os.path.join(folder_destination, 'new.txt')

    if os.path.isfile(location_original):
        os.rename(location_original, location_destination)
    if not os.path.isfile(location_original):
        print('All are Directories!!!')





