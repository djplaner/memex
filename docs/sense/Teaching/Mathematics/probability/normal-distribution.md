<!--
 Copyright (C) 2023 David Jones
 
 This file is part of memex.
 
 memex is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.
 
 memex is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.
 
 You should have received a copy of the GNU General Public License
 along with memex.  If not, see <http://www.gnu.org/licenses/>.
-->

# Normal (Gaussian) distribution



## Why it seems everywhere and why under closer inspection it is almost nowhere.

Normal distribution is based on the assumption that

1. all individual variables have finite variance; and
2. they are independent.

A [thread by @filippie509](https://threadreaderapp.com/thread/1652487779308437505.html) on Thread Reader App - Clipped on Tuesday, May 2, 2023, 9:16 AM


A little thread on how Gaussian (aka Normal) distribution arises, why it seems to be everywhere and why under closer inspection it is almost nowhere. Jump in👇 [![Image](https://pbs.twimg.com/media/Fu7MxT5aYAMUm4p.jpg)](https://pbs.twimg.com/media/Fu7MxT5aYAMUm4p.jpg) 

Gaussian distribution is so prevalent, because it arises as a limit of averaging out many independent random variables with finite variance. This fundamental law of statistics is called a Central Limit Theorem or CLT. [en.wikipedia.org/wiki/Central\_l…](https://en.wikipedia.org/wiki/Central_limit_theorem) [![Image](https://pbs.twimg.com/media/Fu7NX3zaUAE3Suz.jpg)](https://pbs.twimg.com/media/Fu7NX3zaUAE3Suz.jpg) 

This can be very well seen in a little simulation below: 200x400 grid (so 80000) independent random variables with uniform distribution (-0.5,0.5) are simulated and a histogram of averages are taken and plotted below, clearly showing bell curve as expected.   
  
  
![Video Poster](https://pbs.twimg.com/ext_tw_video_thumb/1652484562096885762/pu/img/icpCB05c_xExX1yI.jpg) 

So we are done now? What else is there to say? Well... there are two main assumptions of CLT. First that all individual variables have finite variance. And that is most of the time the case. But second that they are independent. And that is when things are a little complicated.

Because when there is even tiny bit of dependence introduced in these variables, CLT falls apart. I simulate this below by adding a small bias to all the random cells, nothing even noticeable by eye. But suddenly the averages explode into the tail of distribution:   
  
  
![Video Poster](https://pbs.twimg.com/ext_tw_video_thumb/1652485433044115456/pu/img/XbZYc04UUmRC4Dge.jpg) 

6 sigma, 10 sigma, 13 sigma these events should pretty much be impossible under normal distribution. A 10-Sigma would be an event that happens once every 5.249e+020 years (that's half a Septillion). But of course with slight dependence the mean of these vars is no longer Gaussian

And that often happens in real world - here everything is pretty much always slightly dependent. But often that dependence is so weak, CLT still works, and statisticians are happy, models work, and everything is great. But every now and then things suddenly get dependent.

E.g. in stock market, an index is a combination of individual stocks whose prices are mostly independent and so often behaves like a gaussian random walk. Until of course an event occurs that affects all these companies and suddenly they are dependent and you see a 10 sigma jump.

This should be taught in every statistics class as literally the first thing after CLT. But often isn't. And hence people misuse statistics and apply wrong models to complex data. Read more from [@nntaleb](https://twitter.com/nntaleb) who was an inspiration for this little thread.

BTW: Here is the code snippet I wrote to generate these animations if you want to fiddle with it [github.com/piekniewski/ra…](https://github.com/piekniewski/random/blob/main/gauss/gaussian_experiment.py)


