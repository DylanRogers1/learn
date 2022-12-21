class Dog:
  def __init__(self, dog_name):
    self.name = dog_name
    print("A dog called", self.name, "comes running out of the bushes.")
  def bark(self):
    print(self.name, ": WOOF!")

smudge = Dog("Smudge")
smudge.bark()
smudge.name = "Bobby"
smudge.bark()