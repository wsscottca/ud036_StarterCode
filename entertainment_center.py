import fresh_tomatoes
import media

# Create database of movie instances
fight_club = media.Movie("Fight Club",
                         "https://movieswithaplottwist.com/wp-content/uploads/2016/03/fight-club.25541.jpg",
                         "https://www.youtube.com/watch?v=_XgQA9Ab0Gw")
finding_nemo = media.Movie("Finding Nemo",
                           "http://www.impawards.com/2003/posters/finding_nemo.jpg",
                           "https://www.youtube.com/watch?v=wZdpNglLbt8")
american_psycho = media.Movie("American Psycho",
                              "https://www.movieposter.com/posters/archive/main/229/MPW-114774",
                              "https://www.youtube.com/watch?v=5YnGhW4UEhc")
nightmare_before_christmas = media.Movie("Nightmare Before Christmas",
                                         "http://www.impawards.com/1993/posters/nightmare_before_christmas_ver1.jpg",
                                         "https://www.youtube.com/watch?v=8qrB9I3DM80")
guardians_of_the_galaxy = media.Movie("Guardians of the Galaxy",
                                      "http://t2.gstatic.com/images?q=tbn:ANd9GcQW3LbpT94mtUG1PZIIzJNxmFX399wr_NcvoppJ82k7z99Hx6in",
                                      "https://www.youtube.com/watch?v=d96cjJhvlMA")
coraline = media.Movie("Coraline",
                       "http://www.gstatic.com/tv/thumb/movieposters/177367/p177367_p_v8_ae.jpg",
                       "https://www.youtube.com/watch?v=LO3n67BQvh0")

# Create list of movie objects to pass to open_movies_page
movies = {fight_club, finding_nemo, american_psycho, nightmare_before_christmas, guardians_of_the_galaxy, coraline}
fresh_tomatoes.open_movies_page(movies)
