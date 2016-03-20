import movie
import fresh_tomatoes

ddlj = movie.Movie("Dilwale Dulhania Le Jayenge",
                   "Love Story",
                   "http://images.desimartini.com/media/uploads/dilwaledulhanialejayeng.jpg",
                   "https://www.youtube.com/watch?v=EIKZ7amRGwk")


captain_america = movie.Movie("Captain America: Civil War",
                              "Captain America: Civil War is an upcoming American superhero film featuring the Marvel Comics character Captain America",
                              "https://upload.wikimedia.org/wikipedia/en/5/53/Captain_America_Civil_War_poster.jpg",
                              "https://www.youtube.com/watch?v=QGfhS1hfTWw")


x_men = movie.Movie("X-Men: Apocalypse More words added",
                    "X-Men: Apocalypse is an upcoming 2016 American superhero film based on the X-Men characters that appear in Marvel Comics",                    
                    "https://upload.wikimedia.org/wikipedia/en/0/04/X-Men_-_Apocalypse.jpg",
                    "https://www.youtube.com/watch?v=N0io2w_6vT8")

walk_to_remember = movie.Movie("A Walk to Remember",
                   "Landon Carter gets in trouble and has to do community service- including getting involved in the spring play. ",
                   "https://upload.wikimedia.org/wikipedia/en/d/dc/A_Walk_to_Remember_Poster.jpg",
                   "https://www.youtube.com/watch?v=i72wRvPw_ik")


Forrest_Gump = movie.Movie("Forrest Gump",
                           "Forrest Gump is a 1994 American epic romantic-comedy-drama film based on the 1986 novel of the same name by Winston Groom.",
                           "https://upload.wikimedia.org/wikipedia/en/thumb/6/67/Forrest_Gump_poster.jpg/220px-Forrest_Gump_poster.jpg",
                           "https://www.youtube.com/watch?v=eYSnxZKTZzU")


The_Breakfast_Club = movie.Movie("The Breakfast Club",
                    "The Breakfast Club is a 1985 American coming of age comedy-drama film written, produced, and directed by John Hughes",                    
                    "https://upload.wikimedia.org/wikipedia/en/thumb/5/50/The_Breakfast_Club.jpg/220px-The_Breakfast_Club.jpg",
                    "https://www.youtube.com/watch?v=BSXBvor47Zs")

passlist = [ddlj,captain_america,x_men,walk_to_remember,Forrest_Gump,The_Breakfast_Club]

fresh_tomatoes.open_movies_page(passlist)
