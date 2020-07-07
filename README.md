# Python GIF Animations
This project centers around the creation of short animations using Python script. One of the primary goals for these animations is to be used as clips for music visualizers, but the animations can also be used to create standalone GIFs or videos. 

<b>Note: This repo is under construction. I need to organize it better and add the code for each example, but I've gone ahead and made this public to show the results. I'd also like to update the code to be more functionalized, so that it can be used in a more input/output style.</b>

## Bubbles

<p style="text-align:center">
  <img src="https://github.com/gaw1ik/visualizers/blob/master/bubbles/bubbles_1.gif" width="24%"/>
  <img src="https://github.com/gaw1ik/visualizers/blob/master/bubbles/bubbles_2.gif" width="24%"/>
  <img src="https://github.com/gaw1ik/visualizers/blob/master/bubbles/bubbles_drift.gif" width="24%"/>
  <img src="https://github.com/gaw1ik/visualizers/blob/master/bubbles/bubbles_shake.gif" width="24%"/>
</p>

The bubble animations make use of the PIL library which allows for drawing of different basic shapes such as circles (actually ellipses). In order to get the bubbly effect, small circles are drawn which then grow in size over the remaining duration of the GIF. Each bubble is tracked as its own object instance (of the class bubble) with its own unique set of instantaneous attributes (center location, radius, and color). Note that the PIL draw function accepts top-left and bottom-right coordinates of the ellipse's bounding box, so a conversion is done between center point/radius and these coordinates before drawing is done. 

The GIF is structured as a sequence of images containing *nframes* frames. The code loops through each frame, one at a time, and updates the properties of each bubble in that frame. The result is a two-level nested for loop. Growth is imparted to the bubbles by adding an amount *grow* to the bubble radius. Typically *grow* is kept constant, although in the cases with motion, I found that adding a little bit of variability to the growth rate gave a slightly more organic feel. To capture this functionality, possible values for *grow* are put into a list called *grows* (e.g. grows = [5,6,7]), and then *grow* is defined as a random selection from *grows* by applying the choice function. A continuous function could have been applied here instead of a random choice. Motion is handled similarly with the variables *m* and *ms*. Motion is imparted to the bubbles by adding the amount *mx* and *my* to to the center x and y coordinates respectively. In the case where the bubbles are drifting (third from left), a continuous function dependent on the current frame value *f* is defined to control the change in trajectory of the bubbles. Finally, bubble color is set for each bubble in each frame, so the bubble colors can be unique and also change from frame to frame as they do in the instances with the rainbow, strobing effect.

I thought it might be cool and very bubble'y to add a "popping" effect to the animation. After all, real bubbles don't just grow indefinitely. I added some conditional logic to "bubbles_1.py" (responsible for the first GIF) which quickly reduces the brightness of a bubble which had exceeded a certain radius (r>s/2) where *s* is the canvas width. This is done over just a few frames, so the pop happens very quickly. To further add to the popping effect, the radius is quickly increased during the pop. Once the brightness has gone below a certain level, the bubble object is deleted, so that fully popped bubbles aren't hanging around taking up unnecessary memory.

## Twinkly Stars
Look closely... They're twinklin'.

<p style="align:center">
  <img src="https://github.com/gaw1ik/visualizers/blob/master/stars/stars_1.gif" width="100%"/>
  <img src="https://github.com/gaw1ik/visualizers/blob/master/stars/stars_2.gif" width="100%"/>
</p>

In the stars animation, a random distribution of small circles is created and used to initially populate the canvas. The twinkling effect is created by adding a subtle jittering motion and brightness change to each of the stars. The jitter is triggered by adding a value randomly selected (using the choice function) from the list *m_seq* which contains a small negative value, some number of zeros, and a small positive value equal in magnitude to the negative value (e.g. *m_seq* = [-0.001, 0, 0, 0, 0, 0, 0.001]). Since the list has mostly zeros, the stars will mostly not move, but occasionally one of the non-zero values will be selected and the star will jitter. Similarly, the brightness level is randomly selected from a list called *c_seq* which contains values between 0 and 1 (e.g. *c_seq* = [0.6,0.65,0.7]). The instaneous color of each star is then defined as an RGB triplet (c, c, 0.8c) where *c=choice(c_seq)*. The blue value in the RGB triplet is made to be slightly less, so that the stars will all have a slightly yellow tint.

This script uses the pycairo library, which I wanted to try instead of PIL and Skimage because it is built on fractional units (e.g. circle radius is set to a fraction of the overall canvas width), which can make resizing things very convenient. However, I still make use of PIL, because the final conversion to GIF uses PIL. Thus, I needed a way to convert cairo surfaces to PIL images. I made use of a function found here: http://www.casualhacker.net/post/2013-06-02-convert-pycairo-argb32-surface-to-pil-rgb-image/. Also note that Pycairo was somewhat difficult to install. I might add some instructions for that. it was something I did a long time ago.



## Cool Stuff with Sine Waves
<p style="align:center">
  <img src="https://github.com/gaw1ik/visualizers/blob/master/sine/test3.gif" width="24%"/>
  <img src="https://github.com/gaw1ik/visualizers/blob/master/sine/test4.gif" width="24%"/>
</p>

## Electricity/Lightning
<p style="align:center">
  <img src="https://github.com/gaw1ik/visualizers/blob/master/electricity-lightning/6.gif" width="24%"/>
  <img src="https://github.com/gaw1ik/visualizers/blob/master/electricity-lightning/7.gif" width="24%"/>
</p>



## Snow/Rain
<p>Probably more on the snow end of the spectrum.</p>
<p style="align:center">
  <img src="https://github.com/gaw1ik/visualizers/blob/master/snow-rain/snow2.gif" width="24%"/>
  <img src="https://github.com/gaw1ik/visualizers/blob/master/snow-rain/snow3.gif" width="24%"/>
</p>
