''' sprites :
1. pillar
2. bird
3. background
4. grond

# the camera has to move with the bird
which can be achieved by a visual illusion all the other sprites except the bird keep moving backward
and the bird stays in the same place which feels like the bird is moving forward 
the ground, background and the pillars have to re-render. 
also the pillars has to be both on the ground and hanging from the top


# model.

every time the bird successfully manuvers through the pillars it gains a point. 
if it touches any of the pillars it loses a life.
 
the bird has two controls moving up and down.
the amount by which it moves up or down is determined by the duration of the key press.


# AI 
once the model is defined we have all the parameters required for an ai model to train on
actions: 1.up  2.down 3.if possible a weight parameter to determine the amount of either action.

reward: 1.the score itself

state: could be the pixel input(lot of data) or the position of pillars in each frame.'''

import pygame 



