from flask_testing import TestCase
from app import app
import unittest


class IndexTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app
    
    def test_get_index(self):
        response = self.client.get('/')
        self.assert200(response)
        print(response.data)


if __name__ == "__main__":
    unittest.main()
