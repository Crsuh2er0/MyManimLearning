from big_ol_pile_of_manim_imports import *


class Invoker(Scene):
    CONFIG = {'ice': 'my_code\\Invoker_problem\\ice.png',
              'wex': 'my_code\\Invoker_problem\\wex.png',
              'fire': 'my_code\\Invoker_problem\\fire.png'}

    def construct(self):
        ice = ImageMobject(self.ice)
        ice.set_height(1.)
        wex = ImageMobject(self.wex)
        wex.set_height((1.))
        fire = ImageMobject(self.fire)
        fire.set_height(1.)

        wex.shift(UP * 0.6)
        ice.next_to(wex, LEFT)
        fire.next_to(wex, RIGHT)

        text01 = TextMobject("I N V O K E R")
        text01.set_width(3.2)
        text01.next_to(wex, DOWN)

        self.play(FadeInFromLarge(ice), run_time=1.5)
        self.play(FadeInFromLarge(wex), run_time=1.5)
        self.play(FadeInFromLarge(fire), run_time=1.5)

        self.play(Write(text01), run_time=1.5)
        self.wait(1)
