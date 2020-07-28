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

print(Song.__doc__)
print(Song.__init__.__doc__)
Song.__init__.__doc__ = """Song init method

      args:
          title (str): Initalises the 'title' attribute
          artist (Artist): At artist object representing the song's creator
          duration (Optional(int): Initial value for the 'duration' attribute
              Will default to zero if not specified
      """
help(Song)