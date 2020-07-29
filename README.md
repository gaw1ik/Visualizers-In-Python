# Python GIF Animations (a work in progress)

<p style="text-align:center">
   <img src="https://github.com/gaw1ik/visualizers/blob/master/pulsars/pulsars_2.gif" width="32%"/>  
  <img src="https://github.com/gaw1ik/visualizers/blob/master/pulsars/pulsars_7.gif" width="32%"/> 
  <img src="https://github.com/gaw1ik/visualizers/blob/master/pulsars/pulsars_6.gif" width="32%"/>   
</p>

This project centers around the creation of short animations (shown here as GIFs) using Python scripts. One of the primary goals for these animations is to be used as clips for music visualizers, but the animations are still pretty interesting as standalone clips. 

Each type of animation (e.g. bubbles) is built on a single script which is written in an object oriented manner and is intended to be usable entirely from the "Inputs" section of the script only. The scripts are highly functionalized, and all the example GIFs you see for each one are made just by changing the input paramaters. The resulting GIF should save to your current working directory under the filename which you define at the top of the Inputs section.  

Many of the classes are pursued with an original concept in mind - like twinkling stars, for instance - but because of the high degree of funcionality in the scripts, the resulting classes can produce a much wider range of visual aesthetics, often completely deviating from the original concept. Furthermore, some of the classes create a visual that is fairly unfamiliar, and as I continue working on the project, I can see the naming becoming more and more difficult.

I think this is a really great foundation for a potential application centered around creating visuals in which the user can select from any number of "sprites" (e.g. bubbles, stars, rain, pulsars, etc.) and tweak/keyframe a limited, but powerful set of parameters to create really interesting effects, especially for ceating music visualizers! I have used these animations in combination with video editing software before with great results. If they aren't cool enough on their own, the ability to time-stretch, zoom, rotate, fade-in/fade-out, etc. makes for incredibly cool visuals that can be timed to music. 

I continue to evolve the general architecture of these scripts, adding features like the option to select from different color palettes (e.g. 'warm','forest','rainbow'), various motion options, etc. The architecture is not super mature yet, but is heading in a fairly cohesive direction in which objects have there own unique properties, but at some point there may be "global" attributes as well that can be added to animations such as color palettes, fades, zooms, motion, etc. This could be cool for adding a panning effect through the stars, for instance (a la Star Wars).   

Obviously, Python doesn't really lend itself to creating amazing user interfaces, which is sad, but a future rendition of this project could involve mocking it up in Javascript and including a GUI. It would be super nice if the parameters could be changed in real-time instead of having to save a GIF and open it to view the impact of parameter changes. And as I said before, ultimately, it would be excellent if parameters could also be timed to video using keyframing. 

## Bubbles

<p style="text-align:center">
  <img src="https://github.com/gaw1ik/visualizers/blob/master/bubbles/bubbles_1.gif" width="24%"/>
  <img src="https://github.com/gaw1ik/visualizers/blob/master/bubbles/bubbles_2.gif" width="24%"/>
  <img src="https://github.com/gaw1ik/visualizers/blob/master/bubbles/bubbles_3.gif" width="24%"/>
  <img src="https://github.com/gaw1ik/visualizers/blob/master/bubbles/bubbles_4.gif" width="24%"/>
</p>

The bubble animations make use of the PIL library which allows for drawing of basic shapes such as circles (actually ellipses). In order to get the bubbly effect, small circles are drawn at random (both in space and time) which then grow in size over the remaining duration of the GIF. Each bubble is tracked as its own object instance (of the class bubble) with its own unique set of instantaneous attributes (center location, radius, and color) and various methods for growing, jittering, moving, and being drawn. Note that the PIL draw function accepts top-left and bottom-right coordinates of the ellipse's bounding box, so in the method draw a conversion is done between center point/radius and these coordinates before drawing is done. 

The GIF is structured as a sequence of images containing *nframes* frames. The code loops through each frame, one at a time, updates the attributes of each bubble in that frame, and then draws each bubble using the draw method. The result is a two-level nested for-loop. Growth is imparted to the bubbles via the grow method which adds an amount *grow* to the bubble radius. Motion is imparted to the bubbles using the method move by adding the amount *mx* and *my* to to the center x and y coordinates respectively. Jitter is added to the bubbles via the jitter method which randomly adds or subtracts the value *jit* to the center coordinates. Bubble color is set for each bubble using the function choose_color. There are two modes which can be used for color assignement: constant, in which all the bubbles have the same color (as defined by the user) or random in which each bubble's color is chosen randomly from a predefined range of colors. Finally, the bubbles can undergo a "popping" animation by using the method pop. This method has the radius quickly increase while the brightness of the bubble outline quickly decreases. Once the brightness has gone below a certain level, the bubble object is deleted entirely, so that fully popped bubbles aren't hanging around taking up unnecessary memory.

## Stars (also planets, orbits, cellular diffusion, etc.) 
Look closely... They're twinklin'.

<p style="text-align:center">
  <img src="https://github.com/gaw1ik/visualizers/blob/master/stars/stars_1.gif" width="24%"/>
  <img src="https://github.com/gaw1ik/visualizers/blob/master/stars/stars_2.gif" width="24%"/>
</p>

In the stars animation, a random distribution of small circles initially populates the canvas from which point the stars can then move around and change brightness. Each "star" is handled as an object with the class star. Stars are defined by attributes such as center, radius, and color. The star class has many methods to animate them including jitter and twinkle. Jitter is responsible for the movement of the stars. It can be set to two modes: "jitter" and "walk". Jitter creates movements around a fixed central point, whereas walk creates a random walk effect. The random walk effect lends itself well to making more of a cellular, atomistic diffusion type visual. Twinkle allows for the brightness of the stars to change throughout the GIF giving that twinkly star effect.

Originally, this script was intended to make something that looked like stars, and stars only, but messing with the input parameters of the script can actually produce a much wider range of visual effects. The stars can become quite "planetary" by allowing for larger circles and also using the random color mode. Furthermore, I added the capability of choosing between outlined circles and filled circles. Choosing the outlined circles produces a cellular visual at times and at other times - particularly when the size distribution is large - can start to look reminiscent of planetary orbits. 

<p style="text-align:center">
  <img src="https://github.com/gaw1ik/visualizers/blob/master/stars/stars_3.gif" width="24%"/>
  <img src="https://github.com/gaw1ik/visualizers/blob/master/stars/stars_4.gif" width="24%"/>
</p>

This script uses the pycairo library, which I wanted to try instead of PIL and Skimage because it is built on fractional units (e.g. circle radius is set to a fraction of the overall canvas width), which can make resizing things very convenient. Also, the PIL draw function does not do well drawing very small circles. They end up looking like squares, whereas pycairo allows you to draw very small circles. I still make use of PIL, however, because the final conversion to GIF uses PIL. Thus, I needed a way to convert cairo surfaces to PIL images. I made use of a function found here: http://www.casualhacker.net/post/2013-06-02-convert-pycairo-argb32-surface-to-pil-rgb-image/. Also note that Pycairo was somewhat difficult to install. I might add some instructions for that. It was something I did a long time ago.

## Snow/Rain
<p>Probably more on the snow end of the spectrum.</p>
<p style="align:center">
  <img src="https://github.com/gaw1ik/visualizers/blob/master/snow-rain/snow2.gif" width="24%"/>
  <img src="https://github.com/gaw1ik/visualizers/blob/master/snow-rain/snow3.gif" width="24%"/>
  <img src="https://github.com/gaw1ik/visualizers/blob/master/snow-rain/snow2.gif" width="24%"/>
  <img src="https://github.com/gaw1ik/visualizers/blob/master/snow-rain/snow3.gif" width="24%"/>
</p>
