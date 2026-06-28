# Tech Vision Program

class Vision:

    def __init__(self):
        self.creator = "Developer"
        self.field = "Technology"
        self.goal = "Build solutions that help people"
        self.inspiration = "Innovation and curiosity"

    def display(self):
        print("Role:", self.creator)
        print(" Field:", self.field)
        print(" Goal:", self.goal)
        print(" Inspiration:", self.inspiration)

    def message(self):
        print("\nTechnology is not just about coding.")
        print("It is about creating ideas that make life better for everyone.")


v = Vision()

v.display()
v.message()