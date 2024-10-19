from manim import *

class ReLUVisualization(Scene):
    def construct(self):
        # Create the axes
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-1, 5, 1],
            axis_config={"color": BLUE},
            x_axis_config={"numbers_to_include": range(-4, 5)},
            y_axis_config={"numbers_to_include": range(0, 5)},
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label="f(x)")

        # Create the ReLU function
        relu_function = axes.plot(lambda x: max(0, x), color=RED)

        # Create the label for the function
        relu_label = MathTex("f(x) = max(0, x)").next_to(relu_function, UP, buff=0.5)

        # Create a dot to move along the function
        dot = Dot(color=YELLOW)
        dot.move_to(axes.c2p(0, 0))

        # Add everything to the scene
        self.play(Create(axes), Write(axes_labels))
        self.play(Create(relu_function), Write(relu_label))
        self.play(FadeIn(dot))

        # Animate the dot moving along the function
        self.play(MoveAlongPath(dot, relu_function, rate_func=there_and_back), run_time=6)

        # Highlight the non-linear part (corrected)
        highlight = axes.plot(lambda x: 0, x_range=[-5, 0], color=YELLOW)
        self.play(Create(highlight))

        # Add text explanation
        explanation = Text("ReLU is linear for x > 0 and zero for x <= 0", font_size=24).to_edge(DOWN)
        self.play(Write(explanation))

        self.wait(1)

scene = ReLUVisualization()
scene.render()