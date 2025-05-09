from manimlib import *

class TestTexText(Scene):
    def construct(self):
        import os
        os.environ["MANIM_DEBUG"] = "true"

        m = TexText("M").scale(3).set_color(BLACK)
        m.move_to(ORIGIN)
        self.add(m)
