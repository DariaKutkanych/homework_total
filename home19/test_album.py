import unittest
from album_artist_song import Artist, Album, Song, WrongArtistError


class TestAlbum(unittest.TestCase):

    def setUp(self):
        self.a1 = Artist("Bob", "Ukraine")
        self.a2 = Artist("Rick", "USA")

        self.al1 = Album("Cool", 2010, "Rock", self.a1)
        self.al2 = Album("Light", 2017, "Pop", self.a2)
        self.al3 = Album("Light", 2017, "Pop", self.a1)

        self.s1 = Song("Nature", self.a1, ["Steve", "Peter"], 2010, 3, self.al1)
        self.s5 = Song("FGh", self.a1, ["Steve", "Peter"], 2010, 3, self.al1)

    def test_songs_number_append(self):
        self.assertEqual(self.al1.songs_number, 2)
        self.assertEqual(self.al2.songs_number, 0)

    def test_songs_are_classes(self):
        self.assertIsInstance(self.al1.songs[0], Song)

    def test_duration_calculation_correctness(self):
        self.assertEqual(self.al1.duration.seconds, 6)

    def test_repr_work_properly(self):
        self.assertEqual(repr(self.al1), "Cool")

    def test_if_year_is_integer(self):
        for album in self.a1.albums:
            self.assertIsInstance(album.year, int)

