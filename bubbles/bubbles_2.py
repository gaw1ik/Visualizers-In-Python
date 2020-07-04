# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 13:21:23 2020

@author: Brian
"""

#%% Setup Environment

from IPython import get_ipython
get_ipython().magic('reset -sf')

import numpy as np

from PIL import Image, ImageDraw

from random import seed, choice, random

#%% Inputs

s = 300 # width and height of frame
nframes = 200 # number of frames

#%% Setup "frames" list (frame numbers)

frames = []
for f in range(nframes):
    frames.append(f)
    
#%% Make Bubble Class
    
class bubble:
    
    # Initializer / Instance Attributes
    def __init__(self, center, radius, color):
        self.center = center
        self.radius = radius
        self.color  = color        
    
#%% Make the images for the GIF
        
images = []
r0s = [1]
grows = [5]
ms = [-0.5,0,0.5]

bub_chance = [0]*10 
bub_chance.append(1)

color = (255,255,255)

bubbles = []

seed(1)

blank = np.zeros([s, s, 3],dtype=np.uint8) # blank frame

for f in frames:
    im = Image.fromarray(blank)
    start = choice(bub_chance)
    
    if start==1: # make a new bubble
        
        r0 = choice(r0s)
        cx = random()*s
        cy = random()*s
        new_bubble = bubble([cx,cy],r0,color)
        bubbles.append(new_bubble)
        
    for _, bubb in enumerate(bubbles, 1):
        
        r  = bubb.radius
        cx = bubb.center[0]
        cy = bubb.center[1]
        x1,x2 = cx-r, cx+r
        y1,y2 = cy-r, cy+r
        xy = [x1,y1,x2,y2]
        
        draw = ImageDraw.Draw(im)
        draw.ellipse(xy,outline=bubb.color)
        
        grow = choice(grows)
        bubb.radius = r + grow

        m = choice(ms)
        mx = m
        my = m
        bubb.center = [cx+mx,cy+my]

    images.append(im)

#%% Save as GIF
    
images[0].save('bubbles_2.gif',
               save_all=True,
               append_images=images[1:],
               optimize=False,
               duration=1000/24,
               loop=0)

print('DONE')