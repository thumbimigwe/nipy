#!/usr/bin/python3

# Challenge
# Your first challenge consists of writing a Python script that will read the following text file, one line at a time and display the content of each line on screen.

file = `open("MyPlaylist.txt","r")

#Repeat for each song in the text file
for line in file:

# Let's split the line into an array called "fields" using the ";" as a separator:
     fields = line.split(";")

songTitle=fields[0]
artist = fields[1]
duration = [2]

# print the song title
print(songTitle+" by "+artist+"   Duration: "+duration)
file.close
