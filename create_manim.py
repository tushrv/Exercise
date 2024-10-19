from manim import *

class ElricInCircle(Scene):
    def construct(self):
        # Create the circle
        circle = Circle(radius=2, color=WHITE)
        
        # Create the text
        text = Text("elric", font_size=100)
        
        # Animate the circle creation
        self.play(Create(circle))
        
        # Animate each letter appearing one by one
        for i in range(len("elric")):
            self.play(Write(text[i]))
        
        # Center the text inside the circle
        text.move_to(circle.get_center())
        
        # Wait for a moment at the end
        self.wait(2)

if __name__ == "__main__":
    scene = ElricInCircle()
    scene.render()
