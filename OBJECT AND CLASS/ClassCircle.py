 #Create a class Circle

class Circle(object):
    
    # Constructor
    def __init__(self, radius=3, color='blue'):
        self.radius = radius
        self.color = color 
    
    # Method
    def add_radius(self, r):
        self.radius = self.radius + r
        return(self.radius)
    
    # Method
    def drawCircle(self):
        fig, ax = plt.subplots()
        ax.add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        ax.set_aspect('equal', adjustable='box')
        # Make limits visible and consistent around the circle
        pad = max(1, 0.1 * self.radius)
        ax.set_xlim(-(self.radius + pad), (self.radius + pad))
        ax.set_ylim(-(self.radius + pad), (self.radius + pad))
        plt.show()
        