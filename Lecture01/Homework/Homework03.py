# Define a class Triangle to represent a general triangle
class Triangle(object):
    def __init__(self, angle1, angle2, angle3):
        # Initialize the triangle with three angles
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    # Class attribute: all triangles have 3 sides
    number_of_sides = 3

    def check_angles(self):
        # Calculate the sum of all three angles
        sum_all_angles = self.angle1 + self.angle2 + self.angle3
        # Return True if the sum is 180 (valid triangle), else False
        if sum_all_angles == 180:
            return True
        else:
            return False


# Define a subclass Equilateral that inherits from Triangle
class Equilateral(Triangle):
    # All angles in an equilateral triangle are 60 degrees
    angle = 60

    def __init__(self):
        # Initialize an equilateral triangle with all three angles = 60
        self.angle1 = self.angle
        self.angle2 = self.angle
        self.angle3 = self.angle


#######################################
# Create an instance of Triangle with angles 90, 30, 60
my_triangle = Triangle(90, 30, 60)
# Print the number of sides (should be 3)
print(my_triangle.number_of_sides)
# Check if the angles sum to 180 (should be True)
print(my_triangle.check_angles())

# Create an instance of Equilateral (all angles = 60)
my_equilateral = Equilateral()
# Print the angle attribute (should be 60)
print(my_equilateral.angle)
# Print angle1, which was set to 60 in __init__
print(my_equilateral.angle1)
