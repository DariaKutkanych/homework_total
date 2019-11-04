import unittest
from album_artist_song import Artist, Album, Song, WrongArtistError


class TestArtist(unittest.TestCase):

    def setUp(self):
        self.a1 = Artist("Bob", "Ukraine")
        self.a2 = Artist("Rick", "USA")

        self.al1 = Album("Cool", 2010, "Rock", self.a1)
        self.al2 = Album("Light", 2017, "Pop", self.a2)
        self.al3 = Album("Light", 2017, "Pop", self.a1)

        self.s1 = Song("Nature", self.a1, ["Steve", "Pit"], 2010, 3, self.al1)
        self.s5 = Song("FGh", self.a1, ["Steve", "Peter"], 2010, 3, self.al1)

    def test_songs_number_increase(self):
        self.assertEqual(self.a1.songs_number, 2)

    def test_albums_number_increase(self):
        self.assertEqual(self.a2.albums_number, 1)

    def test_repr_works_properly(self):
        self.assertEqual(repr(self.a2), "Rick")
