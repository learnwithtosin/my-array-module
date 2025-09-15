class Myarray:

	def __init__(self):
		self.list = []

	
	def my_append(self, item):
		self.list  += [item]
		print(self.list)
		

	def my_insert(self, index, item):
		new_list = []
		for i in range(len(self.list) + 1):
			if i == index:
				new_list += [item]

			if i < len(self.list):
				new_list += [self.list[i]]
		self.list = new_list
		print(self.list)

	def my_pop(self, index = -1):
		new_list = []
		item_to_pop = self.list[index]
		for item in self.list: 
			if item != item_to_pop:
				new_list += [item]
				self.list = new_list  
		
		print(self.list)
		print(item)

	def my_remove(self, item):
		new_list = []
		for element in self.list:
			if element != item:
				new_list += [element]
				self.list = new_list
		print(self.list)

"""
tosin = Myarray()
tosin.my_append("tosin")
tosin.my_append("male")
tosin.my_insert(1, "kazeem")
tosin.my_insert(2, "olamide")
tosin.my_insert(0, "emmanuel")
tosin.my_insert(-1, "male")

tosin.my_pop()
tosin.my_pop(1)

tosin.my_remove("emmanuel")
"""

