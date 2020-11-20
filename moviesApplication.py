"""
- Enter 'a' to add a movie, 'l' to see your movie , 'f' to find a movie and 'q' to quit

-Add movies
-See movies
-Find a movie
- Stop running the program

Tasks:
[] Decide where to store movies
[] What is the format
[] Show the user the main interface and get their input
[] Allow users to add movies
[] Show all their movies
[] Find a movie
[] Delete a movie 
[] Stop running the program when they type 'q'
"""

movies = []
def menu():
    user_input = input("Enter 'a' to add a movie, 'l' to see your movie , 'f' to find a movie, 'd' to delete a movie and 'q' to quit: ")

    while user_input != 'q':
        if user_input == 'a':
            add_movie()
        elif user_input == 'l':
            show_movie(movies)
        elif user_input == 'd':
            delete_movie(movies)
        elif user_input == 'f':
            find_movie()
        else:
            print("Invalid input")
        user_input = input("Enter 'a' to add a movie, 'l' to see your movie , 'f' to find a movie, 'd' to delete a movie and 'q' to quit: ")

        print(movies)

def add_movie():
    name = input("Enter the name of the movie you want to add")
    director = input("Enter the director's name")
    year = input("Enter the year it was released")

    movies.append ({
        'name':name,
        'director': director,
        'year': year
        })

   

def show_movie(movies_list):
    for movie in movies_list:
        try:
            if movies == "[{}]":
                      print("No movie")
            elif movies == None:
                print("")

            else:
              print(f"Movie : {movie['name']}")
              print(f"Director : {movie['director']}")
              print(f"Release Date : {movie['year']}")
        except:
            print("Error, No Movies")
          

        
        

def delete_movie(movies_list):
    for movie in movies_list:
          movie.clear()
          


def find_movie():
    find_by = input("What property of are you looking for (Year, Director, movie name)")
    looking_for = input("What are you searching for")
    
    found_movies = find_by_attribute(movies, looking_for, lambda x: x[find_by])

    show_movie(found_movies)
    
def find_by_attribute(items, expected, finder):
    found = []

    for i in items:
        if finder(i) == expected:
            found.append(i)

    return found


    
    


menu()
