# Python GIF Animations
This project centers around the creation of short animations using Python script. One of the primary goals for these animations is to be used as clips for music visualizers, but the animations can also be used to create standalone GIFs or videos. 

<b>Note: This repo is under construction. I need to organize it better and add the code for each example, but I've gone ahead and made this public to show the results.</b>

## Bubbles
The bubble animations make use of the PIL library which allows for drawing of different basic shapes such as circles (actually ellipses). In order to get the bubbly effect, small circles are drawn in the frame which then grow in size over the remaining duration of the GIF. Each bubble is tracked as its own instance with its own unique set of current coordinates (top-left and bottom-right of the ellipse's bounding box) which change over time. Bubbles are initialized randomly in both time and spatial location. Growth is imparted to the bubbles by subtracting an amount (grow) from the top-left coordinate and adding that same amount to the bottom-right coordinate. Motion is imparted to the bubbles by adding an equal amount (m) to the top-left and bottom-right coordinates of the circles. Bubble color is currently defined globally, as in it applies to all the bubbles, but can still change from frame to frame.

<p style="text-align:center">
  <img src="https://github.com/gaw1ik/visualizers/blob/master/bubbles/bubbles_1.gif" width="24%"/>
  <img src="https://github.com/gaw1ik/visualizers/blob/master/bubbles/bubbles_2.gif" width="24%"/>
  <img src="https://github.com/gaw1ik/visualizers/blob/master/bubbles/bubbles_drift_1.gif" width="24%"/>
  <img src="https://github.com/gaw1ik/visualizers/blob/master/bubbles/bubbles_shake_1.gif" width="24%"/>
</p>

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

## Twinkly Stars
<p>Look closely... They're twinklin'.</p>
<p style="align:center">
  <img src="https://github.com/gaw1ik/visualizers/blob/master/stars/stars_1.gif" width="100%"/>
</p>

## Snow/Rain
<p>Probably more on the snow end of the spectrum.</p>
<p style="align:center">
  <img src="https://github.com/gaw1ik/visualizers/blob/master/snow-rain/snow2.gif" width="24%"/>
  <img src="https://github.com/gaw1ik/visualizers/blob/master/snow-rain/snow3.gif" width="24%"/>
</p>
