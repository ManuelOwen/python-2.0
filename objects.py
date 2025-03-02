class Robot:
    def introduce_self (self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight
        print("My name is " + self.name + " and my color is " + self.color + " and my weight is " + str(self.weight))
        
r1 = Robot()
r1.introduce_self("Tom", "red", 30)