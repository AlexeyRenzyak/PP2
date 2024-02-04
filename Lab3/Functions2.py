# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#1
def GoodMovie(name):
    for x in movies:
        if x["name"] == name:
            if x["imdb"] > 5.5:
                return True
            else:
                return False
    return False
print(GoodMovie("We Two"))

#2
def GoodMovies():
    goodmovies = []
    for x in movies:
        if x["imdb"] > 5.5:
            goodmovies.append(x["name"])
    return goodmovies
print(GoodMovies())

#3
def GenreMovies(genre):
    gmovies = []
    for x in movies:
        if genre == x["category"]:
            gmovies.append(x["name"])
    return gmovies
print(GenreMovies("Thriller"))

#4
def AverageScore(mlist):
    score = 0
    counter = 0
    for x in movies:
        if x["name"] in mlist:
            score += x["imdb"]
            counter += 1
    return score/counter
print(round(AverageScore(["We Two", "Hitman", "Exam"]), 2))

#5
def GenreAverageScore(genre):
    score = 0
    counter = 0
    for x in movies:
        if x["category"] == genre:
            score += x["imdb"]
            counter += 1
    return score/counter
print(round(GenreAverageScore("Thriller"), 2))