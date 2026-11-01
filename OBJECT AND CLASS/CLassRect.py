# Create a new Rectangle class for creating a rectangle object

class Rectangle(object):
    
    # Constructor
    def __init__(self, width=2, height=3, color='r'):
        self.height = height 
        self.width = width
        self.color = color
    
    # Method
    def drawRectangle(self):
        fig, ax = plt.subplots()
        ax.add_patch(plt.Rectangle((0, 0), self.width, self.height, fc=self.color))
        ax.set_aspect('equal', adjustable='box')
        ax.set_xlim(0, self.width * 1.1)
        ax.set_ylim(0, self.height * 1.1)
        plt.show()
        