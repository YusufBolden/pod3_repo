# Music playlist challenge!
# In this challenge, you'll have to both work on this script, and the accompanying script playlist_functions.py
# All of your functions should be in the other script (playlist_functions.py)
# But, you'll run your functions here

# 1 Import all the functions in playlist_functions.py
import playlist_functions as pf
import numpy as np

# This code initializes your playlist as an empty list. no songs in it yet!
my_playlist = []


# 2 Check what is in your playlist using the display_playlist() function
# HINT: the display_playlist() function in playlist_functions.py to figure out how to use it
print('Question 2')
pf.display_playlist(my_playlist)
# 3 Add a song to my_playlist using the add_song() function
# The song that you add should be a dictionary, with the following key-value pairs
# 'artist' (string)
# 'title' (string)
random_song = {'artist':'ASAP Rocky', 'title': 'Canal St'}
pf.add_song(my_playlist, random_song)
'''
example_song = {'artist': 'Lauryn Hill', 'title': 'Everything Is Everything'}
'''


# 4 Check that you've added the song by running the display_playlist() function again
print('Question 4')
pf.display_playlist(my_playlist)
# 5 Add 2 more songs to my_playlist, then display it again using the display_playlist() function
print('Question 5')
random_song1 = {'artist': 'Meek Mills', 'title': 'Monster'}
random_song2 = {'artist': 'Lil Baby', 'title': 'Global'}
pf.add_song(my_playlist, random_song1)
pf.add_song(my_playlist, random_song2)
pf.display_playlist(my_playlist)

# 6 In playlist_functions.py, define a function called get_playlist_length()
# See playlist_functions.py for details on how to define this function
# THEN, call that function in this script to get the length of my_playlist
print('Question 6')
pf.get_playlist_length(my_playlist)
print(pf.get_playlist_length(my_playlist))


# 7 At the top of this script, import numpy using the usual alias

# 8: Using numpy, calculate the average monthly plays for a song
# TODO: using the mean() function from numpy, calculate the average of monthly_plays
# You don't have to write any functions for this question
print('Question 8')
monthly_plays = [127030, 274920, 232453, 98278, 500301, 235462]
print(np.mean(monthly_plays))


# BONUS In playlist_functions.py, define a new function called play_track()
# See playlist_functions.py for details on how to define this function
# Then play a few tracks, and run display_playlist() again to make sure it works
print('BONUS')

pf.play_track(my_playlist, 2)
pf.play_track(my_playlist, 0)
pf.play_track(my_playlist, 1)
pf.play_track(my_playlist, 1)

pf.display_playlist(my_playlist)