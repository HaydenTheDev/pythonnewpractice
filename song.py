class Song:
    """Class to present a song
    
    Attributes
        title (str): The title of the song
        artist (Artist): ana artist object representing the songs creator.
        duration (int): The duration of the song in seconds. May be zero
    """

    def __init__(self, title, artist, duration):

        self.title = title
        self.artist = artist
        self.duration = duration

class Album:
    """ Class to represent an Album, using it's track list

    Attributes:
        album_name (str): The name of the album.
        year (int): The year the album was released.
        artist (Artist): The artist responsible for the album
        if not specified, the artist will default to the artist with the name
        "various Artists".
        tracks (List(Song)): A list of the songs on the album.

    Methods:
        addSong: Used to add a new song to the album's track list.
        """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = artist("Various Artists")
        else:
            self.artist = artist

        self.tracks = []

    def add_song(self, song, positions=None):
        """Adds a song to the track list

        args:
            song(Song): a song to add
            position (Optional(int)): If specified, the song will be added to that position
            in the track list - inserting it between other songs if necessary.
            Otherwise , the song will be added to the end of the list.
            """
        if positions is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(positions, song)