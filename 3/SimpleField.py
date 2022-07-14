import numpy as np

from big_ol_pile_of_manim_imports import *


class SimpleField(Scene):

    def construct(self):
        plane = NumberPlane(color=RED)
        plane.add(plane.get_axis_labels())
        self.add(plane)

        points = [x * RIGHT + y * UP
                  for x in np.arange(-5, 5, 1)
                  for y in np.arange(-3, 3, 1)]

        vec_field = []
        for point in points:
            field = 0.5 * RIGHT + 0.5 * UP
            result = Vector(field).shift(point)
            vec_field.append(result)

        draw_field = VGroup(*vec_field)
        self.play(ShowCreation(draw_field), run_time=4)
        self.wait(2)
