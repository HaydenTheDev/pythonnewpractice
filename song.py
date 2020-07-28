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
        name (str): The name of the album.
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
            self.artist = Artist("Various Artists")
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


class Artist:
    """Basic class to store artist details.
    
    Attributes:
        name (str): The name of the artist.
        albums (List(Album)): A list of the albums by this artist.
            The list includes only albums in this collection, it is
            not an exhaustive list of the artist's publishes albums.

    Methods:
            add_album: Use to add a new alubm to the artist's albums list"""

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        """Add a new album to the list.

        Args:
            album (Album): Album to add to the list.
                if the album is already present, it will not be added again.
        """
        self.albums.append(album)