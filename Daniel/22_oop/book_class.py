# make a Class Booklist

class Booklist():
	def __init__(self):
		# initialize the books attribute
		self.books = []

# make a method to add a book, title, author

	def add(self, title, author):
		book = {}
		book['title'] = title
		book['author'] = author

# append book to books attribute

		self.books.append(book)

# make a method to count the books by using length on books attribute

	def count_books(self):
		return (len(self.books))

# make a method to remove a book using the title, and using a loop remove
# a book by using the title of the book

	def remove_title(self, title):
		for book in self.books:
			if book['title'] == title:
				self.books.remove(book)

# make a method to display all titles in alphabetical order, make a blank list,
# loop through books and add titles to list,

	def display_titles(self):
		titles = []
		for book in self.books:
			titles.append(book['title'])

# sort alphabetically
		titles.sort()

# print sorted titles

		print(titles)

