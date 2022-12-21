import os

class ToDoList:
	def __init__(self, list_name):
		self.name = list_name
		if not os.path.exists("lists/" + list_name + ".txt"):
			f = open("lists/" + list_name + ".txt", "x")
			f.close()
		f = open("lists/" + list_name + ".txt")
		self.content = f.read().split("\n")
		f.close()
	def __del__(self):
		f = open("lists/" + self.name + ".txt", "w")
		f.write("\n".join(self.content))
		f.close()
	def add(self, item):
		self.content.append(item)
	def get(self):
		return "\n".join(self.content)

print("Welcome to To-Do List Plus! (v2)")
while True:
	list_name = input("Please enter the name of your to-do list (type 'q' to exit)... ")
	if list_name =="q":
		break
	l = ToDoList(list_name)
	while True:
		mode = input("Would you like to view the list (v), add a new item (a) or exit this to-do list (q)? ")
		if mode == "v":
			print(l.get() + "\n")
		if mode == "a":
			item = input(" >>> ")
			l.add(item)
		if mode == "q":
			del l
			break