from big_ol_pile_of_manim_imports import *


class Latex(Scene):

    def construct(self):
        title = TextMobject("This is some \\LaTeX")
        basel = TexMobject(
            "\\sum_{n=1}^\\infty"
            "\\frac{1}{n^2} = \\frac{\\pi^2}{6}"
        )
        VGroup(title,basel).arrange(DOWN)
        self.play(
            Write(title),
            FadeInFrom(basel,UP),
        )
        self.wait()
