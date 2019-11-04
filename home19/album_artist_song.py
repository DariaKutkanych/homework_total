from functools import reduce
import datetime
import time


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
        # datetime.timedelta.(seconds=sum(song.duration.seconds
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
        self.features = [] or features
        self.artist.songs.append(self)

        if self.album:
            if self.artist != self.album.artist:
                raise WrongArtistError("Artists don't match")
            self.album.songs.append(self)

    def __repr__(self):
        return self.name


    def from_seconds(self):
        return reduce(lambda x, y: int(x)*60 + int(y),
                      str(self.duration).split(":"))


if __name__ == "__main__":

    artist1 = Artist("Bob", "Ukraine")
    artist2 = Artist("Rick", "USA")

    album1 = Album("Cool", 2010, "Rock", artist1)
    album2 = Album("Light", 2017, "Pop", artist2)
    album3 = Album("Light", 2017, "Pop", artist1)

    song1 = Song("Nature", artist1, ["Steve", "Peter"], 2010, 300, album1)
    song5 = Song("FGh", artist1, ["Steve", "Peter"], 2010, 305, album1)
    # song2 = Song("Fun", artist2, ["Steve", "Peter"], 2015, 6, album1) #confct
    song3 = Song("Dance", artist2, ["Steve", "Peter"], 2019, 300, album2)
    song6 = Song("Cool", artist1, ["Steve", "Peter"], 2019, 5, album3)
    song4 = Song("Single", artist1, ["Steve", "Peter"], 2010, 3)

    print(song1.from_seconds)
    print(song3)
    print(song4)
    print(album1.songs_number)
    print(album1.duration)
    print(song3.duration.seconds)
    print(artist1.albums, artist1.songs)
    print(song3.from_seconds())
