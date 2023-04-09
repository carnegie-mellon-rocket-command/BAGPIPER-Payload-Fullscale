# Author: Josh Huang

# Dependencies: install Pillow
from PIL import Image, ImageOps, ImageFilter, ImageDraw, ImageFont
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
            
        # set final file name
        fname = f"{folder}/{filename}.jpg"
        # take picture and save
        os.system(f"libcamera-still -n -o {fname} --immediate")
        
        # add timestamp
        print("\nadd time stamp:")
        self.timestamp(fname)
       
    ### FILTERS ###
    
    # Applies a timestamp to the image, 
    # returning filtered image as pillow Image object
    def timestamp(self, filename):
        initImg = Image.open(filename)
        timeString = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        #text parameters
        width, height = initImg.size
        textSize = height/8
        textX = width/8
        textY = height/7
        textFont = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", textSize)
        
        #adding timestamp
        filteredImg = initImg
        drawObj = ImageDraw.Draw(filteredImg)
        drawObj.text(xy=(textX, textY), text=timeString, fill = (127, 0, 0))#, font=textFont)
        
        return filteredImg

    # Makes image greyscale, returning filtered image as pillow Image object
    def grayscale(self, filename):
        initImg = Image.open(filename)
        filteredImg = ImageOps.grayscale(initImg)
        return filteredImg

    # Flips image 180 degrees, returning filtered image as pillow Image object
    def flip(self, filename):
        initImg = Image.open(filename)
        filteredImg = initImg.rotate(180)
        return filteredImg
    
    # Turns image into outline, returning filtered image as pillow Image object
    def edges(self, filename):
        initImg = Image.open(filename)
        filteredImg = initImg.filter(ImageFilter.CONTOUR)
        return filteredImg

def test():
    # python -c 'import camera; camera.test()'
    cam = Camera()
    experiment_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    dir = f"payload_experiment_{experiment_time}"
    cam.capture(filename="test")