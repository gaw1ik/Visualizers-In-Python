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

filename = 'stars_1.gif'

# GIF Options
s = 1 # width and height of frame
nframes = 200 # number of frames
frame_duration = 1000/24*3
pixel_scale = 400

# Size/Arrangement Options
seed_number = 8
n_stars = 50
r_seq = np.arange(0.0010,0.0040,0.0001)*2.5# choice sequence for initial radii
# r_seq = [0.010]*50 + [0.030]*20 + [0.140]*5

# Twinlke Options
# bright_seq = np.arange(0.6, 0.8, 0.05)
bright_seq = [0.8]*5 + [1]
# bright_seq = [1]

# Jitter Options
jitter_mode = 'jitter'
jit_size = 0.0005
jit_seq = [-jit_size] + [0] + [jit_size]

# Color Options
color_mode = 'constant' 
fill_mode = 'fill'
line_thickness = 0.01
color_const = [1,1,0.8]
c_seq = np.arange(0.5,1.05,0.05)

#%%

def choose_color(color_mode,c_seq):
    if color_mode=='constant':
        b = choice([0.3,0.6,1.0])
        color = [color_const[0]*b,color_const[1]*b,color_const[2]*b] # some constant color
    elif color_mode=='random':
        # c_seq = np.arange(0.5,1.05,0.05)
        color = [choice(c_seq),choice(c_seq),choice(c_seq)]
    return color

    
#%% Make star Class
    
class star:
    
    # Initializer / Instance Attributes
    def __init__(self, base_center, radius, base_color):
        
        self.base_center = base_center
        self.inst_center = base_center
        self.radius = radius
        self.base_color = base_color 
        self.inst_color = base_color
        
    def draw(self,ctx,fill_mode):
        
        ctx.set_source_rgb(self.inst_color[0], self.inst_color[1], self.inst_color[2])
        ctx.arc(self.inst_center[0], self.inst_center[1], self.radius, 0, 2*math.pi)
        if (fill_mode=='fill'):
            ctx.fill()
        elif (fill_mode=='outline'):
            ctx.set_line_width(line_thickness)
            ctx.stroke()
        
    def twinkle(self,bright_seq):
        
        b = choice(bright_seq)
        self.inst_color = [self.base_color[0]*b, self.base_color[1]*b, self.base_color[2]*b]
     
    def jitter(self,jit_size,jit_seq,jitter_mode):
        if (jitter_mode=='jitter'):
            cx, cy = self.base_center[0], self.base_center[1]
        elif (jitter_mode=='walk'):        
            cx, cy = self.inst_center[0], self.inst_center[1]
        jit_x, jit_y = choice(jit_seq), choice(jit_seq)
        self.inst_center = [cx+jit_x, cy+jit_y]        

#%% Function for converting cairo surface to PIL image
        
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
    c0 = choose_color(color_mode,c_seq)
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
        starro.draw(ctx,fill_mode)
        
        # Twinkle the star
        starro.twinkle(bright_seq)
        
        # Jitter the star for the next frame 
        starro.jitter(jit_size,jit_seq,jitter_mode)
        
        # Move the star for the next frame
        # starro.walk(walk_size)
         
    im = pilImageFromCairoSurface(surface)
    
    images.append(im)

#%% Save as GIF
    
images[0].save(filename,
               save_all=True,
               append_images=images[1:],
               optimize=False,
               duration=frame_duration,
               loop=0)

print('DONE')