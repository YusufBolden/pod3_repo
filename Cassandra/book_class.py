class Booklist():
	def __init__(self):
		self.books = []
		
	def add(self, title, author):
		book = {}
		book['title'] = title
		book['author'] = author
		self.books.append(book)
		# [].append({})

	def count_books(self):
		pass

	def remove_title(self, title):
		pass

	def display_titles(self):
		pass

