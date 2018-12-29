import movie
import my_fresh_tomatoes

# Creates a new movie object
toy_story = movie.Movie(
    "Toy Story",
    "A story of a boy and his toys that come to life",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://youtu.be/KYz2wyBy3kc"
    )

emperor = movie.Movie(
    "The Emperor",
    "A story about a emperor and his new jorney",
    "https://upload.wikimedia.org/wikipedia/pt/6/69/Grooveposter.jpg",
    "https://youtu.be/Hjvy8vc39kw"
    )

capitain_america = movie.Movie(
    "Captain America",
    "The Captain America's story",
    "https://upload.wikimedia.org/wikipedia/en/3/37/Captain_America_The_First_Avenger_poster.jpg",
    "https://youtu.be/JerVrbLldXw"
    )

mowgli = movie.Movie(
    "Mowgli",
    "A story about a boy that grows in the jungle",
    "https://upload.wikimedia.org/wikipedia/pt/0/07/Mowgli.jpg",
    "https://youtu.be/FB1KTG-O1V0"
)

krampus = movie.Movie(
    "Krampus",
    "A family has no longer its christmas spirit and soon is terrified by a demon that punish"
    + "those who don't give value to the celebration",
    "https://upload.wikimedia.org/wikipedia/en/1/1e/Krampus_poster.jpg",
    "https://youtu.be/h6cVyoMH4QE"
)

spider_man = movie.Movie(
    "Spider-Man",
    "The story about a boy that was bitten by a spider and then receives great power",
    "https://upload.wikimedia.org/wikipedia/en/f/f3/Spider-Man2002Poster.jpg",
    "https://youtu.be/O7zvehDxttM"
)


# The list that contains all movie objects
movies = [toy_story, emperor, capitain_america, mowgli, krampus, spider_man]

# Opens the movie page in a new browser window
my_fresh_tomatoes.open_movies_page(movies)
