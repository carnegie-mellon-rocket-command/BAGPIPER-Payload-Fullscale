# Author: Josh Huang

# Dependencies: install Pillow
from PIL import Image, ImageOps, ImageFilter, ImageDraw, ImageFont
import os
from datetime import datetime

class Camera:
    
    def __init__(self):
        self.filters = dict({'gray': False, 'rotation': 0, 'contour': False})
        print("camera initiated")
        
    def capture(self, folder="images", filename=None):
        '''
        Captures an image and saves it to specific folder and filename
        if no parameters given it will save to images folder by default with current time as filename
        '''
        # set filename to date time if no filename given
        if filename == None:
            filename = datetime.now().strftime("%m-%d-%Y_%H-%M-%S")
        
        # set folder to be in images
        if folder != "images":
            folder = "images/" + folder
        
        # create folder if folder not exist
        isExist = os.path.exists(folder)
        if not isExist:
            # Create a new directory because it does not exist
            os.makedirs(folder)
            
        # set final file name
        fname = f"{folder}/{filename}.jpg"
        
        # take picture and save
        os.system(f"sudo libcamera-still -n -o {fname} --immediate")
        
        # apply filters
        if self.filters['gray']:
            self.grayscale(fname)
        if self.filters['contour']:
            self.contour(fname)
            
        self.rotate(self.filters['rotation'], fname)
        self.timestamp(fname)
        
       
    ### FILTERS ###
    
    # Applies a timestamp to the image, 
    # returning filtered image as pillow Image object
    def timestamp(self, filename):
        initImg = Image.open(filename)
        timeString = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        #text parameters
        width, height = initImg.size
        textSize = height/20
        textX = width/20
        textY = height/20
        textFont = ImageFont.truetype("fonts/FreeMono.ttf", int(textSize))
        
        #adding timestamp
        filteredImg = initImg
        drawObj = ImageDraw.Draw(filteredImg)
        drawObj.text(xy=(textX, textY), text=timeString, fill = (127), font=textFont)
        
        filteredImg.save(filename)
        return

    # Makes image greyscale, returning filtered image as pillow Image object
    def grayscale(self, filename):
        initImg = Image.open(filename)
        filteredImg = ImageOps.grayscale(initImg)
        
        filteredImg.save(filename)
        return

    # Flips image 180 degrees, returning filtered image as pillow Image object
    def rotate(self, degrees, filename):
        initImg = Image.open(filename)
        filteredImg = initImg.rotate(degrees)
        
        filteredImg.save(filename)
        return
    
    # Turns image into outline, returning filtered image as pillow Image object
    def contour(self, filename):
        initImg = Image.open(filename)
        filteredImg = initImg.filter(ImageFilter.CONTOUR)
        
        filteredImg.save(filename)
        return
    
    def reset_filters(self):
        self.filters['contour'] = False
    
    def reset_all(self):
        self.filters = dict({'gray': False, 'rotation': 0, 'contour': False})


def test():
    # python -c 'import camera; camera.test()'
    cam = Camera()
    experiment_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    dir = f"payload_experiment_{experiment_time}"
    
    # cam.filters['gray'] = False
    # cam.filters['contour'] = True
    # cam.filters['rotation'] += 180
    cam.capture(folder=dir, filename="test")
