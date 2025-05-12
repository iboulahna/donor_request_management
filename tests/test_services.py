import unittest
from app.services.query_handler import generate_response

class TestQueryHandler(unittest.TestCase):

    def test_generate_response(self):
        query = "I would like to increase my monthly donation."
        response = generate_response(query)
        self.assertIn("increase", response)

if __name__ == '__main__':
    unittest.main()
