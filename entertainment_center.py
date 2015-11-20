import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story","A story of toys","https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg","https://www.youtube.com/watch?v=KYz2wyBy3kc")

print(toy_story.storyline)

avatar = media.Movie("Avatar","A marine on an alien Planet","https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg","https://www.youtube.com/watch?v=cRdxXPV9GNQ")

print(avatar.storyline)
#avatar.show_trailer()

movies = [toy_story,avatar]
fresh_tomatoes.open_movies_page(movies)
