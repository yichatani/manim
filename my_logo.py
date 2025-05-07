# from manimlib import *

# class BenzYLogo(Scene):
#     def construct(self):
#         bg = FullScreenRectangle()
#         bg.set_fill(WHITE, opacity=1)
#         bg.set_z_index(-10)
#         self.add(bg)

#         arm_length = 1
#         stroke = 8
#         angles = [30, 150, 270]

#         # ✅ 使用 CV 常见的纯红绿蓝颜色（RGB 1/0/0）
#         colors = [
#             Color(rgb=(1, 0, 0)),  # 红
#             Color(rgb=(0, 1, 0)),  # 绿
#             Color(rgb=(0, 0, 1)),  # 蓝
#             # Color(rgb=(0, 0, 0))
#         ]

#         arms = VGroup()
#         for angle, color in zip(angles, colors):
#             theta = angle * DEGREES
#             direction = np.array([np.cos(theta), np.sin(theta), 0])
#             arm = Line(ORIGIN, arm_length * direction, color=color, stroke_width=stroke)
#             arms.add(arm)

#         arms.move_to(ORIGIN)

#         letter_m = Text("M", font_size=144, color=BLACK).move_to(LEFT * 4)
#         letter_c = Text("C", font_size=144, color=BLACK).move_to(RIGHT * 4)

#         # 添加元素
#         self.add(letter_m, letter_c, arms)

#         # 绕中心旋转 Y 臂（无位移）
#         for _ in range(3):
#             self.play(Rotate(arms, angle=120 * DEGREES, about_point=ORIGIN), run_time=2)
#             self.wait(0.5)

#         self.wait(1)

from manimlib import *

class BenzYLogo(Scene):
    def construct(self):
        # 白色背景
        bg = FullScreenRectangle()
        bg.set_fill(WHITE, opacity=1)
        # bg.set_z_index(-10)
        self.add(bg)

        # 参数设置
        arm_length = 1.5
        stroke = 10
        angles = [30, 150, 270]  # 使用你的角度设置
        colors = [
            Color(rgb=(1, 0, 0)),  # 红
            Color(rgb=(0, 1, 0)),  # 绿
            Color(rgb=(0, 0, 1)),  # 蓝
        ]

        # 构建三条臂，从 ORIGIN 指向每个角度对应点
        arms = VGroup()
        for angle, color in zip(angles, colors):
            theta = angle * DEGREES
            direction = np.array([np.cos(theta), np.sin(theta), 0])
            arm = Line(ORIGIN, arm_length * direction, color=color, stroke_width=stroke)
            arms.add(arm)

        # 中心放置 Y（已从 ORIGIN 出发）
        arms.move_to(ORIGIN)

        # 创建黑色的大写 M / C，使用 next_to 放置
        letter_m = Text("M", font_size=144, color=BLACK)
        letter_c = Text("C", font_size=144, color=BLACK)
        # letter_m.next_to(arms, LEFT, buff=1.5)
        # letter_c.next_to(arms, RIGHT, buff=1.5)


        VGroup(letter_m).arrange(LEFT, buff=1.5)
        VGroup(letter_c).arrange(RIGHT, buff=1.5)


        # 添加元素
        self.add(letter_m, letter_c, arms)

        # ✅ 精确绕原点旋转，不偏心
        for _ in range(100):
            self.play(Rotate(arms, angle=120 * DEGREES, about_point=ORIGIN), run_time=2)
            self.wait(0.5)

        self.wait(1)

