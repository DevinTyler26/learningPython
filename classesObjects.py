class Robot:
  def __init__(self, name, color, weight):
    self.name = name
    self.color = color
    self.weight = weight

  def introduce_self(self):
    print('My name is ' + self.name)

r1 = Robot('Devin', 'blue', 26)
# r1.name = 'Devin'
# r1.color = 'blue'
# r1.weight = 26
r1.introduce_self()

r2 = Robot('Brad', 'red', 40)
# r2.name = 'Brad'
# r2.color = 'red'
# r2.weight = 40
r2.introduce_self()


class Person:
  def __init__(self, n, p, i,):
    self.name = n
    self.personality = p
    self.is_sitting = i
  def sit_down(self):
    self.is_sitting = True
  def stand_up(self):
    self.is_sitting = False

p1 = Person('Dev', 'awesome', True)
p2 = Person('Stitch', 'cool', False)
p1.robot_owned = r2
p2.robot_owned = r1

print(p1.name, 'owns', p1.robot_owned.name, 'and he weights', p1.robot_owned.weight)