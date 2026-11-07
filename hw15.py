# 1
import json

def save_json(path, data):
    with open(path, 'w', encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
    return data

def load_json(path, default="არასწორი ფაილი"):
    try:
        with open(path, 'r', encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return default

data = {
    "name": "ნინო",
    "scores": [90, 85],
    "pair": (1, 2)
}

save_json("data/data.json", data)
data = load_json("data/data.json")

print(data)
print(type(data['pair']))
print(load_json("data/r.json"))


# 2

from dataclasses import dataclass, field, asdict

@dataclass
class Movie:
    title: str
    year: int = 2000
    rating: float = 0.0
    genres: list = field(default_factory=list)
    def __post_init__(self):
        if self.rating < 0 or self.rating > 10:
            raise ValueError("რეიტინგი უნდა იყოს 0-დან 10-მდე")


def best_movies(movies, min_rating):
    result = []
    for movie in movies:
        if movie.rating >= min_rating:
            result.append(movie)
    return sorted(result, key=lambda movie: movie.rating, reverse=True)

movie1 = Movie("მონანიება", 1984, 9.1, ["დრამა"])
movie2 = Movie("გზა", 2020, 7.5)
movie3 = Movie("მოგზაურობა", rating=8.2, genres=["თავგადასავალი"])

print(movie1)
movie4 = Movie("მონანიება", 1984, 9.1, ["დრამა"])
print(movie1 == movie4)
movie2.genres.append("კომედია")
print(movie2.genres, movie3.genres)

movies = [movie1, movie2, movie3]
result = best_movies(movies, 8)
for movie in result:
    print(movie.title, movie.rating)


print(json.dumps(asdict(movie1), ensure_ascii=False))

try:
    movie5 = Movie("ცუდი", 2000, 11)
except ValueError as error:
    print("შეცდომა:" ,error)



