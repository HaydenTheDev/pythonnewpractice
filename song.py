class Song:
    """Class to present a song
    
    Attributes
        title (str): The title of the song
        artist (Artist): ana artist object representing the songs creator.
        duration (int): The duration of the song in seconds. May be zero
    """

    def __init__(self, title, artist):

        self.title = title
        self.artist = artist


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
            add_album: Use to add a new album to the artist's albums list
    """

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


def load_data():
    new_artist = None
    new_album = None
    artist_list = []

    with open("albums.txt", 'r') as albums:
        for line in albums:
            artist_field, album_field, year_field, song_field = tuple(line.strip("\n").split("\t"))
            year_field = int(year_field)
            print("{}:{}:{}:{}".format(artist_field, album_field, year_field, song_field))

            if new_artist is None:
                new_artist = Artist(artist_field)
            elif new_artist.name != artist_field:
                new_artist.add_album(new_album)
                artist_list.append(new_artist)
                new_artist = Artist(artist_field)
                new_album = None

            if new_album is None:
                new_album = Album(album_field, year_field, new_artist)
            elif new_album.name != album_field:
                # We've just read a new album for the current artist.
                # Store current album in artist's collection then create a new album
                new_artist.add_album(new_album)
                new_album = Album(album_field, year_field, new_artist)

            # create a new song object and add it to the current album's collection.
            new_song = Song(song_field, new_artist)
            new_album.add_song(new_song)

        # After read the last line of the text file, we will have an artist and album
        if new_artist is not None:
            if new_album is not None:
                new_artist.add_album(new_album)
            artist_list.append(new_artist)
    return artist_list


def create_checkfile(artist_list):
    """Create a check file from the object data for comparison with the original file"""
    with open("checkfile.txt", 'w') as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print("{0.name}\t{1.year}\t{2.title}".format(new_artist, new_album, new_song),
                          file=checkfile)


if __name__ == '__main__':
    artists = load_data()
    print("There are {} artists".format(len(artists)))

    create_checkfile(artists)