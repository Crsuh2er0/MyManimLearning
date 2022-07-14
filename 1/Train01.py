from big_ol_pile_of_manim_imports import *


class Train01(Scene):
    def construct(self):
        lovesquare = Square(side_length=2, color=RED, fill_color=RED, fill_opacity=0.375)
        lovecircle01 = Circle(color=RED, fill_color=RED, fill_opacity=0.375)
        lovecircle02 = Circle(color=RED, fill_color=RED, fill_opacity=0.375)
        lovecircle01.scale(1)
        lovecircle02.scale(1)

        lovesquare_copy = Square(side_length=2, color=RED, fill_color=RED, fill_opacity=0.375)
        lovecircle01_copy = Circle(color=RED, fill_color=RED, fill_opacity=0.375)
        lovecircle02_copy = Circle(color=RED, fill_color=RED, fill_opacity=0.375)

        crossrect01 = Rectangle(height=4, width=1, color=RED, fill_color=RED, fill_opacity=0.375)
        crossrect01.rotate(np.pi / 2)
        crossrect02 = Rectangle(height=4, width=1, color=RED, fill_color=RED, fill_opacity=0.375)

        crossrect01_copy = Rectangle(height=4, width=1, color=RED, fill_color=RED, fill_opacity=0.375)
        crossrect01_copy.rotate(np.pi / 2)
        crossrect02_copy = Rectangle(height=4, width=1, color=RED, fill_color=RED, fill_opacity=0.375)

        botsquare = Square(side_length=2, color=RED, fill_color=RED, fill_opacity=0.375)
        botcircle01 = Circle(color=RED, fill_color=BLACK, fill_opacity=1)
        botcircle01.scale(0.2)
        botcircle02 = Circle(color=RED, fill_color=BLACK, fill_opacity=1)
        botcircle02.scale(0.2)

        botsquare_copy = Square(side_length=2, color=RED, fill_color=RED, fill_opacity=0.375)
        botcircle01_copy = Circle(color=RED, fill_color=BLACK, fill_opacity=1)
        botcircle01_copy.scale(0.2)
        botcircle02_copy = Circle(color=RED, fill_color=BLACK, fill_opacity=1)
        botcircle02_copy.scale(0.2)

        line = Line(start=np.array([-5, -2, 0]), end=np.array([5, -2, 0]), color=RED)

        lovecircle01.shift(LEFT * 0.7072 + UP * 0.7072)
        lovecircle02.shift(RIGHT * 0.7072 + UP * 0.7072)
        lovesquare.rotate(np.pi / 4)
        love = VGroup(lovesquare, lovecircle01, lovecircle02)

        lovecircle01_copy.shift(LEFT * 0.7072 + UP * 0.7072)
        lovecircle02_copy.shift(RIGHT * 0.7072 + UP * 0.7072)
        lovesquare_copy.rotate(np.pi / 4)
        love_copy = VGroup(lovesquare_copy, lovecircle01_copy, lovecircle02_copy)

        cross = VGroup(crossrect01, crossrect02)
        cross.rotate(np.pi / 4)

        cross_copy = VGroup(crossrect01_copy, crossrect02_copy)
        cross_copy.rotate(np.pi / 4)

        botsquare.shift(np.array([4, 0, 0]))
        botcircle01.shift(np.array([3.5, 0.5, 0]))
        botcircle02.shift(np.array([4.5, 0.5, 0]))
        bot = VGroup(botsquare, botcircle01, botcircle02)

        botsquare_copy.shift(np.array([4, 0, 0]))
        botcircle01_copy.shift(np.array([3.5, 0.5, 0]))
        botcircle02_copy.shift(np.array([4.5, 0.5, 0]))
        bot_copy = VGroup(botsquare_copy, botcircle01_copy, botcircle02_copy)

        self.play(ShowCreation(love))
        self.play(ApplyMethod(love.shift, (np.array([-4, 0, 0]))))

        love_copy.shift(np.array([-4, 0, 0]))

        self.play(ShowCreation(cross))
        self.play(ShowCreation(bot))

        allcopy = VGroup(love_copy, cross_copy, bot_copy)
        allcopy.set_opacity(1)
        self.play(FadeIn(allcopy))

        self.play(ShowCreation(line))

        text = TextMobject("LOVE DEATH + ROBOTS", color=RED)
        text.shift(DOWN * 2)
        self.play(Transform(line, text))

        all = VGroup(love, cross, bot, line, text, allcopy)
        self.play(ApplyMethod(all.shift, (UP * 1)))
