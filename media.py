import fresh_tomatoes

class Movie():
    """Define the Movie class template

    Attributes:
        movie_title(str) - title of the movie
        poster_image_url(str) - URL containing the image of the poster for the movie
        trailer_youtube_url(str) - URL of the trailer for the movie on youtube
    
    """
    def __init__(self, movie_title, poster_image_url, trailer_youtube_url):
        self.title = movie_title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        
