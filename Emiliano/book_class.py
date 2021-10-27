


from Emiliano.library_challenge import count_books


class Booklist():
	def __init__(self):
		self.books=[]
		pass

	def add(self, title, author):
		book={'title': title, 'author': author}		
		self.books.append(book)
		pass

	def count_books(self):
		return len(self.books)
		

	def remove_title(self, title):
		pass

	def display_titles(self):
		pass

