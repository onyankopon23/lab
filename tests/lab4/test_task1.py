import unittest

from src.lab4.task1 import Movie, Recommendation


class RecommendationTestCase(unittest.TestCase):
    def test_example(self):
        movies = {
            1: Movie(1, "Мстители: Финал"),
            2: Movie(2, "Хатико"),
            3: Movie(3, "Дюна"),
            4: Movie(4, "Унесенные призраками")
        }
        history = [[2, 1, 3],
                   [1, 4, 3],
                   [2, 2, 2, 2, 2, 3]]
        recommendation = Recommendation(movies, history)
        self.assertEqual(recommendation.recommend([2, 4]), "Дюна")

    def test_empty_user_movies(self):
        movies = {
            1: Movie(1, "Мстители: Финал"),
            2: Movie(2, "Хатико")
        }
        history = [[1, 2]]
        recommendation = Recommendation(movies, history)
        self.assertEqual(recommendation.recommend([]), None)

    def test_no_matched_histories(self):
        movies = {
            1: Movie(1, "Фильм 1"),
            2: Movie(2, "Фильм 2"),
            3: Movie(3, "Фильм 3"),
            4: Movie(4, "Фильм 4")
        }
        history = [[3, 4]]
        recommendation = Recommendation(movies, history)
        self.assertEqual(recommendation.recommend([1, 2]), None)

    def test_half_movies_match(self):
        movies = {
            1: Movie(1, "Фильм 1"),
            2: Movie(2, "Фильм 2"),
            3: Movie(3, "Фильм 3")
        }
        history = [[1, 3]]
        recommendation = Recommendation(movies, history)
        self.assertEqual(recommendation.recommend([1, 2]), "Фильм 3")

    def test_watched_movies_not_recommended(self):
        movies = {
            1: Movie(1, "Фильм 1"),
            2: Movie(2, "Фильм 2"),
            3: Movie(3, "Фильм 3")
        }
        history = [[1, 2, 3]]
        recommendation = Recommendation(movies, history)
        self.assertEqual(recommendation.recommend([1, 2]), "Фильм 3")

    def test_all_movies_watched(self):
        movies = {
            1: Movie(1, "Фильм 1"),
            2: Movie(2, "Фильм 2")
        }
        history = [[1, 2]]
        recommendation = Recommendation(movies, history)
        self.assertEqual(recommendation.recommend([1, 2]), None)

    def test_most_popular_movie(self):
        movies = {
            1: Movie(1, "Фильм 1"),
            2: Movie(2, "Фильм 2"),
            3: Movie(3, "Фильм 3"),
            4: Movie(4, "Фильм 4")
        }
        history = [
            [1, 3],
            [1, 3],
            [1, 4]
        ]
        recommendation = Recommendation(movies, history)
        self.assertEqual(recommendation.recommend([1]), "Фильм 3")