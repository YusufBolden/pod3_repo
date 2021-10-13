class Booklist():
	def __init__(self):
		self.books = []



	def add(self, title, author):
		book = {}
		book["title"] = title
		book["author"] = author
		self.books.append(book)
		


	def count_books(self):
		return len(self.books)

	def remove_title(self, title):
		for book in self.books:
			if book["title"] == title:
				self.books.remove(book)

	def display_titles(self, listed):
		listed = sorted(listed, key= lambda i,: i["title"])
		return(listed)
# Solution found from https://www.geeksforgeeks.org/ways-sort-list-dictionaries-values-python-using-lambda-function/ on how to organzine full dictionaries. 
		


			

