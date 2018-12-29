import webbrowser 


class Movie:

    """
    This class provides a way to store movie related information
    """

    # Constant with all valid ratings
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, title, storyline,
                 poster_image_url, trailer_youtube_url):
        """
        Constructor method that create an instance of this class

        :param title: string
        :param storyline: string
        :param poster_image_url: string
        :param trailer_youtube_url: string
        """
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        """"
        Shows the movie trailer in a browser window
        """
        webbrowser.open(self.trailer_youtube_url)
