'''
create a list of 5 movies, print 1st, last, middle using both positive nd negative indexing
'''

movies = ["Weak Hero", "Moving", "Twinkling Watermelon", "Eternal Love", "Speed runner"]

print(f"List of movies: {movies}")
n = len(movies)
print(f"The length of list id : {len(movies)}")

print(f"the 1st element of list is: {movies[0]} ")
print(f"the middle element of list is: {movies[n//2]} ")
print(f"the last element of list is: {movies[-1]} ")