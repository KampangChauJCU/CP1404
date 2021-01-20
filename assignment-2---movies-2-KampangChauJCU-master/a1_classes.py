"""
Replace the contents of this module docstring with your own details
Name: Jinpeng Zhou
Student Number: 13710009
Date started: 04/12/2020
GitHub URL: https://github.com/JCUS-CP1404/assignment-2---movies-2-KampangChauJCU.git
"""

MENU = """Menu:
L - List movie
A - Add new movie
W - Watch a movie
Q - Quit
"""


def main():
    """Start of program"""
    print("Movies To Watch 1.0 - by Jinpeng Zhou")
    print("5 movies loaded")
    print(MENU)
    choice = input(">>> ").upper()
    all_movies = load_movies()
    while choice != "Q":  # Enter Q, print the end message
        if choice == "L":
            list_movies(all_movies)
        elif choice == "A":
            all_movies.append(add_movies())
        elif choice == "W":
            see_movies(all_movies)
        else:  # Enter other word, display the invalid menu choice
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").upper()
    save_to_file(all_movies)  # enter Q, it will overwrite the csv file
    print(len(all_movies), "movies saved to", 'movies.csv', "\nHave a nice day :)")


def load_movies():  # This function is used for open the csv file and put the data to the list
    all_movies = []  # Create a list for saving movies data
    movies_file = open('movies.csv', 'r')  # Open the csv file with 'r' read module
    for line in movies_file:
        line = line.strip("\n")
        movie_director_year_list = line.split(",")
        all_movies.append(movie_director_year_list)
    movies_file.close()
    return all_movies


def list_movies(all_movies):  # This function is used to display the movies list
    count = 0
    for i in range(len(all_movies)):  # Using the for loop with constant i
        if all_movies[i][3] == "w":
            count += 1  # If the movie is watched, count + 1
            symbol = " "
            print(" ", str(i) + ".", symbol, "", end="")
        else:
            symbol = "*"  # Use * symbol beside the watched movies list
            print(" ", str(i) + ".", symbol, "", end="")
        for j in range(len(all_movies[i]) - 2):  # Use the for loop to add the dash before the director
            if j == 1:
                dash = "-"  # If there is a director, add the dash
            else:
                dash = ""   # Else add the blank
            print(dash, "{:30}".format(all_movies[i][j]), end=" ")
        print("({:4})".format(all_movies[i][-2]))
    print(len(all_movies) - count, "movies watched,", count, "movies watched,""movies still to watched")


def see_movies(all_movies):  # This function is used to mark the watched movies
    count = 0
    for i in range(len(all_movies)):  # Using the for loop with constant i
        if all_movies[i][3] == "w":
            count += 1  # If the movie is watched, count + 1
            symbol = " "
        else:
            symbol = "*"  # Add * symbol beside the watched movies list
        print(" ", str(i) + ".", symbol, "", end="")  # Printing the format
        for j in range(len(all_movies[i]) - 2):
            if j == 1:
                dash = "-"
            else:
                dash = ""
            print(dash, "{:30}".format(all_movies[i][j]), end=" ")
        print("({:4})".format(all_movies[i][-2]))
    if count == 0:
        print("No more movies to watch! Please kindly enter Q to Quit")

    print(len(all_movies) - count, "movies watched,", count, "movies still to watched")
    movie_number = count_number("Enter the number of a movie to mark as watched\n>>> ")
    # Asking which number of movie that user want to watch
    if all_movies[movie_number][3] == "u":
        # If there is "u" in forth position in csv file, it show the duplicate message
        print("You have already watched", all_movies[movie_number][0])
    else:
        all_movies[movie_number][3] = "u"
        print(all_movies[movie_number][0], "from", all_movies[movie_number][1], "watched")
        # Print which movie has been watched
        return all_movies


def count_number(choice):
    valid = False  # Make variable as False
    while not valid:
        try:
            input_number = int(input(choice))
            if input_number < 0:  # If the user input is less than 0, display the following message
                print("Number must be >= 0")
            elif input_number >= 7:  # If the user input more than 7, display the following message
                print("Invalid movie number")
            else:
                return input_number
        except ValueError:  # Except the error
            print("Invalid input; enter a valid number")


def add_movies():  # This function is used for adding new movie
    new_movie = []  # Create a list to save the new movie detail
    movie_title = word_input("Title: ")  # Enter the title
    year = str(count_number_year("Year: "))  # Enter the year
    category = word_input("Category: ")  # Enter the category
    new_movie.append(movie_title)
    new_movie.append(year)
    new_movie.append(category)
    new_movie.append("w")
    print(movie_title, "(", category, "from", "{:4}".format(year), ")", "added to movie list")  # Print movie message
    return new_movie


def word_input(choice):  # This function is used for collecting user nput and error checking
    input_string = input(choice)
    while len(input_string) == 0:  # Using the while loop to check if the user input blank
        print("Input can not be blank")  # Display the error message
        input_string = input(choice)
    return input_string.title()


def count_number_year(choice):  # This function is used for checking the new movie year while user entering year
    valid = False  # Make the variable as False
    while not valid:
        try:
            input_number = int(input(choice))  # Connect it with integer user input
            if input_number < 0:
                print("Number must be >= 0")  # Remind the user to enter the valid number
            else:
                return input_number  # Ask for the user input to rewrite the input_number
        except ValueError:  # Except the error
            print("Invalid input；enter a valid number")


def save_to_file(all_movies):  # This function is used to write the movie list to the csv file
    final_save = open("movies.csv", 'w')
    for i in range(len(all_movies)):  # Using the for loop and declare variable
        if i != 0:
            print("\n", end="", file=final_save)
        for j in range(len(all_movies[i])):  # Constant j represent the range of the list
            final_save.write(all_movies[i][j])  # Write the arranged data into the csv file
            if j != 3:
                print(",", end="", file=final_save)
    final_save.close()  # Close the csv file

# Finish


if __name__ == '__main__':
    main()
