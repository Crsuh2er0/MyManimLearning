
from big_ol_pile_of_manim_imports import *

class Hello_World(Scene):

     def construct(self):

         helloworld = TextMobject("Hello World!", color=RED)



         self.play(Write(helloworld))
         self.wait(1)
