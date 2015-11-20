import webbrowser


class Video():
     def __init__(self,title):
         self.title = title
         
class Movie(Video):
    def __init__(self,movie_title,movie_storyline,poster,urlrl):
        Video.__init__(self,movie_title)        
        self.storyline = movie_storyline
        self.poster_image_url = poster
        self.trailer_youtube_url = urlrl

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
