# Implement a simple Audio Streaming Service class architecture
# It'll include 3 classes - Song, Album and Artist
#
# Artist class:
#   - name: str
#   - country: str
#   - songs: list = []
#   - albums: list = []
#   - songs_number: int - must be declared using property decorator as the
#   length of songs list
#   - albums_number: int - must be declared using property decorator as the
#   length of albums list
#
# Album class:
#   - name: str
#   - year: int
#   - genre: str
#   - artist: Artist
#   - songs: list = []
#   - songs_number: int - must be declared using property decorator as the
#   length of songs list
#   - duration: float - must be declared using property decorator. Album
#   duration is the sum of all songs' (from songs list) duration.
#
# Song class:
#   - name: str
#   - artist: Artist
#   - features: list[Author] = [] (can feature 1 or more Artists)
#   - year: int
#   - duration: float
#   - album: Album (can be None if it's a single)
#
#   when you specify an album, make sure add the song to album's [songs] list.
#   the same with Arist albums/songs lists
#
#   Also, you need implement a custom exception WrongArtistError which is
#   raised when you try to add a song to an album and artists don't match.

from functools import reduce
import datetime


class WrongArtistError(Exception):
    pass


class Artist:
    def __init__(self, name, country):
        self.name = name
        self.country = country
        self.songs = []
        self.albums = []

    def __repr__(self):
        return self.name

    @property
    def songs_number(self):
        return len(self.songs)

    @property
    def albums_number(self):
        return len(self.albums)


class Album:
    def __init__(self, name, year, genre, artist):
        self.name = name
        self.year = year
        self.genre = genre
        self.artist = artist
        self.songs = []
        self.artist.albums.append(self)
        self._duration = 0

    @property
    def songs_number(self):
        return len(self.songs)

    @property
    def duration(self):
        return reduce(lambda x, y: x.duration + y.duration, self.songs)
        #datetime.timedelta.(seconds=sum(song.duration.seconds
        # for song in self.songs

    def __repr__(self):
        return self.name


class Song:
    def __init__(self, name, artist, features, year, duration, album=None):
        self.name = name
        self.artist = artist
        self.year = year
        self.duration = datetime.timedelta(seconds=duration)
        self.album = album
        self.features = features or []
        self.artist.songs.append(self)

        if self.album:
            if self.artist != self.album.artist:
                raise WrongArtistError("Artists don't match")
            self.album.songs.append(self)

    def __repr__(self):
        return self.name


artist1 = Artist("Bob", "Ukraine")
artist2 = Artist("Rick", "USA")

album1 = Album("Cool", 2010, "Rock", artist1)
album2 = Album("Light", 2017, "Pop", artist2)
album3 = Album("Light", 2017, "Pop", artist1)

song1 = Song("Nature", artist1, ["Steve", "Peter"], 2010, 300, album1)
song5 = Song("FGh", artist1, ["Steve", "Peter"], 2010, 305, album1)
# song2 = Song("Fun", artist2, ["Steve", "Peter"], 2015, 6, album1) #conflict
song3 = Song("Dance", artist2, ["Steve", "Peter"], 2019, 5, album2)
song6 = Song("Cool", artist1, ["Steve", "Peter"], 2019, 5, album3)
song4 = Song("Single", artist1, ["Steve", "Peter"], 2010, 3)

print(song1)
print(song3)
print(song4)
print(album1.songs_number)
print(album1.duration)
print(artist1.albums, artist1.songs)
