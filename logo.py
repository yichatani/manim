from manimlib import *

class MYLogo(Scene):
    def construct(self):
        bg = FullScreenRectangle()
        bg.set_fill(WHITE, opacity=1)
        bg.set_z_index(-10)
        # bg.scale(0.7)
        self.add(bg)

        arm_length = 0.7 * 2
        stroke = 30 * 2
        angles = [30, 150, 270]
        colors = [
            Color(rgb=(1, 0, 0)),  # R
            Color(rgb=(0, 1, 0)),  # G
            Color(rgb=(0, 0, 1)),  # B
        ]

        arms = VGroup()
        for angle, color in zip(angles, colors):
            theta = angle * DEGREES
            direction = np.array([np.cos(theta), np.sin(theta), 0])
            arm = Line(np.array([0.19 * direction[0] * 2, 0.19 * direction[1] * 2, 0.]), arm_length * direction, color=color, stroke_width=stroke)
            arms.add(arm)
        # center_dot = Dot(arms.get_center(), color=BLACK, radius=0.05)
        # self.add(center_dot)
        self.add(arms)
        arms.move_to(np.array([0., 0.18 * 2, 0.]))
       
        m = TexText(r"\texttt{M}").scale(8).set_color(BLACK)
        c = TexText(r"\texttt{C}").scale(8).set_color(BLACK)

        m.move_to(1.6*LEFT*2)
        self.add(m)

        # c = TexText("C").scale(4).set_color(BLACK)
        c.move_to(1.6*RIGHT*2)
        self.add(c)


        for _ in range(3):
            self.play(Rotate(arms, angle=120 * DEGREES, about_point=ORIGIN+np.array([0., 0.07*2, 0.])), run_time=2)
            self.wait(0.2)

        self.wait(1)

