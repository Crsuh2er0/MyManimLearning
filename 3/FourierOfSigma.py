from big_ol_pile_of_manim_imports import *


class FourierOfSigma(FourierCirclesScene):
    CONFIG = {"n_circles": 60,
              "center_point": ORIGIN,
              "slow_factor": 0.1,
              "run_time": 30,
              "tex": "\\Sigma",
              "start_drawn": False
              }

    def construct(self):
        path = self.get_path()
        coefs = self.get_coefficients_of_path(path)

        circles = self.get_circles(coefficients=coefs)
        for k, circle in zip(it.count(1), circles):
            circle.set_stroke(width=max(
                1 / np.sqrt(k),
                1
            ))
        drawn_path = self.get_drawn_path(circles)
        if self.start_drawn:
            drawn_path.curr_time = 1 / self.slow_factor

        self.add(path)
        self.add(circles)
        self.add(drawn_path)
        self.wait(self.run_time)

    def get_path(self):
        tex_mob = TexMobject(self.tex)
        tex_mob.set_height(6)
        path = tex_mob.family_members_with_points()[0]
        path.set_fill(opacity=0)
        path.set_stroke(WHITE, 1)
        return path
