import requests
import json
import os
import mutagen
from mutagen.easyid3 import EasyID3
import pylast

API_KEY = '76e2d6fda82f6c2377d2bc5728e8aa8d'
API_SECRET = '540fd48e6f06d8306016d6d592b160a8'

network = pylast.LastFMNetwork(api_key = API_KEY, api_secret = API_SECRET)
directory = "/home/edwin-dev/dev/musicly/test-files"
songlist = os.listdir(directory)
path = str



#Testing ID3
# for song in songlist:
#     if song.endswith("mp3"):
#         path = os.path.join(directory,song)
#         keys = EasyID3(path)
        # print(keys["artist"])


class Tagger:
    #Grabs ID3 Tags from audio file
    def getid3(self, filename):
        return EasyID3(filename)

    #Grabs location of audio file
    def music_directory(self, directory):
        songlist = []
        for song in os.listdir(directory):
            path = os.path.join(directory,song)
            songlist.append(self.getid3(path))
            return songlist

    def find_tags(self, tag):
        for id in self.music_directory(directory):
            musictag = id[tag]
            return musictag


tag = Tagger()

print(tag.find_tags("artist"))