Camera Matching
###############
:date: 2012-04-12 17:51
:author: cho102997
:category: Dev Blog
:slug: camera_matching

.. raw:: html

   <div>

**Topic:** Camera Matching
 **Team Member:** Everett
 **Location:** Boiler Island
 **Challenge:** Creating perfectly accurate scenes

.. raw:: html

   </div>

For the first post on our brand new dev blog, I thought I'd explain the
ins and outs of “camera matching”, a process we use to recreate the
environments of Riven. At the time of writing this post, I'm deep in the
process of camera matching for Boiler Island, which makes it a great
time to feature it here.

Camera matching for our project is the process of taking the original
images from Riven and using them to rebuild the scenes exactly as they
were. It's generally a process of trial and error, piecing together
information little by little until a scene begins to take shape,
matching the original line-for-line.

[caption id="" align="alignnone" width="500" caption="The Ytram cave
walkways and balcony are portrayed here in wireframe. The orange pyramid
shapes are cameras matched to images from the original."]\ `|Ytram cave
topology|`_\ [/caption]

The first step in the camera matching for any new scene is always the
same: find a predictable object to line up the first shot. You need an
object which you know for certain is an exact shape, like a circle or a
pentagon, on which to base the perspective and angle of the rest of the
scene.

For Boiler Island, that shape was the boiler. Its perfectly cylindrical
shape made it a wonderful fit to start matching with. The first shot is
very important. You have to be sure that it's nearly perfect before you
move on to matching others. If not, the errors you made in matching the
first image will greatly affect your ability to match later images,
making the entire process much more of a fumble in the dark, constantly
attempting to correct early mistakes. The boiler made the first shot
much simpler, by supplying a clear visual representation of the camera's
rotation and location in respect to the shapes of the boiler.

[caption id="" align="alignnone" width="500" caption="Matching the first
camera angle with a primitive shape representing the
boiler."]\ `|Boiler|`_\ [/caption]

Matching an exact camera angle is a tougher prospect than you might
think. Each camera basically has 7 relevant variables: X, Y and Z
location, X, Y and Z rotation, and the lens angle.

X, Y, and Z locations describe the camera's exact point-based location
in the 3D space. Figuring out the general location is usually the first
step to matching a camera. Often when figuring out location, I can use
parallel lines in the scene to estimate a general range. For example, in
the image above, the boiler is built of circular rows of bricks. By
looking at which row is completely parallel with the image itself, I can
tell that the camera is probably at a height which is level with that
row of bricks. Then I can lock the camera to that specific height and
move onto other variables.

Lens angle is the pin that holds it all together. This variable can make
or break a camera angle. Basically, lens angle describes the exact
section of perspective which is seen by a camera. When you zoom using a
camera, lens angle gets very narrow, showing only a tiny piece of a
point's perspective. Zooming out, on the other hand, shows a wider lens
angle, framing a much larger portion of the view. Needless to say,
getting this value exactly right is imperative, as it directly affects
the apparent scale of objects in the camera's view. If you can manage to
estimate the lens angle with accuracy, the rest of the matching is quite
simple.

[caption id="" align="alignnone" width="500" caption="A wireframe pan of
the balcony and Ytram cave areas' half-completed guideline
meshes."]\ `|Ytram Cave wireframe|`_\ [/caption]

Once the first shot is lined up reliably, the rest of the process is
simply branching out from that information. Then, more cameras are lined
up with the basic model. These multiple camera angles then allow more
models to be added in which match all of the current camera angles.

Sometimes, angles need to be adjusted to match new models, as well. For
example, on Boiler Island, I had most of the boiler area set up and
matching well. Then I moved ahead to matching the balcony and cliffs,
and realized that none of my camera angles were matched accurately
enough for extremely distant features to line up properly. This led to
me going back and realigning every camera angle I had set so far, so as
to match the new details of the cliff walkways and the balcony.

[caption id="" align="alignnone" width="500" caption="The exit from the
Ytram cave to the cliff walkway, matched with a wireframe of our
recreation."]\ `|Ytram Cave walkway|`_\ [/caption]

Of course, the process of camera matching is only a precursor to the
final environment. During the course of matching camera angles with the
geometry on the scene, I try to use as little detail as possible to
convey the basic lengths and angles necessary to match each new camera
angle. I do this both to keep the scene uncluttered, as I do much of my
matching work in a wireframe view, but also because what I'm building
will not be used in the final game, so dwelling on its details would be
a waste of time. The models I create during the camera matching stage
are simply to be used as guides when creating the final game assets. The
camera matching stage is very freeform and branching, whereas the final
modeling stage will likely be much more structured and organized, simply
because of the detail involved.

[caption id="" align="alignnone" width="500" caption="The newly made
Ytram cave walkway is shown here, matched with an image from the
original."]\ `|Ytram Cave with the new geometry fading in and
out|`_\ [/caption]

The stage of camera matching is certainly where we get our most
concentrated exposure to the details of Riven's original images,
exposing some of the mistakes and odd anomalies that dot the images. For
example, in an image standing by the boiler's controls, looking up
towards the pump system, you can see towards the lower left of the
screen the handle of the paper press, an object that was intended to be
completely removed from the game before it was released. (The image's
filename is "287\_bislandcrater.1590.png", for those interested enough
to look for it.)

All of this work will culminate to a set of guideline meshes which will
span the island and make the final asset creation that much more
accurate and streamlined. Camera matching, while tedious and time
consuming on its own, stands as an integral part of the process. It
allows a level of loyalty and exacting similarity to the original not
available by any other means.

.. _|image5|: /wp-content/uploads/2012/04/ytramcave-wire.jpg
.. _|image6|: /wp-content/uploads/2012/04/boiler-overlay.jpg
.. _|image7|: /wp-content/uploads/2012/04/ytramcavew.gif
.. _|image8|: /wp-content/uploads/2012/04/ytramcaveexit.jpg
.. _|image9|: /wp-content/uploads/2012/04/cam_matching.gif

.. |Ytram cave
topology| image:: /wp-content/uploads/2012/04/ytramcave-wire.jpg
.. |Boiler| image:: /wp-content/uploads/2012/04/boiler-overlay.jpg
.. |Ytram Cave
wireframe| image:: /wp-content/uploads/2012/04/ytramcavew.gif
.. |Ytram Cave
walkway| image:: /wp-content/uploads/2012/04/ytramcaveexit.jpg
.. |Ytram Cave with the new geometry fading in and
out| image:: /wp-content/uploads/2012/04/cam_matching.gif
.. |image5| image:: /wp-content/uploads/2012/04/ytramcave-wire.jpg
.. |image6| image:: /wp-content/uploads/2012/04/boiler-overlay.jpg
.. |image7| image:: /wp-content/uploads/2012/04/ytramcavew.gif
.. |image8| image:: /wp-content/uploads/2012/04/ytramcaveexit.jpg
.. |image9| image:: /wp-content/uploads/2012/04/cam_matching.gif
