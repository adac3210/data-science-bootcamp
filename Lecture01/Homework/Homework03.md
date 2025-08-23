### Problem Statement

1. Write a class called **`Triangle`**:

   * It should take three parameters for the angles.
   * It should have a function **`check_angles`** that returns `True` if the sum of the three angles is 180, otherwise `False`.
   * Each triangle should also have a property **`number_of_sides`**, set to 3.

2. Write a class called **`Equilateral`** that **inherits** from `Triangle`:

   * An equilateral triangle has all three angles equal to 60.
   * Create an initializer that sets these angles automatically.

3. Create objects of each class and test their attributes and methods.

---

### Solution Skeleton

```python
class Triangle(object):
    number_of_sides = 3   # class attribute

    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    def check_angles(self):
        """Return True if the sum of the angles is 180, else False."""
        return self.angle1 + self.angle2 + self.angle3 == 180


class Equilateral(Triangle):
    def __init__(self):
        # All angles in an equilateral triangle are 60
        super().__init__(60, 60, 60)
        self.angle = 60    # extra attribute for convenience


#######################################
# Testing the classes
my_triangle = Triangle(90, 30, 60)
print(my_triangle.number_of_sides)   # 3
print(my_triangle.check_angles())    # True

my_equilateral = Equilateral()
print(my_equilateral.angle)          # 60
print(my_equilateral.angle1)         # 60
```

---

✅ **Key Points:**

* `number_of_sides` is set as a **class attribute** since all triangles have 3 sides.
* `check_angles` verifies the triangle’s validity.
* `Equilateral` uses `super()` to call the parent constructor with all angles set to 60.

