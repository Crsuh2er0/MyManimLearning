from big_ol_pile_of_manim_imports import *


class LuXun(Scene):
    def construct(self):
        quote = TextMobject("使用manim制作数学动画很有意思")
        quote.set_color(RED)
        quote.to_edge(UP)
        quote2 = TextMobject("Making animation by Manim is funny.")
        quote2.set_color(BLUE)
        author = TextMobject("-鲁迅", color=PINK)

        author.next_to(quote.get_corner(DOWN + RIGHT), DOWN)

        self.add(quote)
        self.add(author)
        self.wait(2)
        self.play(Transform(quote, quote2),
                  ApplyMethod(author.move_to, quote2.get_corner(DOWN + RIGHT) + DOWN + 2 * LEFT))
        self.play(ApplyMethod(author.scale, 1.6))
        author.match_color(quote2)
        self.play(FadeOut(quote), FadeOut(author))
        self.wait()
