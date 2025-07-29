from tkinter import Tk, BOTH, Canvas

# Create a new Window class, its constructor should:
# Take a width and height as parameters. This will be the size of the new window we create in pixels.
# It should create a new root widget using Tk() and save it as a data member
# Set the title property of the root widget
# Create a Canvas widget and save it as a data member.
# Pack the canvas widget so that it's ready to be drawn
# Create a data member to represent that the window is "running", and set it to False

# Add a redraw() method to the Window class. It should redraw all the graphics in the window (the assumption is their positions and colors and such may have changed).
# Note: Tkinter is not a reactive framework like React or Vue - we need to tell the window when it should render to visuals.
# Use the root widget's update_idletasks() and update() methods to accomplish this.

# Add a wait_for_close() method to the Window class. This method should:
# Set the running state to True
# Call self.redraw() over and over as long as the running state remains True

# Add a close() method to the Window class. This method should:
# Set the running state to False
# Call the root widget's protocol method to connect your close method to the "delete window" action. This will stop your program from running when you close the graphical window.

class Window():
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, width=width, height=height)
        self.__canvas.pack()
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self):
        self.__running = False

def main():
    win = Window(800, 600)
    win.wait_for_close()

if __name__ == "__main__":
    main()