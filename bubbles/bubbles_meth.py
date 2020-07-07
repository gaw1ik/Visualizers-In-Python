# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 16:36:24 2020

@author: Brian
"""

#%% Setup Environment

from IPython import get_ipython
get_ipython().magic('reset -sf')

import numpy as np

from PIL import Image, ImageDraw

from random import seed, choice, random

#%% Inputs

s = 200 # width and height of frame
nframes = 200 # number of frames

pop_active = 1 # turn popping on/off (1=on, 0=off)
pop_thresh = s/4

r0s = [1] # choice sequence for initial radii
grow = 2 # choice sequence for growth rate

mx, my = s/400, s/200 # this sets the motion directory

jit_size = s/100

color_mode = 'random' 
color_const = (255,200,170)

rarity = 6 # rarity parameter (creates a choice sequence with this many 0's and one 1)

#%%

def choose_color(color_mode):
    if color_mode=='constant':
        color = color_const # some constant color
    elif color_mode=='random':
        c_seq = np.arange(150,260,5)
        color = (choice(c_seq),choice(c_seq),choice(c_seq))
    return color

    
#%% Make Bubble Class
    
class bubble:
    
    # Initializer / Instance Attributes
    def __init__(self, center, radius, color):
        
        self.center = center
        self.radius = radius
        self.color  = color        
        
    def draw(self,im):
        
        cx, cy = self.center[0], self.center[1]
        radius = self.radius
        x1,x2 = cx-radius, cx+radius
        y1,y2 = cy-radius, cy+radius
        xy = [x1,y1,x2,y2]
        draw = ImageDraw.Draw(im)
        draw.ellipse(xy,outline=bubb.color)
        
    def grow(self,grow):
        
        self.radius = self.radius + grow
     
    def jitter(self,jit_size):
        cx, cy = self.center[0], self.center[1]
        jit_x = choice([-jit_size,0,jit_size])
        jit_y = choice([-jit_size,0,jit_size])
        self.center = [cx+jit_x, cy+jit_y]        
        
    def move(self,mx,my):
        
        cx, cy = self.center[0], self.center[1]
        self.center = [cx+mx, cy+my]
        
    def pop(self, popped_list):
        
        fade = 0.6
        
        # If the brightness is low enough we'll consider it totally popped
        if self.color[0]<10:
            popped_list.append(i-1)
           
        # If the radius is large enough we'll initiate the popping sequence
        if self.radius>pop_thresh:
            self.radius = self.radius*1.05
            self.color = (np.uint8(self.color[0]*fade), np.uint8(self.color[1]*fade), np.uint8(self.color[2]*fade))
        
        return popped_list
    
#%% Make the images for the GIF
        
images = []
bubbles = []
seed(1)
pop = 0 

# Setup "frames" list (frame numbers)
frames = []
for f in range(nframes):
    frames.append(f)

# Setup bubble start choice sequence
bub_chance = [0]*rarity
bub_chance.append(1)

# Create a blank frame
blank = np.zeros([s, s, 3],dtype=np.uint8) 

# Make each frame
for f in frames:
    
    im = Image.fromarray(blank)
    
    start = choice(bub_chance)
    
    # Randomly instantiate new bubbles
    if start==1: 
        
        r0 = choice(r0s)
        cx, cy = random()*s, random()*s
        color = choose_color(color_mode) # choose random color
        new_bubble = bubble([cx,cy],r0,color)
        bubbles.append(new_bubble)
    
    # Draw each bubble and update their attributes
    popped_list = []
    for i, bubb in enumerate(bubbles, 1): 
        
        # Draw the bubble
        bubb.draw(im)
        
        # Grow the bubble for the next frame
        bubb.grow(grow)
        
        # Jitter the bubble for the next frame 
        bubb.jitter(jit_size)
        
        # Move the bubble for the next frame
        bubb.move(mx,my)
        
        # Pop the bubble stuff
        if pop_active==1:
            popped_list = bubb.pop(popped_list)

    # Pop the bubble stuff
    if len(popped_list)>0:
        for i in popped_list: del bubbles[i]
            
    images.append(im)

#%% Save as GIF
    
images[0].save('bubbles_1_meth.gif',
               save_all=True,
               append_images=images[1:],
               optimize=False,
               duration=1000/24,
               loop=0)

print('DONE')