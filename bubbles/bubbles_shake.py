# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 20:00:46 2020

@author: Brian
"""

#%% Setup Environment

from IPython import get_ipython
get_ipython().magic('reset -sf')

import numpy as np

from PIL import Image, ImageDraw

# from matplotlib.pyplot import imshow, show, scatter

from random import seed, choice, random

#%% Inputs
s = 300 # width and height of frame
blank = np.zeros([s, s, 3],dtype=np.uint8) #blank frame
nframes = 200

#%% Setup "frames" list (frame numbers)
frames = []
for f in range(nframes):
    frames.append(f)
    
#%% Make the images for the GIF
images = []
color = (255,255,255)
circles = []
r0s = [3,4,5,6,7,8,9]
grows = [1,2,3]
ms = [1,-1,2,-2,3,-3]

bub_chance = [0,0,0,0,1]

col_seq = np.arange(150,260,5)

seed(1)

for f in frames:
    im = Image.fromarray(blank)
    start = choice(bub_chance)
    if start==1:
        r0 = choice(r0s)
        cx = random()*s
        cy = random()*s
        x1,x2 = cx-r0, cx+r0
        y1,y2 = cy-r0, cy+r0
        circles.append([x1,y1,x2,y2])
        
    for i, xy in enumerate(circles, 1):
        colr,colg,colb = choice(col_seq),choice(col_seq),choice(col_seq)
        draw = ImageDraw.Draw(im)
        draw.ellipse(xy,outline=(colr,colg,colb))
        grow = choice(grows)
        m = choice(ms)
        xy = [xy[0]-grow+m,xy[1]-grow+m,xy[2]+grow+m,xy[3]+grow+m]
        circles[i-1] = xy
        
    images.append(im)

#%% save as GIF
images[0].save('bubbles_shake_1.gif',
               save_all=True,
               append_images=images[1:],
               optimize=False,
               duration=1000/24,
               loop=0)

print('DONE')