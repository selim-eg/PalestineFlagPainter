import turtle

class Flag:
    def __init__(self):
        self.turtle = turtle.Turtle()
        turtle.setup(width=1.0 , height=1.0)
        self.turtle.speed(5)
        self.screen = turtle.Screen()
        self.screen.bgcolor("#87CEFA")

    def draw_rectangle(self, color):
        self.turtle.begin_fill()
        self.turtle.fillcolor(color)
        for _ in range(2):
            self.turtle.forward(600)
            self.turtle.right(90)
            self.turtle.forward(100)
            self.turtle.right(90)

        self.turtle.end_fill()

    def draw_triangle(self, color):
        self.turtle.begin_fill()
        self.turtle.fillcolor(color)
        self.turtle.right(30)
        self.turtle.forward(300)
        self.turtle.right(120)
        self.turtle.forward(300)
        self.turtle.right(120)
        self.turtle.forward(300)
        self.turtle.right(30)
        self.turtle.end_fill()

    def draw_flag(self):
        self.turtle.up()
        self.turtle.goto(-200 , -50)
        self.turtle.down()
        self.draw_rectangle("black")
        
        self.turtle.up()
        self.turtle.goto(-200 , -150)
        self.turtle.down()
        self.draw_rectangle("white")          

        self.turtle.up()
        self.turtle.goto(-200 , -250)
        self.turtle.down()
        self.draw_rectangle("green")        

        self.turtle.up()
        self.turtle.goto(-200 , -50)
        self.turtle.down()
        self.draw_triangle("red")
        self.turtle.write("Palestine" , align="center" , font=("Arial" , 25 ,"normal")) 



flag = Flag()
flag.draw_flag()
turtle.done()