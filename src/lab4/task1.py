class Movie:
    def __init__(self, movie_id, title):
        self.movie_id = movie_id
        self.title = title


class MovieData:
    def __init__(self, movies_file, history_file):
        self.movies_file = movies_file
        self.history_file = history_file

    def load_movies(self):
        movies = {}
        file = open(self.movies_file, "r", encoding="utf-8")
        for line in file:
            line = line.strip()
            if line == "":
                continue
            parts = line.split(",", 1)
            movie_id = int(parts[0])
            title = parts[1]
            movie = Movie(movie_id, title)
            movies[movie_id] = movie

        file.close()

        return movies

    def load_history(self):
        history = []
        file = open(self.history_file, "r", encoding="utf-8")
        for line in file:
            line = line.strip()
            if line == "":
                continue
            parts = line.split(",")
            user_history = []
            for part in parts:
                movie_id = int(part)
                user_history.append(movie_id)
            history.append(user_history)

        file.close()

        return history

class Recommendation:
    def __init__(self, movies, history):
        self.movies = movies
        self.history = history

    def recommend(self, user_movies):
        if len(user_movies) == 0:
            return None

        user_movies_set = set(user_movies)
        min_common_movies = (len(user_movies_set) + 1) // 2
        matched_histories = []
        for history in self.history:
            history_set = set(history)
            common_movies = user_movies_set.intersection(history_set)
            if len(common_movies) >= min_common_movies:
                matched_histories.append(history)

        candidates = {}
        for history in matched_histories:
            for movie_id in history:
                if movie_id not in user_movies_set:
                    if movie_id not in candidates:
                        candidates[movie_id] = 0
                    candidates[movie_id] = candidates[movie_id] + 1

        if len(candidates) == 0:
            return None

        recommended_id = max(candidates, key=candidates.get)
        if recommended_id not in self.movies:
            return None

        return self.movies[recommended_id].title



def main():
    movies_file = "movies.txt"
    history_file = "history.txt"
    data = MovieData(movies_file, history_file)
    movies = data.load_movies()
    history = data.load_history()

    service = Recommendation(movies, history)
    user_input = input()
    parts = user_input.split(",")
    user_movies = []

    for part in parts:
        movie_id = int(part)
        user_movies.append(movie_id)

    recommendation = service.recommend(user_movies)
    if recommendation is None:
        print("No recommendation")
    else:
        print(recommendation)



if __name__ == "__main__":
    main()





