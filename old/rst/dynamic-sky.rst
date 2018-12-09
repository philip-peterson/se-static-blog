Dynamic Sky
###########
:date: 2012-08-03 19:18
:author: cho102997
:category: Dev Blog
:slug: dynamic-sky

.. raw:: html

   <div>

**Topic:** Dynamic Sky
 **Team Members:** Everett and Philip
 **Location:** Riven
 **Challenge:** Creating a realistic sky which can change with the time
of day and weather

.. raw:: html

   </div>

At the time of writing this dev blog post, the project of creating a
dynamic sky has been ongoing for more than ten months. We're proud to
say that now the sky is reaching its completion.

The project started with our group's dissatisfaction with our older
skies. They all had big problems which couldn't be overlooked. For
example, our oldest sky was a basic, static skybox. At that point in
time, we weren't even considering having dynamic time or weather, so it
served its purpose reasonably well. Eventually though, we grew more
ambitious and wanted to bring a full day/night cycle with realistic
weather changes to Riven. We brought in a third-party sky shader called
UniSky for last year's Mysterium demo, but we weren't satisfied with
certain limitations it had. For example, the sky tended to use flat
colors for the clouds, all the way across the sky. There was no
backlighting or shading from the sun or moon. It just didn't meet our
standards.

[caption id="attachment\_470" align="aligncenter"
width="300"]\ `|image0|`_ The original static sky texture used both in
Riven and later in Uru’s “Cleft” scene[/caption]

So we went to work designing a new way for a sky system to operate. The
original idea we had was for a static skybox to use multiple textures
(cloud alpha, cloud normals, cloud edges, etc.) to change its lighting
and composition with the time of day. It was then realized that simply
by animating this static system with pre-rendered dynamic clouds, we
could have a skybox that looked natural, was lit realistically, and
could have clouds that moved as the player worked in the game.

 

.. raw:: html

   <div>

.. raw:: html

   <center>

An early test of animated clouds.

.. raw:: html

   </center>

.. raw:: html

   </div>

 

The first iteration of this idea was flawed. Our static system was based
on a set of pre-rendered image textures, being brought separately into
the shader. We naively extended this same system to animated clouds,
without realizing that having 400 to 800 frames each for 8 texture sets
would eat up a lot of storage space and system memory.

Eventually, after several revisions of this flawed system, we agreed
that the texture sets needed to be overhauled to save space and be more
efficient for the shader to compute. The system we decided on was to
have one basic animated texture. This texture would be a grayscale
animation of soft cloud formations, which could then be modified in real
time to produce sharper cloud textures that could also morph on cue to
cover more or less of the sky, making the transition from a clear blue
sky to a gray overcast sky much smoother than in previous iterations.

 

.. raw:: html

   <div>

.. raw:: html

   <center>

A test of the very first iteration of cloudiness variation.

.. raw:: html

   </center>

.. raw:: html

   </div>

 

The whole sky architecture was also designed so that it could be
controlled using very few final variables. At this stage, there are
three main properties that control the sky: time of day, cloud speed,
and cloudiness. That isn’t to mention the complexities that depend on
time, however, such as determining the correct position of the sun and
moon as well as the proper colors of different parts of the sky. Weather
effects like rain have not yet been integrated, so there will likely be
a fourth variable (not in the sky shader itself, but in the related
systems) for raininess, to transition from a light shower to a
thunderstorm. We'll likely end up limiting any extreme weather to be
quite rare and quick, so as not to interfere with puzzle solving too
much.

 

.. raw:: html

   <div>

.. raw:: html

   <center>

Another early iteration, with improved lighting.

.. raw:: html

   </center>

.. raw:: html

   </div>

 

The lighting for the sky is all texture-based at this time. Most of the
sun and moon's influence on the sky is driven by simple black-to-white
gradients, modified by the cloudiness of the sky and the appropriate
color of the the sky, and these gradients move with the location of the
sun. The cloud layer’s transparency blocks the sunlight, naturally, as
well as part of the sun's glow. When overcast, this creates a natural
brightness in the sun's half of the sky, while maintaining the flat
haziness that defines a cloudy sky.

[caption id="attachment\_471" align="aligncenter"
width="256"]\ `|image1|`_ An animation showing all 27 frames of the
lunar cycle.[/caption]

The moon is animated as well, with 27 frames of animation representing
each daily phase. The phases fade between each other to produce a
cohesive lunar cycle. Moonlight, though it hasn't yet been made dynamic,
will be directly affected by the phase of the moon. A full moon will
illuminate the night scenes greatly, but a new moon will leave the
scenes very dark. We've planned ahead though, and have added night-time
activated lights in certain areas to make it easy to navigate Riven and
solve the puzzles even in the extreme dark.

 

.. raw:: html

   <div>

.. raw:: html

   <center>

A test of an experimental god-ray effect for the moon.

.. raw:: html

   </center>

.. raw:: html

   </div>

 

The last major change made to the sky, made during its second build in
Unity, was the addition of a backlighting effect, which harshly darkens
the centers of clouds which are blocking the sun, and softly darkens the
centers of cloud all across the sky.

 

.. raw:: html

   <div>

.. raw:: html

   <center>

A test video demonstrating cloud backlighting.

.. raw:: html

   </center>

.. raw:: html

   </div>

 

One of the problems we ran into, writing the software behind the sky,
was that we often ran out of registers (or memory slots). None of us had
ever written a shader of this size before, so we were not aware of the
way in which writing a shader is so different from writing most
programs. The main difference is that the entire program (and all its
memory) is confined to the space available in the GPU (Graphics
Processing Unit, a chip on the computer specifically for doing graphics
operations).

So, we had to write the shader to be unusually lightweight and efficient
with the memory it used. That meant storing variables for as short a
time as possible, finding the least memory-consumptive way to do certain
color-mixing operations, and finding new ways to cram data into
otherwise unused channels of our textures. It was more than a few times
that we were informed that we had “run out of constant registers” or had
“exceeded the maximum number of instruction units” and had to rework
everything from a blank slate. The final sky shader ended up being 557
standard lines of code.

The final version of the sky is flexible, determining cloud size and sky
colors all in real time. It could be adapted for use in Tay and The
233rd Age, for example, and changed to match those Ages’ color schemes.
The sky is the product of much of the last year’s development, and we
think that it’s a robust addition to Starry Expanse.

.. _|image2|: http://www.starryexpanse.com/wp-content/uploads/2012/08/clftsky3small-800-0-hsm.jpeg
.. _|image3|: http://www.starryexpanse.com/wp-content/uploads/2012/08/moon.gif

.. |image0| image:: http://www.starryexpanse.com/wp-content/uploads/2012/08/clftsky3small-800-0-hsm-300x108.jpeg
.. |image1| image:: http://www.starryexpanse.com/wp-content/uploads/2012/08/moon.gif
.. |image2| image:: http://www.starryexpanse.com/wp-content/uploads/2012/08/clftsky3small-800-0-hsm-300x108.jpeg
.. |image3| image:: http://www.starryexpanse.com/wp-content/uploads/2012/08/moon.gif
