'''
Function to list all artists
- takes 1 argument, playlist (list)
- returns a list of artist names in the playlist
'''
def get_playlist_titles(playlist):
	titles = []
	for song in playlist:
		titles.append(song["title"])
	return titles

'''
Function to search songs by artist
-takes 2 arguments, playlist (list) and artist_name (a string)
-returns a list of songs in the playlist by that artist
-if there are no songs found by that artist, the list will be empty
'''
def search_by_artist(playlist, artist_name): 
	songs_found = []
	for song in playlist:
		if artist_name == song['artist']:
			songs_found.append(song['title'])
	return songs_found

'''
Function to search songs by title
-takes 2 arguments, playlist (list) and song_title (string)
-returns a list including all the songs with the title searched
-if there are no songs with this title, the list will be empty
'''
def search_by_title(playlist, song_title):
	songs_found = []
	for song in playlist:
		if song_title == song['title']:
			songs_found.append(song)
	return songs_found 
