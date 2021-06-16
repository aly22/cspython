import json
import requests


def get_movies_from_tastedive(movie_name_or_artist_name):
    baseurl = "https://tastedive.com/api/similar"
    params_d = get_parameters(
        ['q', movie_name_or_artist_name, "type", "movies", "limit", 5])
    tastedive = requests.get(baseurl, params=params_d)

    return tastedive.json()


def get_parameters(lst: list) -> dict:
    params_d = {}

    for idx in range(0, len(lst) - 1, 2):
        params_d[lst[idx]] = lst[idx + 1]

    return params_d


def extract_movie_titles(movies_json):
    names = []
    for movie in movies_json['Similar']["Results"]:
        names.append(movie["Name"])

    return names


# def filtery(lst):
#     for title in extract_movie_titles(get_movies_from_tastedive(lst)):
#         started on filtering the movies but then realised that it's the same as the list comprehension --> can't refer to itself

def get_related_titles(lst_of_movies):
    related_titles = []

    # brelated=[title for movie in lst_of_movies for title in extract_movie_titles(get_movies_from_tastedive(movie)) if title not in related_titles]
    for movie in lst_of_movies:
        movie_json = get_movies_from_tastedive(movie)
        for title in extract_movie_titles(movie_json):
            if title not in related_titles:
                related_titles.append(title)
    return related_titles


def get_movie_data(movie):
    baseurl = "http://www.omdbapi.com/"
    params_d = get_parameters(["t", movie, 'r', 'json', 'apikey',
                               "2c4cc701"])
    movie_info = requests.get(baseurl, params_d)
    return movie_info.json()


def get_movie_rating(jsondata):
    RT_rating = 0
    for rating in jsondata["Ratings"]:
        if "Rotten Tomatoes" in rating["Source"]:
            RT_rating += int(rating["Value"][:-1])
            return RT_rating
    return 0


def get_sorted_recommendations(lst_of_movies):
    lst_of_recommendations = []
    ret_lst = []
    related_movies = get_related_titles(lst_of_movies)
    for movie in related_movies:
        rating = get_movie_rating(get_movie_data(movie))
        lst_of_recommendations.append([movie, rating])
    for recommendation in sorted(lst_of_recommendations,
                                 key=lambda x: (x[1], x[0]), reverse=True):
        ret_lst.append(recommendation)
    return [movie[0] for movie in ret_lst]


# print(get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"]))


# print(get_related_titles(["Black Panther", "Captain Marvel"]))
# cpt_marv=(get_movies_from_tastedive("Captain Marvel"))
# jsonobj=json.dumps(cpt_marv,indent=2)
# print(jsonobj)
def write_to_file(jsonobj):
    with open("movies.json", 'w') as file:
        json.dump(jsonobj, file)


# write_to_file(jsonobj)
def read_from_file(path):
    # data={}
    with open(path, "r") as file:
        data = json.load(file)
        return json.loads(data)

# movies = (read_from_file("movies.json"))
# movies = json.dumps(movies, indent=2)
# print(movies)
# print(extract_movie_titles(get_movies_from_tastedive("Black Panther")))

