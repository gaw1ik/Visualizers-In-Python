# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 12:03:51 2020

@author: Brian
"""

#!/usr/bin/env python
from IPython import get_ipython
get_ipython().magic('reset -sf')

import math
import cairo

import numpy as np

from PIL import Image

from matplotlib.pyplot import imshow, show

from random import seed, choice, random

#%% INPUTS

# s = 300 # width and height of frame
h = 1
w = 4
pixel_scale = 200
nframes = 100

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

#%% setup "frames" list (frame numbers)

images = []
frames = []
for f in range(nframes):
    frames.append(f)
    
#%% movement sequence
move = 0.0010
m_seq = [-move] + [0]*5 + [move]

#%% Determine random starting positions for stars

n_stars = 30

r_seq = np.arange(0.0010,0.0030,0.0001)*20
r_seq = list(r_seq)

c_seq = np.arange(0.6,0.7,0.05)
c_seq = list(c_seq)

stars = []
seed(2)
for _ in range(n_stars):
    stars.append( (random()*w, random()*h, choice(r_seq), choice(c_seq)) )

#%%
for f in frames:    
    
    # initialize the blank canvas each frame
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, w*pixel_scale, h*pixel_scale)
    ctx = cairo.Context(surface)
    ctx.scale(pixel_scale, pixel_scale)  # Normalizing the canvas
    
    for star in stars:
        
        cx = star[0] + choice(m_seq)
        cy = star[1] + choice(m_seq)
        r  = star[2]
        # c  = star[3] * random()
        c = choice(c_seq)
        
        ctx.set_source_rgb(c, c, 0.8*c)

        ctx.arc(cx, cy, r, 0, 2*math.pi)
        ctx.fill()

    im = pilImageFromCairoSurface(surface)
    
    images.append(im)
    
# surface.write_to_png("example.png")  # Output to PNG
    
#%% save as GIF
images[0].save('stars_2.gif',
               save_all=True,
               append_images=images[1:],
               optimize=False,
               duration=1000/24*3,
               loop=0)

print('DONE')