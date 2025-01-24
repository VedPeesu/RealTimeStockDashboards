import unittest
from app import app

class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
    
    def tearDownn(self):
        pass

    def test_home_get(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Stock Dashboard', response.data)

    def test_home_post(self):
        response = self.app.post('/', data={'ticker': 'AAPL'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'currentPrice', response.data)
        self.assertIn(b'openPrice', response.data)

if __name__ == '__main__':
    unittest.main()