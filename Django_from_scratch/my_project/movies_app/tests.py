from django.test import TestCase, Client

def add_two_numbers(a,b):
    return a+b
#python manage.py test
class TestExample(TestCase):
    def test_add_two_number(self):
        self.assertEqual(add_two_numbers(2,3),5)

class Test_add_movie(TestCase):
    @classmethod
    def setUpTestData(self):
        self.client = Client()
        self.newMovie = {
            "name": "mov 1",
            "lang":"Eng",
            "imdb_rating": 8,
            "year_of_release":2021,
            "director":"test 1"
        }
    def test_add_movie(self):
        response = self.client.post('/api/movies/',self.newMovie)
        self.assertEqual(response.status_code, 201)
    def test_add_movie_response(self):
        response = self.client.post('/api/movies/',self.newMovie)
        self.assertEqual(self.newMovie['name'], response.data['name']) 
        self.assertEqual(self.newMovie['lang'], response.data['lang'])  