# Author: Josh Huang

import os
from datetime import datetime

class Camera:
    def __init__(self):
        print("camera initiated")
        
    def capture(self, folder="images", filename=None):
        '''
        Captures an image and saves it to specific folder and filename
        if no parameters given it will save to images folder by default with current time as filename
        '''
        # set filename to date time if no filename given
        if filename == None:
            filename = datetime.now().strftime("%m-%d-%Y_%H-%M-%S")
        
        # create folder if folder not exist
        isExist = os.path.exists(folder)
        if not isExist:
            # Create a new directory because it does not exist
            os.makedirs(folder)
            
        # take picture and save
        os.system(f"libcamera-still -o {folder}/{filename}.jpg --immediate")