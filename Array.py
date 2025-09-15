class Myarray:

	def __init__(self, array:list):
		self.array: list = array

	
	def my_append(self, item):
		self.array  += [item]
		print(self.array)
		

	def my_insert(self, index, item):
		new_list = []
		for i in range(len(self.array) + 1):
			if i == index:
				new_list += [item]

			if i < len(self.array):
				new_list += [self.array[i]]
		self.array = new_list
		print(self.array)

	def my_pop(self, index = -1):
		new_list = []
		item_to_pop = self.array[index]
		for item in self.array: 
			if item != item_to_pop:
				new_list += [item]
				self.array = new_list  
		
		print(self.array)
		print(item)

	def my_remove(self, item):
		new_list = []
		for element in self.array:
			if element != item:
				new_list += [element]
				self.array = new_list
		print(self.array)

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

