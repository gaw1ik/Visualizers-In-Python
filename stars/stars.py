# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 00:08:46 2020

@author: Brian
"""

#%% Setup Environment

from IPython import get_ipython
get_ipython().magic('reset -sf')

import numpy as np

import math

import cairo

from PIL import Image

from random import seed, choice, random

#%% Inputs

filename = 'stars_4.gif'

s = 1 # width and height of frame
nframes = 100 # number of frames

seed_number = 5

pixel_scale = 200

n_stars = 50

r_seq = np.arange(0.0010,0.0030,0.0001)*10# choice sequence for initial radii

bright_seq = np.arange(0.6, 0.8, 0.05)

mx, my = 0, 0 # this sets the motion directory

jit_size = 0.01

# color_mode = 'constant' 
# color_const = [255,255,210]

const_color = [0.5,1,1]

#%%

# def choose_color(color_mode):
#     if color_mode=='constant':
#         color = color_const # some constant color
#     elif color_mode=='random':
#         c_seq = np.arange(150,260,5)
#         color = [choice(c_seq),choice(c_seq),choice(c_seq)]
#     return color

    
#%% Make star Class
    
class star:
    
    # Initializer / Instance Attributes
    def __init__(self, center, radius, color):
        
        self.center = center
        self.radius = radius
        self.color  = color        
        
    def draw(self,ctx):
        
        ctx.set_source_rgb(self.color[0], self.color[1], self.color[2])
        ctx.arc(self.center[0], self.center[1], self.radius, 0, 2*math.pi)
        # ctx.fill()
        ctx.set_line_width(0.004)
        ctx.stroke()
        
    def twinkle(self,bright_seq):
        
        b = choice(bright_seq)
        self.color = [const_color[0]*b, const_color[1]*b, const_color[2]*b]
     
    def jitter(self,jit_size):
        
        cx, cy = self.center[0], self.center[1]
        jit_seq = [-jit_size] + [0]*5 + [jit_size]
        jit_x = choice(jit_seq)
        jit_y = choice(jit_seq)
        self.center = [cx+jit_x, cy+jit_y]        
        
    def move(self,mx,my):
        
        cx, cy = self.center[0], self.center[1]
        self.center = [cx+mx, cy+my]

#%%
def pilImageFromCairoSurface( surface ):
   cairoFormat = surface.get_format()
   if cairoFormat == cairo.FORMAT_ARGB32:
      pilMode = 'RGB'
      # Cairo has ARGB. Convert this to RGB for PIL which supports only RGB or
      # RGBA.
      argbArray = np.frombuffer( bytes(surface.get_data()), 'c' ).reshape( -1, 4 )
      rgbArray = argbArray[ :, 2::-1 ]
      pilData = rgbArray.reshape( -1 ).tostring()
   else:
      raise ValueError( 'Unsupported cairo format: %d' % cairoFormat )
   pilImage = Image.frombuffer( pilMode,
         ( surface.get_width(), surface.get_height() ), pilData, "raw",
         pilMode, 0, 1 )
   pilImage = pilImage.convert( 'RGB' )
   return pilImage

#%% Determine random starting positions for stars

r_seq = list(r_seq)

bright_seq = list(bright_seq)

stars = []

seed(seed_number)

for _ in range(n_stars):
    cx = random()*s
    cy = random()*s
    r0 = choice(r_seq)
    b = choice(bright_seq)
    c0 = [b, b, 0.8*b]
    # c0 = (np.uint8(choice(c_seq)*255),np.uint8(choice(c_seq)*255),np.uint8(choice(c_seq)*255))
    new_starro = star( [cx, cy], r0, c0 )
    stars.append(new_starro)

#%% Make the images for the GIF  
images = []
seed(1)

# Setup "frames" list (frame numbers)
frames = []
for f in range(nframes):
    frames.append(f)

# Make each frame
for f in frames:
    
    # initialize the blank canvas each frame
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, s*pixel_scale, s*pixel_scale)
    ctx = cairo.Context(surface)
    ctx.scale(pixel_scale, pixel_scale)  # Normalizing the canvas
    
    # Draw each star and update their attributes
    for i, starro in enumerate(stars, 1): 
        
        # Draw the star
        starro.draw(ctx)
        
        # Twinkle the star
        starro.twinkle(bright_seq)
        
        # Jitter the star for the next frame 
        starro.jitter(jit_size)
        
        # Move the star for the next frame
        starro.move(mx,my)
         
    im = pilImageFromCairoSurface(surface)
    
    images.append(im)

#%% Save as GIF
    
images[0].save(filename,
               save_all=True,
               append_images=images[1:],
               optimize=False,
               duration=1000/24*3,
               loop=0)

print('DONE')