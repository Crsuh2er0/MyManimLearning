from big_ol_pile_of_manim_imports import *


class Example(Scene):

    def construct(self):

        equal = TextMobject("k",color=RED)
        eq_left01 = TextMobject("$1^3+2^3+3^3+\\quad\\dots\\quad+n^3$",color=GREEN)
        eq_right01 = TextMobject("$(1+2+3+\\quad\\dots\\quad+n)^2$",color=YELLOW)

        eq_left02 = TextMobject("$\\Sigma_{i=1}^{n} i^{3}$",color=GREEN)
        eq_right02 = TextMobject("$(\\Sigma_{i=1}^{n} i)^{2}$",color=YELLOW)
        equation02 = VGroup(equal,eq_left02,eq_right02)

        eq_left01.next_to(equal,LEFT)
        eq_left02.next_to(equal,LEFT)
        eq_right01.next_to(equal,RIGHT)
        eq_right02.next_to(equal,RIGHT)

        self.play(FadeIn(eq_left01),FadeIn(equal),FadeIn(eq_right01))
        self.wait(1)
        self.play(ReplacementTransform(eq_left01,eq_left02))
        self.play(ReplacementTransform(eq_right01,eq_right02))
        self.wait(1)
        self.play(ApplyMethod(equation02.scale,2.4))
        self.wait(1)