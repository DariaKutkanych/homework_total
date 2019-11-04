import unittest
from album_artist_song import Artist, Album, Song, WrongArtistError


class TestSong(unittest.TestCase):

    def setUp(self):
        self.a1 = Artist("Bob", "Ukraine")
        self.a2 = Artist("Rick", "USA")

        self.al1 = Album("Cool", 2010, "Rock", self.a1)
        self.al2 = Album("Light", 2017, "Pop", self.a2)
        self.al3 = Album("Light", 2017, "Pop", self.a1)

        self.s1 = Song("Nature", self.a1, ["Steve", "Pit"], 2010, 3, self.al1)
        self.s5 = Song("FGh", self.a1, ["Steve", "Peter"], 2010, 300, self.al1)

    def test_if_incorrect_artist_raise_error(self):
        with self.assertRaises(WrongArtistError):
            self.s3 = Song("FGh", self.a2, ["Steve", "Peter"], 2010, 3,
                           self.al1)

    def test_if_album_is_class(self):
        self.assertIsInstance(self.s1.album, Album)

    def test_if_artist_is_class(self):
        self.assertIsInstance(self.s1.artist, Artist)

    def test_whether_single_has_no_erors(self):
        self.assertTrue(Song("FGh", self.a2, ["Steve", "Peter"], 2010, 3))

    def test_song_duration(self):
        self.assertEqual(self.s5.from_seconds(), 300)
        self.assertEqual(self.s5.duration.seconds, 300)
