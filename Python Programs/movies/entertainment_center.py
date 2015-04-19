import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print(toy_story.storyline)

avatar = media.Movie("Avatar", "A marine on an alien planet", "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

#print(avatar.storyline)

#avatar.show_trailer()

predator = media.Movie("Predator", "The story follows an elite special forces team, on a mission to rescue hostages from guerrilla territory in Central America. Unbeknownst to the group, they are being stalked and hunted by a technologically advanced form of extraterrestrial life, the Predator.",
                       "http://upload.wikimedia.org/wikipedia/en/9/95/Predator_Movie.jpg", "https://www.youtube.com/watch?v=K9AT3tQGbIk")
#print(predator.storyline)

#predator.show_trailer()

school_of_rock = media.Movie("School of Rock", "Storyline", "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie("Ratatoullie", "Storyline", "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris", "Storyline", "https://i.ytimg.com/vi/-NoGpkSTK8k/movieposter.jpg?v=5339eafb",
                                "https://www.youtube.com/watch?v=-NoGpkSTK8k")

hunger_games = media.Movie("Hunger Games", "Storyline", "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                           "https://www.youtube.com/watch?v=PbA63a7H0bo")

movies = [toy_story, avatar, predator, school_of_rock, ratatouille, midnight_in_paris, hunger_games]

#fresh_tomatoes.open_movies_page(movies)

#print(media.Movie.VALID_RATINGS)
#print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)


