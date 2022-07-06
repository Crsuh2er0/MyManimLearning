from big_ol_pile_of_manim_imports import *


class 换个皮肤走下位(Scene):

    def construct(self):

        square = Square(side_length=5, fill_color=BLUE,fill_opacity=0.5)
        label = TextMobject("扭一下身体")
        label.bg = BackgroundRectangle(label,fill_opacity = 1)
        label_group = VGroup(label.bg,label)
        label_group.rotate(TAU/8)
        label2 = TextMobject("加个边框",color=BLACK)
        label2.bg = SurroundingRectangle(label2,color=BLUE,fill_color=RED,fill_opacity=.5)
        label2_group = VGroup(label2.bg,label2)
        label2_group.next_to(label_group,DOWN)
        label3 = TextMobject("变成彩虹")
        label3.scale(1.8)
        label3.set_color_by_gradient(RED,ORANGE,YELLOW,GREEN,BLUE,PURPLE)
        label3.to_edge(DOWN)

        self.add(square)
        self.play(FadeIn(label_group))
        self.play(FadeIn(label2_group))
        self.play(FadeIn(label3))
        self.wait()